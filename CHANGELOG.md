# Changelog

## [0.3.0] - Milestone 3
### Added
- QE Orchestrator agent definitions for Claude Code and GitHub Copilot.
- `qe-orchestration` and `execution-safety` skills, synchronized to both native skill locations.
- Human-in-the-loop execution classification and approval request template.
- Architecture, orchestration, execution-flow, setup, skills, agents, tool-specific and workflow documentation.
- QE task plan and orchestrated task playbook.

### Changed
- Expanded shared agent instructions with orchestration, traceability and approval requirements.
- Expanded Claude Code and Copilot guidance.
- Replaced the short starter README with complete architecture, setup and usage documentation.

### Safety
- External, state-changing, destructive, deployment and load-intensive operations require explicit approval.
- The toolkit remains a guidance/starter repository; no live external integrations are configured.

## [0.4.0] - Milestone 4
### Added
- MCP integration architecture and provider capability contract.
- Claude Code, VS Code and portable Copilot configuration templates.
- Atlassian Jira/Confluence, GitHub and Jenkins integration guides.
- MCP security checklist, approval policy and QE workflow prompts.
- Setup, verification and rollback instructions for MCP clients.

### Security
- GitHub starter configuration uses read-only mode and a limited toolset.
- Jenkins guidance requires a dedicated read-only service account.
- Atlassian guidance recommends browse-only permissions for initial rollout.
- No credentials, live server connections or external actions are included in the archive.
