---
name: ci-cd-automation
description: Design, implement, review and troubleshoot Jenkins pipelines and GitHub Actions workflows for build, test, scan, artifact and deployment automation.
---
# CI/CD Automation Skill

## Mission
Build secure, observable and maintainable CI/CD workflows for Quality Engineering.

## Before changes
1. Inspect Jenkinsfile/workflows, shared libraries, runners/agents and credential patterns.
2. Identify triggers, branch strategy, environment boundaries and artifact retention.
3. Establish agent OS (Windows/Linux/container), tool versions and approvals.
4. Do not assume cloud account, repository or production permissions.

## Pipeline design
Consider explicit stages: checkout, restore, build, unit/component tests, API/UI tests, security scans, coverage/quality gates, artifact publishing and approved deployment.

## Reliability
- Set stage/job timeouts and concurrency controls.
- Fail on non-zero command exit codes.
- Preserve test reports and diagnostics on failure where practical.
- Make environment and version inputs explicit.
- Use approved shared libraries/actions; clean up safely.
- Never silently continue after failed quality gates.

## Security
- Apply least privilege to agents, service accounts and tokens.
- Use Jenkins Credentials or GitHub Actions secrets/environments.
- Never print secrets or enable shell tracing around secret-bearing commands.
- Pin third-party actions to approved immutable references where policy requires.
- Review token permissions and deployment protections.

## Windows agent considerations
Verify PowerShell vs cmd syntax, path separators, quoting, installed SDK/tool versions, workspace cleanup and process termination. Do not assume Linux commands work on Windows.

## Troubleshooting
Classify checkout, agent provisioning, dependency restore, build, test, scan, artifact, permission, network, configuration and deployment failures. Cite log evidence; distinguish facts from hypotheses.

## Safety
Do not deploy, alter shared infrastructure, rotate credentials or run destructive jobs without explicit approval. Validate changes in a non-production branch/environment first.
