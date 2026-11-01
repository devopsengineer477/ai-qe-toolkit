# CI Integration Pattern

A recommended CI pattern is to add a report aggregation job after framework-specific jobs complete.

1. Each test job publishes raw JUnit/TRX/Newman/k6 artifacts.
2. A downstream reporting job downloads the artifacts for the same commit and environment.
3. The job runs the relevant normalizers.
4. It invokes `build_qe_report.py` with normalized runs, requirements, traceability and release thresholds.
5. It publishes `reports/latest/index.html` and `qe-report.json` as restricted CI artifacts.
6. It retains original raw artifacts according to the organization's audit policy.

Do not merge runs from different commits or environments into one release report unless that aggregation is intentional and clearly labelled. Use stable run IDs and include branch/commit/environment metadata. Protect reports that contain internal failure details.
