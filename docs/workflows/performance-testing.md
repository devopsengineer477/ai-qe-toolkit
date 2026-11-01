# Performance Testing Workflow

1. Use `k6-performance` skill.
2. Define business transaction, SLOs, workload model, ramp-up, duration and stop conditions.
3. Confirm the exact target environment and system-owner authorization.
4. Start with script validation and a low-volume smoke profile against a controlled environment.
5. Obtain explicit approval for load, stress, spike or soak tests, including concurrency, duration and monitoring.
6. Monitor service health and stop if agreed thresholds are exceeded.
7. Report workload, environment, achieved load, latency percentiles, error rate, resource observations and limitations.
