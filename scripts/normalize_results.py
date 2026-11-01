#!/usr/bin/env python3
"""Normalize common QE test result formats into the toolkit execution-run schema."""
from __future__ import annotations
import argparse, json, re, sys, uuid
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

def iso_now():
    return datetime.now(timezone.utc).isoformat()

def clean_text(value, limit=1200):
    if value is None:
        return None
    value = re.sub(r"(?i)(authorization:\s*(?:bearer|basic)\s+)[^\s]+", r"\1[REDACTED]", str(value))
    value = re.sub(r"(?i)(password|token|secret|api[_-]?key)(\s*[=:]\s*)[^\s,;]+", r"\1\2[REDACTED]", value)
    return value[:limit]

def status_counts(tests):
    counts = {k: 0 for k in ("passed", "failed", "skipped", "not_run")}
    for test in tests:
        counts[test["status"]] += 1
    return {"total": len(tests), **counts}

def make_run(source, tests, args, started_at=None, duration=None, quality_signals=None):
    for test in tests:
        test.setdefault("suite", None)
        test.setdefault("duration_seconds", None)
        test.setdefault("message", None)
        test.setdefault("requirement_ids", [])
        test.setdefault("defect_ids", [])
        test.setdefault("evidence", [])
    return {
        "schema_version": "1.0",
        "run_id": args.run_id or f"{source}-{uuid.uuid4().hex[:10]}",
        "source": source,
        "project": args.project,
        "environment": args.environment,
        "branch": args.branch,
        "commit_sha": args.commit_sha,
        "started_at": started_at or iso_now(),
        "duration_seconds": duration,
        "source_artifacts": [str(Path(args.input).name)],
        "summary": status_counts(tests),
        "tests": tests,
        "quality_signals": quality_signals or {},
        "metadata": {"normalizer_version": "0.5.0"}
    }

def parse_junit(path, args):
    root = ET.parse(path).getroot()
    suites = [root] if root.tag.endswith("testsuite") else list(root.iter("testsuite"))
    tests = []
    for suite in suites:
        suite_name = suite.attrib.get("name")
        for case in suite.findall("testcase"):
            failure = case.find("failure")
            error = case.find("error")
            skipped = case.find("skipped")
            node = failure if failure is not None else error
            status = "failed" if node is not None else ("skipped" if skipped is not None else "passed")
            message = None
            if node is not None:
                message = clean_text((node.attrib.get("message", "") + " " + (node.text or "")).strip())
            elif skipped is not None:
                message = clean_text(skipped.attrib.get("message") or skipped.text)
            classname = case.attrib.get("classname") or suite_name or ""
            name = case.attrib.get("name", "unnamed")
            test_id = ".".join(x for x in (classname, name) if x)
            try:
                duration = float(case.attrib["time"]) if "time" in case.attrib else None
            except ValueError:
                duration = None
            tests.append({
                "test_id": test_id, "name": name, "suite": suite_name or classname,
                "status": status, "duration_seconds": duration, "message": message,
                "requirement_ids": [], "defect_ids": [], "evidence": []
            })
    total_time = root.attrib.get("time")
    try:
        duration = float(total_time) if total_time else None
    except ValueError:
        duration = None
    return make_run("junit", tests, args, duration=duration)

def parse_trx(path, args):
    tree = ET.parse(path)
    root = tree.getroot()
    ns = {"t": root.tag.split("}")[0].strip("{")} if "}" in root.tag else {}
    def findall(node, path):
        return node.findall(path, ns) if ns else node.findall(path.replace("t:", ""))
    tests = []
    for result in findall(root, ".//t:UnitTestResult"):
        outcome = result.attrib.get("outcome", "").lower()
        status = "passed" if outcome in ("passed", "completed") else ("skipped" if outcome in ("notexecuted", "pending", "inconclusive") else "failed")
        name = result.attrib.get("testName", "unnamed")
        test_id = result.attrib.get("testId") or name
        msg = None
        output = findall(result, ".//t:Message")
        if output:
            msg = clean_text(output[0].text)
        duration = None
        # TRX duration is hh:mm:ss.fffffff
        raw = result.attrib.get("duration")
        if raw:
            try:
                h, m, sec = raw.split(":")
                duration = int(h) * 3600 + int(m) * 60 + float(sec)
            except Exception:
                pass
        tests.append({"test_id":test_id,"name":name,"suite":None,"status":status,
                      "duration_seconds":duration,"message":msg,"requirement_ids":[],"defect_ids":[],"evidence":[]})
    return make_run("dotnet-trx", tests, args)

