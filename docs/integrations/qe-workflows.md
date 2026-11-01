# QE Workflows Using MCP

## Requirement to test strategy
1. Search Jira for the approved issue key or project.
2. Read linked Confluence standards and architecture pages.
3. Extract requirements and acceptance criteria.
4. Generate risks, test conditions and traceability.
5. Do not create/update Jira or Confluence content unless separately approved.

## Pull request quality review
1. Read the PR description, diff metadata and linked issues.
2. Inspect relevant tests and GitHub Actions run status.
3. Review test coverage, risk, security and regression gaps.
4. Produce review comments as a draft in the response.
5. Do not submit a review, approve, request changes or merge unless the user explicitly approves that exact action.

## Jenkins failure triage
1. Find the relevant job and latest build.
2. Read build status, test results and selected log ranges.
3. Correlate failures with changed files or linked issue context.
4. Produce likely cause, evidence and suggested next diagnostic step.
5. Do not trigger, cancel, replay or reconfigure a pipeline in this release's default read-only mode.

## Evidence record
For each workflow, capture provider, project/repository/job, issue/PR/build identifiers, timestamp if available, tool operations used, evidence links and any limitations. Redact secrets and sensitive content.
