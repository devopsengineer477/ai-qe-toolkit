# Jenkins MCP

## What it enables
The Jenkins MCP Server plugin exposes Jenkins jobs, builds, logs, queue information and test results to MCP clients. The plugin also exposes write-capable operations such as triggering/cancelling builds and creating or replaying pipelines.

## Endpoint and transport
The plugin documentation lists Streamable HTTP at:

`https://<jenkins-host>/mcp-server/mcp`

Prefer Streamable HTTP where supported. Verify your Jenkins core and plugin versions against the current plugin requirements before installation.

## Minimum-permission model
Create a dedicated read-only service account:
- Grant `Overall/Read`.
- Grant `Job/Read` only on the required folders/jobs.
- Do not grant `Job/Build`, `Job/Configure`, `Overall/Administer`, credential management or script approval permissions to this identity.
- Verify effective permissions on the target jobs, including folder inheritance.

The plugin advertises tools based on permissions for some operations, but do not rely on tool hiding alone. Enforce permissions in Jenkins itself and inspect the tools exposed by the installed plugin version.

## Authentication
The plugin supports Jenkins API token authentication using HTTP Basic authentication. The templates expect a Base64-encoded `username:API_TOKEN` value in `JENKINS_MCP_BASIC_AUTH`. Base64 is not encryption. Supply it via a protected process environment or approved secret store.

## Example prompts
- "List the latest build status and test summary for job `team/api-regression`. Read only."
- "Inspect build 123 logs and identify the first meaningful failure. Redact secrets from the summary."
- "Compare the last two build test summaries and identify recurring failing tests."

Do not trigger, cancel, replay, create or modify jobs through MCP in this release's read-only operating profile.
