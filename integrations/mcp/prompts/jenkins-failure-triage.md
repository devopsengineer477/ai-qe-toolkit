# Jenkins Failure Triage — MCP Prompt

Use Jenkins MCP with the configured read-only service account. Inspect only the named Jenkins job/build.

1. Read build status and test result summary.
2. Read the relevant log range and find the earliest meaningful failure.
3. Separate infrastructure, configuration, test-code and product failure hypotheses.
4. Correlate with the supplied commit or PR only if the user named it.
5. Return evidence, likely cause, confidence and next diagnostic step.
6. Do not trigger, cancel, replay or modify any job or pipeline.
