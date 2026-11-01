# QE Reporting Data Contract

## Canonical execution run
All adapters normalize results to `schemas/execution-run.schema.json`.

Required provenance:
- `run_id`, `source`, `started_at`
- project/environment/branch/commit when available
- source artifact filename(s)
- summary counts and test-level records

Each test record has a stable `test_id`, display name, suite, status, duration, message, requirement/defect references and evidence references.

## Supported inputs in v0.5.0
- JUnit XML (including common pytest and Playwright JUnit output)
- .NET TRX XML
- Newman JSON report
- k6 JSON summary export

Jenkins and GitHub Actions are represented by their underlying published artifacts/logs in this release. Native live API ingestion is not included.

## Status mapping
- passed: successful test outcome
- failed: assertion, error or failed request outcome
- skipped: intentionally skipped/not executed test
- not_run: planned but not executed (requires an explicit source record)

A missing result is not automatically classified as skipped or not_run.

## Metric definitions
- Pass rate = passed / (passed + failed); skipped excluded.
- Requirement coverage = in-scope requirements with at least one traceability row / in-scope requirements.
- Not-run and skipped counts are reported separately.
- Flaky tests require history across comparable runs and stable test identity; this release does not infer flakiness from one run.
- Defect escape rate is not calculated without an agreed escaped-defect dataset and observation window.

## Provenance and privacy
Raw artifacts should be retained unchanged and stored separately from normalized reports. Do not put tokens, passwords, customer payloads or personal data in messages or evidence. Report paths are references, not copies of raw evidence.
