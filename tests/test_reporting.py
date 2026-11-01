import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

normalizer = load_module("normalizer", "scripts/normalize_results.py")
report_builder = load_module("report_builder", "scripts/build_qe_report.py")

class ReportingPipelineTests(unittest.TestCase):
    def args(self, path):
        return SimpleNamespace(
            input=str(path), run_id="test-run", project="test", environment="local",
            branch=None, commit_sha=None
        )

    def test_junit_normalization_counts(self):
        run = normalizer.parse_junit(ROOT/"examples/reporting/junit-sample.xml", self.args("junit"))
        self.assertEqual(run["summary"]["total"], 6)
        self.assertEqual(run["summary"]["passed"], 4)
        self.assertEqual(run["summary"]["failed"], 1)
        self.assertEqual(run["summary"]["skipped"], 1)

    def test_dotnet_trx_normalization(self):
        run = normalizer.parse_trx(ROOT/"examples/reporting/dotnet-sample.trx", self.args("trx"))
        self.assertEqual(run["summary"]["total"], 3)
        self.assertEqual(run["summary"]["passed"], 1)
        self.assertEqual(run["summary"]["failed"], 1)
        self.assertEqual(run["summary"]["skipped"], 1)

    def test_newman_normalization(self):
        run = normalizer.parse_newman(ROOT/"examples/reporting/newman-sample.json", self.args("newman"))
        self.assertEqual(run["summary"]["total"], 3)
        self.assertEqual(run["summary"]["failed"], 1)

    def test_k6_is_not_counted_as_test_pass(self):
        run = normalizer.parse_k6(ROOT/"examples/reporting/k6-summary-sample.json", self.args("k6"))
        self.assertEqual(run["summary"]["total"], 0)
        self.assertEqual(run["quality_signals"]["http_requests"], 1200)

    def test_report_metrics_and_gates(self):
        args = self.args("input")
        runs = [
            normalizer.parse_junit(ROOT/"examples/reporting/junit-sample.xml", args),
            normalizer.parse_newman(ROOT/"examples/reporting/newman-sample.json", args),
            normalizer.parse_k6(ROOT/"examples/reporting/k6-summary-sample.json", args)
        ]
        requirements = report_builder.read_csv(ROOT/"examples/reporting/requirements.csv")
        traceability = report_builder.read_csv(ROOT/"examples/reporting/traceability.csv")
        metrics = report_builder.aggregate(runs, requirements, traceability)
        self.assertEqual(metrics["execution"]["total"], 9)
        self.assertEqual(metrics["execution"]["pass_rate_percent"], 75.0)
        self.assertEqual(metrics["requirements"]["coverage_percent"], 80.0)
        self.assertEqual(metrics["data_quality"]["tests_without_requirement_links"], 5)
        gates = report_builder.evaluate_gates(metrics, json.loads((ROOT/"config/release-gates.example.json").read_text()))
        self.assertEqual([g["status"] for g in gates], ["fail","fail","fail"])

if __name__ == "__main__":
    unittest.main()
