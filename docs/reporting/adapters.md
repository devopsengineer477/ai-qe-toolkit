# Reporting Adapters

## Current command-line adapters

```powershell
# JUnit XML from pytest / Playwright / Jenkins JUnit publisher
python scripts/normalize_results.py --format junit --input examples/reporting/junit-sample.xml --output reports/normalized/api-run.json --project QualityPilot --environment staging

# Newman JSON report
python scripts/normalize_results.py --format newman --input examples/reporting/newman-sample.json --output reports/normalized/newman-run.json --project QualityPilot --environment staging

# k6 JSON summary export
python scripts/normalize_results.py --format k6-summary --input examples/reporting/k6-summary-sample.json --output reports/normalized/performance-run.json --project QualityPilot --environment staging

# .NET TRX
python scripts/normalize_results.py --format dotnet-trx --input TestResults/results.trx --output reports/normalized/dotnet-run.json
```

## Build consolidated report

```powershell
python scripts/build_qe_report.py `
  --runs reports/normalized/api-run.json reports/normalized/newman-run.json reports/normalized/performance-run.json `
  --requirements examples/reporting/requirements.csv `
  --traceability examples/reporting/traceability.csv `
  --thresholds config/release-gates.example.json `
  --out-dir reports/latest
```

Open `reports/latest/index.html` in a browser.

## CI integration pattern
Publish raw result artifacts from each job, download them in a report job, normalize them, build the consolidated report, and publish `reports/latest/` as a CI artifact. Keep raw artifacts for audit and reprocessing. Use immutable run IDs and attach commit SHA/environment metadata.

## Adapter limitations
- JUnit parser supports common `<testsuite>` / `<testsuites>` layouts.
- Newman parser maps request executions and assertion failures; it does not preserve full request/response bodies.
- k6 parser consumes a summary JSON export; it does not execute k6.
- TRX parser supports common `UnitTestResult` outcomes; validate against your test platform's TRX variant.
- Direct Jenkins/GitHub/Atlassian API ingestion is not included.
