# QE Metrics Catalogue

| Metric | Definition | Data needed | Interpretation caution |
|---|---|---|---|
| Pass rate | Passed / (passed + failed) | Test outcomes | Excludes skipped; always show denominator |
| Execution completion | Executed / planned | Explicit planned and executed inventory | Not calculated when planned inventory is absent |
| Requirement coverage | In-scope requirements linked to tests / in-scope requirements | Requirements and traceability | A link does not prove test quality |
| Defect density | Defects / size unit | Defects and agreed size measure | Compare only consistent products/releases |
| Defect escape rate | Production escaped defects / all defects in cohort | Production defect linkage and cohort | Not available from test run data alone |
| Flaky rate | Tests with inconsistent outcomes / tests observed repeatedly | Comparable run history | Needs stable test IDs and sufficient repetitions |
| Mean time to restore | Time from incident start to service restoration | Incident timestamps | Use incident-management source |
| p95 latency | 95th percentile response duration | Performance test metrics | Include workload, environment and duration |
| Error rate | Failed requests / total requests | Load test metrics | Distinguish HTTP errors from transport failures |
| Pipeline reliability | Successful pipeline runs / completed pipeline runs | CI run history | Define treatment of cancellations and manual reruns |

## Dashboard principles
- Show numerator and denominator for rates.
- Display time range, environment, branch and commit.
- Mark missing/insufficient data as N/A.
- Avoid ranking teams by raw pass rate without context.
- Pair quality indicators with test coverage and product risk.
