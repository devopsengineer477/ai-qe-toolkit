# GitHub MCP

## What it enables
The official GitHub MCP server can provide access to repositories, issues, pull requests and Actions data. This toolkit template uses the remote endpoint with a limited toolset and read-only mode.

## Starter configuration
The configuration templates use:
- Endpoint: `https://api.githubcopilot.com/mcp/`
- Toolsets: `repos,issues,pull_requests,actions`
- Header: `X-MCP-Readonly: true`

Read-only mode is a server-side restriction that disables write tools. Do not remove it from the starter configuration merely to make a task easier.

## Example prompts
- "Inspect this pull request and summarize changed files, test evidence and risks. Do not approve or merge it."
- "Review the latest GitHub Actions run for this branch. Summarize the failed jobs and likely cause."
- "Find existing tests for the authentication module and suggest missing scenarios. Do not modify files."

## Permissions
Prefer OAuth or a narrowly scoped GitHub App/PAT. Ensure the credential grants access only to the repositories and data required. Keep toolsets minimal; add code-security or other toolsets only when required and approved.
