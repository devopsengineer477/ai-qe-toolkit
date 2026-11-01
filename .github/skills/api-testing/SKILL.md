---
name: api-testing
description: Analyze REST APIs and design or implement API tests using pytest, Postman and Newman. Use for API test strategy, request validation, schema checks, auth testing and automation.
---

# API Testing Skill

## Purpose
Create maintainable API test coverage that verifies contract, business behavior, authorization and error handling.

## First inspect
- API specification or documented contract
- Base URL and environment configuration (use placeholders if unavailable)
- Authentication model and role matrix
- Existing API test framework and dependencies
- Test data setup and cleanup conventions
- Rate limits and authorized test scope

## Design workflow
1. Identify endpoints, methods, parameters, headers and request/response models.
2. Map requirements to endpoint and business-rule coverage.
3. Design positive, negative, boundary and malformed-input scenarios.
4. Cover authentication and authorization separately, including role and object-level access where applicable.
5. Validate status codes, response headers, schema, required fields, data types and business invariants.
6. Consider idempotency, pagination, filtering, sorting, concurrency and rate limits where relevant.
7. Identify integration and persistence checks only when access and architecture justify them.
8. Define deterministic test data, isolation and cleanup.
9. Recommend pytest or Postman/Newman based on the repository and execution needs.
10. Execute only against the explicitly authorized target.

## pytest implementation guidance
- Use a shared client/session fixture where appropriate.
- Keep base URLs and secrets in environment configuration.
- Use parametrization for data-driven cases.
- Keep assertions explicit and diagnostic.
- Validate both contract and business semantics.
- Avoid tests that depend on execution order.
- Mask tokens and sensitive response fields in logs.

## Postman / Newman guidance
- Use collections and environments with variable placeholders.
- Never commit populated secret values.
- Use pre-request scripts only for necessary setup and keep them readable.
- Add assertions for status, schema and business behavior.
- Make environment selection explicit in execution commands.
- Preserve Newman reports as CI artifacts.
- Do not use `--insecure` as a routine workaround for TLS errors.

## Security and safety
- Do not test endpoints outside the user's explicit authorization.
- Do not enumerate real user accounts or access other users' data.
- Use test accounts and synthetic data.
- Do not perform destructive, fuzzing or high-volume tests without explicit approval and safe scope.
- Treat tokens, cookies and personal data as secrets.

## Output
Provide:
1. API inventory and assumptions
2. Requirement-to-endpoint coverage
3. Test scenario matrix
4. Recommended framework and rationale
5. Example tests or collection structure
6. Execution commands using placeholders
7. Reporting and CI integration
8. Security, data and environment risks
