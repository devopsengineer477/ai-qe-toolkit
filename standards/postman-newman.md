# Postman / Newman Standards

- Keep collections organized by business capability or API domain.
- Use environment variables for base URLs and non-secret configuration.
- Keep secrets in approved secret stores or CI credential stores.
- Assert contract and business behavior, not only status codes.
- Make environment selection explicit.
- Preserve machine-readable and human-readable reports in CI.
- Avoid logging authorization headers, cookies and sensitive payload fields.
