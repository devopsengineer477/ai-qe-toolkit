#!/usr/bin/env python3
"""Aggregate normalized runs into a QE report JSON and self-contained HTML dashboard."""
from __future__ import annotations
import argparse, csv, html, json, sys
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter, defaultdict

def read_csv(path):
    if not path:
        return []
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def load_runs(paths):
    runs=[]
    for p in paths:
        data=json.loads(Path(p).read_text(encoding="utf-8"))
        if data.get("schema_version") != "1.0" or not isinstance(data.get("tests"), list):
            raise ValueError(f"Unsupported normalized run: {p}")
        runs.append(data)
    return runs

def aggregate(runs, requirements, traceability):
    counts=Counter()
    all_tests=[]
    linked_by_test=defaultdict(set)
    for row in traceability:
        test_id=row.get("test_id")
        requirement_id=row.get("requirement_id")
        if test_id and requirement_id:
            linked_by_test[test_id].add(requirement_id)
    for run in runs:
        counts.update(run.get("summary", {}))
        for test in run.get("tests", []):
            # Enrich test records from the explicit traceability file without changing raw normalized evidence.
            enriched=dict(test)
            enriched["requirement_ids"]=sorted(set(enriched.get("requirement_ids", [])) | linked_by_test.get(enriched.get("test_id"), set()))
            all_tests.append(enriched)
    total=counts["total"]
    executed=counts["passed"]+counts["failed"]
    pass_rate=(counts["passed"]/executed*100) if executed else None
    in_scope=[r for r in requirements if str(r.get("in_scope","true")).lower() in ("true","1","yes","y")]
    linked={r.get("requirement_id") for r in traceability if r.get("requirement_id")}
    covered={r.get("requirement_id") for r in in_scope if r.get("requirement_id") in linked}
    coverage=(len(covered)/len(in_scope)*100) if in_scope else None
    failing=sorted([t for t in all_tests if t.get("status")=="failed"], key=lambda x:x.get("test_id",""))
    by_source=defaultdict(Counter)
    for run in runs:
        for k,v in run.get("summary",{}).items():
            if isinstance(v,int):
                by_source[run.get("source","unknown")][k]+=v
    perf={}
    for run in runs:
        if run.get("source")=="k6-summary":
            perf[run.get("run_id")]=run.get("quality_signals",{})
    return {
      "execution":{"total":total,"passed":counts["passed"],"failed":counts["failed"],"skipped":counts["skipped"],"not_run":counts["not_run"],"executed":executed,"pass_rate_percent":round(pass_rate,2) if pass_rate is not None else None},
      "requirements":{"in_scope":len(in_scope),"covered":len(covered),"uncovered":max(0,len(in_scope)-len(covered)),"coverage_percent":round(coverage,2) if coverage is not None else None},
      "failures":[{"test_id":t.get("test_id"),"name":t.get("name"),"suite":t.get("suite"),"message":t.get("message"),"source":next((r.get("source") for r in runs if t in r.get("tests",[])),None)} for t in failing],
      "by_source":{k:dict(v) for k,v in by_source.items()},
      "performance":perf,
      "data_quality":{"runs":len(runs),"tests_without_requirement_links":sum(1 for t in all_tests if not t.get("requirement_ids")),"requirements_without_linked_tests":max(0,len(in_scope)-len(covered))}
    }

def evaluate_gates(metrics, thresholds):
    gates=[]
    execm=metrics["execution"]
    reqm=metrics["requirements"]
    def add(name, actual, threshold, passed, note):
        gates.append({"name":name,"actual":actual,"threshold":threshold,"status":"pass" if passed else "fail" if actual is not None else "not_evaluated","note":note})
    min_pass=thresholds.get("min_pass_rate_percent")
    if min_pass is not None:
        actual=execm["pass_rate_percent"]
        add("Minimum test pass rate",actual,min_pass,actual is not None and actual>=min_pass,"Uses passed / (passed + failed); skipped tests excluded.")
    max_fail=thresholds.get("max_failed_tests")
    if max_fail is not None:
        actual=execm["failed"]
        add("Maximum failed tests",actual,max_fail,actual<=max_fail,"Failed test count across included runs.")
    min_cov=thresholds.get("min_requirement_coverage_percent")
    if min_cov is not None:
        actual=reqm["coverage_percent"]
        add("Minimum requirement coverage",actual,min_cov,actual is not None and actual>=min_cov,"Coverage depends on supplied requirements.csv and traceability.csv.")
    if not gates:
        gates.append({"name":"Release gates","actual":None,"threshold":None,"status":"not_configured","note":"No release thresholds configured; report is informational only."})
    return gates

