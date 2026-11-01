# Postman / Newman example layout

Reference only; no populated secrets are included.

```text
postman/
  collections/customer-api.postman_collection.json
  environments/test.postman_environment.example.json
  data/synthetic-customers.json
```

Inject credentials from an approved secret store at runtime and publish Newman JUnit reports as CI artifacts.
