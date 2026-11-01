# MCP Client Setup

## Claude Code

1. Copy `integrations/mcp/templates/claude-code/.mcp.json` to the project root.
2. For Jenkins, set `JENKINS_MCP_URL` and `JENKINS_MCP_BASIC_AUTH` in the environment used to start Claude Code. Do not put token values in the JSON.
3. Start Claude Code from the trusted project directory.
4. Review the project MCP server approval prompt before accepting any server.
5. Run `/mcp` to inspect status and available tools.
6. Run `claude mcp list` and `claude mcp get <server-name>` to inspect configuration/connection status.
7. Verify with one read-only query per provider.

Claude Code project-scoped `.mcp.json` entries require user approval in an interactive session. Keep server definitions in the project config but credentials outside version control.

## VS Code / GitHub Copilot

1. Copy `integrations/mcp/templates/vscode/mcp.json` to `.vscode/mcp.json`.
2. Set `JENKINS_MCP_URL` and `JENKINS_MCP_BASIC_AUTH` in the VS Code process environment before launching VS Code.
3. Open Command Palette and run **MCP: List Servers**.
4. Start each server and review its trust/authentication prompts.
5. Inspect output and verify one read-only query per provider.

VS Code's config uses the top-level `servers` object. Do not paste a Claude `.mcp.json` directly into `.vscode/mcp.json`.

## Portable Copilot MCP configuration

For Copilot harnesses that use the portable format, see `integrations/mcp/templates/copilot-portable/.mcp.json`. Its top-level key is `mcpServers`. Follow the installed Copilot client's current guidance for authentication and server discovery.

## Rollback
Disable the server from the client's MCP management UI or remove the server entry from the configuration. Revoke its OAuth grant or API token in the provider's security settings when access should end.
