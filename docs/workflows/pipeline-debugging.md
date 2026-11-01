# Pipeline Debugging Workflow

1. Use `ci-cd-automation` and the CI Pipeline Reviewer agent.
2. Inspect the failing stage, logs, agent image, tool versions, environment variables and artifact paths.
3. Separate infrastructure, configuration, test and product failures.
4. Check permissions using least privilege; never print secret values.
5. Propose the smallest change and add validation where possible.
6. Do not rerun a deployment or mutate shared infrastructure without explicit approval.
7. Report root-cause evidence, workaround, permanent fix and regression prevention.
