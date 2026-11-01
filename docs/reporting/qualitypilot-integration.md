# Future QualityPilot AI Integration

The canonical `execution-run` and `qe-report` schemas are designed as a boundary between execution adapters and a future QualityPilot AI service.

Suggested future flow:
1. CI adapters upload raw artifacts to object storage.
2. A backend ingestion service normalizes each artifact to the execution-run schema.
3. A queue/job processor validates and persists normalized runs.
4. A metrics service aggregates by project, branch, environment and release.
5. A dashboard API serves time-series and release reports.
6. An AI analysis service summarizes trends and proposes investigations, always linking back to source evidence.

Suggested future entities: `Project`, `Requirement`, `TestCase`, `AutomationAsset`, `ExecutionRun`, `TestResult`, `Defect`, `EvidenceArtifact`, `ReleaseGate`, `MetricSnapshot`.

Do not let an LLM invent metric values or infer missing test outcomes. AI summaries should consume validated metrics and link to evidence.
