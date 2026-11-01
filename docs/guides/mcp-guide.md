# MCP Integration Guide

MCP integrations are intentionally not preconfigured in this release. Add a server only when a specific workflow requires it and the organization approves the provider, scopes, data handling and authentication model.

Before enabling an MCP server:
- Confirm vendor/source and trustworthiness.
- Review requested tools and permissions.
- Prefer read-only scopes initially.
- Use approved OAuth or secret-management flows.
- Avoid storing tokens in repository files.
- Test against non-production data.
- Document owner, purpose, permissions, setup and revocation steps.

Potential future integrations include Jira, Confluence, GitHub and Jenkins. This release does not claim that any of these are connected.
