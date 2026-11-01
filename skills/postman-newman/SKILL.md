---
name: postman-newman
description: Create, maintain and execute Postman collections with Newman for API validation and CI reporting. Use for collection design, scripts, environments and pipeline integration.
---
# Postman / Newman Skill

## Mission
Produce portable, secure API collections that validate contract and business behavior from local development and CI.

## Before implementation
1. Inspect API contract, existing collections, environment conventions and Newman version.
2. Confirm authorized base URL and test accounts.
3. Identify setup, test data and cleanup requirements.
4. Use placeholders; never request or commit real credentials.

## Collection design
- Organize requests by business capability or API resource.
- Use collection/folder/request scripts deliberately; avoid hidden coupling.
- Use environment variables for base URLs and non-secret settings.
- Keep secret values in approved secret stores or CI credential stores.
- Exclude populated secret-bearing environment files from source control.

## Assertions
Validate status, headers, content type, schema, required fields, business invariants, auth/authz, error responses and relevant pagination/filtering/idempotency behavior. A 2xx response alone does not prove correctness.

## Newman execution
- Make collection and environment selection explicit.
- Use bounded timeouts and appropriate data inputs.
- Configure CLI/JUnit reports and preserve them as CI artifacts.
- Ensure assertion failures produce a non-zero pipeline result.
- Do not use insecure TLS bypasses as a routine workaround.

## Example command (adapt paths/version)
```powershell
newman run collections/customer-api.postman_collection.json `
  -e environments/test.postman_environment.json `
  --reporters cli,junit `
  --reporter-junit-export artifacts/newman-junit.xml
```

## Output
Provide collection structure, assertions, required variables, execution command, reporting and coverage gaps.

## Safety
Use synthetic data and explicitly authorized non-production targets. Ask before destructive or high-volume activity.
