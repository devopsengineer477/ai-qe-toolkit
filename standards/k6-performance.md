# k6 Performance Testing Standards

- Define the performance question and workload model before writing a script.
- Record assumptions for virtual users, arrival rate, ramp-up, duration and data.
- Define thresholds from approved SLAs/SLOs; never invent acceptance limits.
- Start with a low-volume smoke test against an authorized non-production target.
- Monitor target health and stop if agreed safety limits are exceeded.
- Avoid production load tests without explicit written approval and coordination.
- Use synthetic data and protect credentials.
- Separate functional checks from performance thresholds.
- Preserve summaries and relevant trend data.
