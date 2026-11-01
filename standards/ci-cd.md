# Jenkins / GitHub Actions Standards

- Apply least privilege to agents, service accounts and tokens.
- Store secrets in Jenkins Credentials or GitHub Actions secrets/environments.
- Do not echo secrets or enable verbose shell tracing around credentials.
- Fail the pipeline on failed quality gates; do not swallow exit codes.
- Use explicit timeouts and concurrency controls.
- Publish test, coverage and diagnostic artifacts even when practical after failures.
- Separate build, test, scan and deploy stages.
- Protect production deployments with approvals and environment controls.
