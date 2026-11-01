---
name: k6-performance
description: Design, implement and analyze k6 performance tests including smoke, load, stress and spike profiles, thresholds, workload models and CI reporting.
---
# k6 Performance Testing Skill

## Mission
Create safe, explainable performance tests whose workload and thresholds reflect an agreed performance question and service objectives.

## Mandatory preconditions
Before execution, establish explicitly authorized target/environment, owner and escalation path, workload profile and maximum load, test window/duration, approved thresholds/SLOs, test data, monitoring and stop conditions. If missing, design but do not execute. Never target production without explicit written authorization and coordination.

## Test types
- Smoke: very low load to validate script and target readiness.
- Load: expected normal or peak workload.
- Stress: controlled increase to identify limits.
- Spike: short, controlled abrupt load change.
- Soak: sustained load to identify degradation.

## Workload design
- Explain VUs or arrival-rate model and why it matches expected traffic.
- Define ramp-up, steady state, ramp-down and duration.
- Model realistic think time and request mix.
- Use synthetic data and safe test accounts.
- Set conservative maximums and abort/stop criteria.
- Do not invent SLAs or thresholds; ask for approved values.

## Script and analysis
- Reuse HTTP helpers and checks where appropriate.
- Use tags for endpoint, scenario and environment.
- Avoid logging secrets or sensitive payloads.
- Set thresholds from agreed SLOs.
- Correlate k6 output with server metrics/logs.
- Report p50/p90/p95/p99 where available, throughput, error rate, checks and limitations.

## Example command (do not run until authorized)
```powershell
k6 version
k6 run --vus 1 --duration 30s .\performance\smoke.js
```

## Output
Provide objective, workload assumptions, scenario, thresholds, script, execution prerequisites, analysis and recommendations.
