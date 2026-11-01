# MCP Integration Pack

This directory contains **configuration templates and operating policy**, not live credentials or active connections. Copy only the configuration format for the client you use, review every server, authenticate through its supported flow, and approve the project-scoped servers yourself.

## Providers in this release

| Provider | MCP endpoint / transport | Default posture |
|---|---|---|
| Atlassian Jira + Confluence | Remote Streamable HTTP: `https://mcp.atlassian.com/v2/mcp` | Use an identity with browse/read permissions only |
| GitHub | Remote HTTP: `https://api.githubcopilot.com/mcp/` | Read-only header and limited toolsets |
| Jenkins | Jenkins MCP Server plugin: `/mcp-server/mcp` | Dedicated read-only account; no build/configure permissions |

## Choose a configuration

- Claude Code: `templates/claude-code/.mcp.json` -> copy to project root as `.mcp.json`.
- VS Code: `templates/vscode/mcp.json` -> copy to `.vscode/mcp.json`.
- Portable Copilot configuration: `templates/copilot-portable/.mcp.json` -> copy to workspace root as `.mcp.json` only when using the portable Copilot format. Do not use it at the same time as the Claude project `.mcp.json` unless you intentionally maintain one compatible shared file.

VS Code's `.vscode/mcp.json` uses a top-level `servers` object. The portable Copilot and Claude Code project formats use `mcpServers`; these are not interchangeable formats in every client. Review the client guide before copying.

## Jenkins prerequisites

Install and configure the official Jenkins MCP Server plugin on a supported Jenkins controller. The current plugin documentation lists its Streamable HTTP endpoint as `/mcp-server/mcp`. Verify the minimum Jenkins core version and plugin compatibility against your controller before installing.

Create a dedicated service account and API token. Grant only `Overall/Read` and `Job/Read` for the jobs it must inspect. Do not grant `Job/Build`, `Job/Configure`, `Overall/Administer`, or credentials-management permissions to the read-only integration identity. The plugin exposes write-capable tools; Jenkins permissions are therefore an essential control.

Set the environment variables in the client process before starting it:
- `JENKINS_MCP_URL` — exact HTTPS endpoint for your controller.
- `JENKINS_MCP_BASIC_AUTH` — Base64 encoding of `username:API_TOKEN` for HTTP Basic authentication.

Base64 is encoding, not encryption. Protect this value like the original token. Prefer a managed secret store or a short-lived process environment. Never commit it to `.mcp.json`, `.vscode/mcp.json`, `.env`, or source control.

## Authentication

- Atlassian: complete the OAuth flow offered by your MCP client; access is bounded by the signed-in user's Jira and Confluence permissions.
- GitHub: complete the remote server's supported authentication flow. Keep the `X-MCP-Readonly` header enabled. Do not remove it to enable write operations in this starter template.
- Jenkins: use a dedicated API token with read-only Jenkins permissions.

## Enable gradually

1. Start with one server, preferably Atlassian or GitHub read-only.
2. Review the server publisher, endpoint, available tools, requested OAuth scopes and data handling.
3. Authenticate interactively.
4. Verify with a read-only query.
5. Inspect tool names and permissions before allowing the AI to use them.
6. Keep write tools disabled or blocked by account permissions until a separate change-control process approves them.

## Important limitations

- Templates do not install plugins, create credentials, configure network access or connect to your organization.
- Jira and Confluence are exposed through the same Atlassian MCP server.
- The Jenkins plugin's exposed tools vary by plugin version. Inspect the tools advertised by your installed version.
- MCP access does not replace normal application authorization, network controls, audit logging or human approval.


## Official references
See `docs/integrations/references.md` for vendor-maintained setup and security documentation.
