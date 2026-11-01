# API Testing Workflow

1. Use `api-testing` and `postman-newman` skills.
2. Inspect API contracts, auth model, existing collections and environment conventions.
3. Generate positive, negative, boundary, authorization and schema scenarios.
4. Use synthetic test data and explicit environment configuration.
5. Review secret handling and ensure logs redact tokens and personal data.
6. Run local/mock checks first. For a real API, confirm the exact authorized host, account and operations.
7. Capture request identifiers and sanitized evidence; never expose credentials.
