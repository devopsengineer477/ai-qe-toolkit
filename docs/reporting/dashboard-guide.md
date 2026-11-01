# Dashboard Guide

The report generator creates:
- `qe-report.json`: machine-readable metrics, run inventory, failures, gates and limitations.
- `index.html`: self-contained browser dashboard.

The dashboard is intentionally static and dependency-free. It is suitable for CI artifacts or local review, not a multi-user SaaS dashboard. Do not publish reports containing confidential failure messages or internal hostnames to public artifact storage.

For QualityPilot AI, the JSON report and canonical schema can become the ingestion contract for a future API, database and interactive dashboard.