def safe_json(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")

def make_html(report):
    m=report["metrics"]; e=m["execution"]; r=m["requirements"]
    def val(x, suffix=""):
        return "N/A" if x is None else f"{x}{suffix}"
    rows=[]
    for gate in report["release_gates"]:
        status=gate["status"].replace("_"," ").upper()
        rows.append(f"<tr><td>{html.escape(gate['name'])}</td><td>{html.escape(val(gate['actual']))}</td><td>{html.escape(val(gate['threshold']))}</td><td><span class='tag {html.escape(gate['status'])}'>{html.escape(status)}</span></td><td>{html.escape(gate['note'])}</td></tr>")
    failures=[]
    for item in m["failures"]:
        failures.append("<tr><td>"+html.escape(str(item.get("test_id") or ""))+"</td><td>"+html.escape(str(item.get("name") or ""))+"</td><td>"+html.escape(str(item.get("source") or ""))+"</td><td>"+html.escape(str(item.get("message") or ""))+"</td></tr>")
    if not failures:
        failures=["<tr><td colspan='4'>No failed tests in supplied evidence.</td></tr>"]
    payload=safe_json(report)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI QE Toolkit — Quality Report</title>
<style>
:root{{font-family:Inter,Segoe UI,Arial,sans-serif;color:#172033;background:#f5f7fb}}body{{margin:0;padding:28px}}main{{max-width:1180px;margin:auto}}h1{{margin-bottom:4px}}.muted{{color:#65718a}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:14px;margin:22px 0}}.card,section{{background:#fff;border:1px solid #e2e7f0;border-radius:12px;padding:18px}}.value{{font-size:28px;font-weight:700;margin-top:8px}}section{{margin:16px 0;overflow:auto}}table{{border-collapse:collapse;width:100%;font-size:14px}}th,td{{text-align:left;border-bottom:1px solid #e7ebf2;padding:10px;vertical-align:top}}th{{color:#59647a}}.tag{{padding:4px 8px;border-radius:999px;font-size:11px;font-weight:700;background:#edf0f5}}.pass{{background:#e4f6eb;color:#17643b}}.fail{{background:#fde8e8;color:#9d2525}}.not_evaluated,.not_configured{{background:#eef1f6;color:#536078}}.bar{{height:12px;background:#e9edf4;border-radius:8px;overflow:hidden;margin-top:10px}}.bar>i{{display:block;height:100%;background:#2774c7}}footer{{font-size:12px;color:#69758b;margin-top:24px}}@media(max-width:600px){{body{{padding:14px}}}}
</style></head><body><main>
<h1>Quality Engineering Report</h1><div class="muted">Generated {html.escape(report['generated_at'])} · {len(report['runs'])} run(s)</div>
<div class="grid">
<div class="card"><div class="muted">Total test records</div><div class="value">{e['total']}</div></div>
<div class="card"><div class="muted">Passed</div><div class="value">{e['passed']}</div></div>
<div class="card"><div class="muted">Failed</div><div class="value">{e['failed']}</div></div>
<div class="card"><div class="muted">Skipped</div><div class="value">{e['skipped']}</div></div>
<div class="card"><div class="muted">Pass rate</div><div class="value">{val(e['pass_rate_percent'],'%')}</div><div class="bar"><i style="width:{max(0,min(100,e['pass_rate_percent'] or 0))}%"></i></div></div>
<div class="card"><div class="muted">Requirement coverage</div><div class="value">{val(r['coverage_percent'],'%')}</div><div class="bar"><i style="width:{max(0,min(100,r['coverage_percent'] or 0))}%"></i></div></div>
</div>
<section><h2>Release gates</h2><table><thead><tr><th>Gate</th><th>Actual</th><th>Threshold</th><th>Status</th><th>Notes</th></tr></thead><tbody>{''.join(rows)}</tbody></table></section>
<section><h2>Failed tests</h2><table><thead><tr><th>Test ID</th><th>Name</th><th>Source</th><th>Failure message</th></tr></thead><tbody>{''.join(failures)}</tbody></table></section>
<section><h2>Run inventory</h2><table><thead><tr><th>Run ID</th><th>Source</th><th>Project</th><th>Environment</th><th>Commit</th><th>Total</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr></thead><tbody>
{''.join(f"<tr><td>{html.escape(str(x.get('run_id')))}</td><td>{html.escape(str(x.get('source')))}</td><td>{html.escape(str(x.get('project') or ''))}</td><td>{html.escape(str(x.get('environment') or ''))}</td><td>{html.escape(str(x.get('commit_sha') or ''))}</td><td>{x.get('summary',{}).get('total',0)}</td><td>{x.get('summary',{}).get('passed',0)}</td><td>{x.get('summary',{}).get('failed',0)}</td><td>{x.get('summary',{}).get('skipped',0)}</td></tr>" for x in report['runs'])}
</tbody></table></section>
<section><h2>Performance signals</h2><pre>{html.escape(json.dumps(m['performance'],indent=2))}</pre></section>
<section><h2>Data quality and limitations</h2><pre>{html.escape(json.dumps(m['data_quality'],indent=2))}</pre><ul>{''.join('<li>'+html.escape(x)+'</li>' for x in report.get('limitations',[]))}</ul></section>
<footer>Generated by AI QE Toolkit v0.5.0. This report summarizes supplied evidence only; it does not independently verify test execution or release fitness.</footer>
<script type="application/json" id="report-data">{payload}</script>
</main></body></html>"""

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs",nargs="+",required=True,help="Normalized execution-run JSON files")
    ap.add_argument("--requirements")
    ap.add_argument("--traceability")
    ap.add_argument("--thresholds",help="JSON file containing release thresholds")
    ap.add_argument("--out-dir",default="reports/latest")
    args=ap.parse_args()
    try:
        runs=load_runs(args.runs)
        req=read_csv(args.requirements); trace=read_csv(args.traceability)
        metrics=aggregate(runs,req,trace)
        thresholds=json.loads(Path(args.thresholds).read_text(encoding="utf-8")) if args.thresholds else {}
        gates=evaluate_gates(metrics,thresholds)
        limitations=[]
        if not req: limitations.append("Requirement coverage was not calculated: no requirements CSV supplied.")
        if not trace: limitations.append("Requirement-to-test traceability was not supplied.")
        if len(runs)<2: limitations.append("Trend metrics are unavailable: fewer than two comparable runs supplied.")
        if any(r.get("source")=="k6-summary" for r in runs): limitations.append("k6 summary metrics are descriptive; SLO evaluation requires explicit performance thresholds.")
        report={"schema_version":"1.0","generated_at":datetime.now(timezone.utc).isoformat(),"runs":runs,
                "metrics":metrics,"release_gates":gates,"limitations":limitations}
        out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
        (out/"qe-report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
        (out/"index.html").write_text(make_html(report),encoding="utf-8")
        print(f"QE report generated: {out/'index.html'}")
        print(f"JSON evidence report: {out/'qe-report.json'}")
        print(f"Runs={len(runs)} tests={metrics['execution']['total']} pass_rate={metrics['execution']['pass_rate_percent']} requirement_coverage={metrics['requirements']['coverage_percent']}")
        return 0
    except Exception as exc:
        print(f"Report generation failed: {type(exc).__name__}: {exc}",file=sys.stderr)
        return 2

if __name__=="__main__":
    sys.exit(main())