def parse_newman(path, args):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    executions = data.get("run", {}).get("executions", data.get("executions", []))
    if not executions and isinstance(data.get("executions"), list):
        executions = data["executions"]
    tests = []
    for i, execution in enumerate(executions):
        item = execution.get("item") or {}
        name = item.get("name") or f"request-{i+1}"
        request = execution.get("request") or {}
        url = request.get("url")
        if isinstance(url, dict):
            url = url.get("raw")
        method = request.get("method", "")
        assertions = execution.get("assertions") or []
        errors = [a for a in assertions if a.get("error")]
        response = execution.get("response") or {}
        status_code = response.get("code")
        failed = bool(errors) or (isinstance(status_code, int) and status_code >= 400)
        status = "failed" if failed else "passed"
        msg = "; ".join(clean_text((e.get("assertion") or "assertion") + ": " + str((e.get("error") or {}).get("message", ""))) for e in errors) or None
        # Avoid embedding full URLs/query strings in test IDs or report labels.
        endpoint = ""
        if url:
            endpoint = re.sub(r"^https?://[^/]+", "", str(url).split("?")[0])
        test_id = ".".join(x for x in (method, endpoint, name) if x)
        tests.append({"test_id":test_id,"name":name,"suite":"Newman","status":status,
                      "duration_seconds":(response.get("responseTime") or 0)/1000 if response.get("responseTime") is not None else None,
                      "message":msg,"requirement_ids":[],"defect_ids":[],"evidence":[]})
    timings = data.get("run", {}).get("timings", {})
    started = None
    if timings.get("started"):
        try:
            started = datetime.fromtimestamp(timings["started"]/1000, timezone.utc).isoformat()
        except Exception:
            pass
    duration = None
    if timings.get("started") and timings.get("completed"):
        duration = max(0, (timings["completed"]-timings["started"])/1000)
    return make_run("newman", tests, args, started_at=started, duration=duration)

def parse_k6(path, args):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    metrics = data.get("metrics", {})
    def values(name):
        return (metrics.get(name) or {}).get("values", {})
    duration = values("http_req_duration")
    failed = values("http_req_failed")
    reqs = values("http_reqs")
    vus = values("vus_max")
    signals = {
        "http_req_duration_ms": {k: duration.get(k) for k in ("avg","med","p(90)","p(95)","max") if k in duration},
        "http_req_failed_rate": failed.get("rate"),
        "http_requests": reqs.get("count"),
        "http_requests_per_second": reqs.get("rate"),
        "vus_max": vus.get("value")
    }
    # k6 summary metrics are performance measurements, not discrete test cases.
    # Keep the test list empty so the report does not invent a 100% pass rate.
    return make_run("k6-summary", [], args, quality_signals=signals)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", required=True, choices=["junit","dotnet-trx","newman","k6-summary"])
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--run-id")
    parser.add_argument("--project")
    parser.add_argument("--environment")
    parser.add_argument("--branch")
    parser.add_argument("--commit-sha")
    args = parser.parse_args()
    try:
        if args.format == "junit":
            run = parse_junit(args.input, args)
        elif args.format == "dotnet-trx":
            run = parse_trx(args.input, args)
        elif args.format == "newman":
            run = parse_newman(args.input, args)
        else:
            run = parse_k6(args.input, args)
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(json.dumps(run, indent=2), encoding="utf-8")
        print(f"Normalized {run['source']} evidence: {run['summary']['total']} test records -> {args.output}")
        return 0
    except Exception as exc:
        print(f"Normalization failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
