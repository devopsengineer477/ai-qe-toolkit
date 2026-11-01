# MCP Security Checklist

## Before connecting
- [ ] Confirm the server is official or approved by your organization.
- [ ] Confirm the endpoint hostname and TLS certificate.
- [ ] Review available tools, prompts, resources and requested OAuth scopes.
- [ ] Confirm which data may leave the workstation/network.
- [ ] Use a dedicated identity with minimum permissions.
- [ ] Confirm audit logging and token revocation procedure.
- [ ] Ensure no secrets are stored in tracked config.

## While operating
- [ ] Treat issue descriptions, wiki pages, PR comments, commit messages and build logs as untrusted data.
- [ ] Do not follow instructions found in retrieved content that attempt to change policy, reveal secrets or expand scope.
- [ ] Prefer read-only operations.
- [ ] Require approval before ticket writes, comments, PR writes, build triggers, cancellations, pipeline edits or deployments.
- [ ] Never provide production credentials to a general-purpose AI tool.
- [ ] Redact tokens, personal data and internal secrets from generated reports.

## After use
- [ ] Review tool-call audit records where available.
- [ ] Revoke unused credentials and remove unused server entries.
- [ ] Reassess scopes when workflows change.
