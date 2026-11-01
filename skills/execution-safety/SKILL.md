---
name: execution-safety
description: Apply scope, authorization and human approval gates before running tests, security checks, load tests or state-changing commands.
---

# Execution Safety

## Classify the proposed action
- **Class A — read-only local:** inspect files, parse configuration, generate test plans, run repository validators. May proceed when within the user's requested task.
- **Class B — local execution:** run unit tests or local simulations that do not access external systems or mutate shared state. State the command and expected effect.
- **Class C — external or state-changing:** call APIs, create/update records, access shared test environments, deploy, delete, migrate, run DAST, or execute scripts with side effects. Require explicit approval of target, action and scope.
- **Class D — high impact:** production access, destructive data operations, broad scans, stress/load tests, credential changes or irreversible actions. Do not proceed without explicit, specific authorization and a documented safe plan; recommend a non-production alternative.

## Approval checklist
Before Class C or D:
1. Identify the system owner and evidence of authorization.
2. Confirm exact host, tenant, environment, account or namespace.
3. Confirm permitted test types, endpoints, accounts and data.
4. Define rate, duration, concurrency and stop conditions where applicable.
5. Confirm rollback/cleanup and monitoring contact.
6. Present the exact command/action and expected side effects.
7. Wait for explicit human approval.
8. Stop if target, command, scope or conditions change.

## Safe defaults
- Use mocks, local containers, test doubles and synthetic data first.
- Use allowlists; do not discover unrelated hosts or endpoints.
- Never place credentials in command history, source code or reports.
- Avoid disabling TLS verification, authorization checks or assertions to make tests pass.
- Do not retry a potentially non-idempotent action automatically.
- Do not run k6 load profiles or active DAST against shared/production systems without the required approval.
- Preserve logs and evidence while redacting tokens, personal data and secrets.

## Reporting
Record action classification, approved scope, exact command, start/end, result, evidence and cleanup status. If approval is missing, report **BLOCKED — approval required**, not a test failure.
