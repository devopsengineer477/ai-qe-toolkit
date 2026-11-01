# pytest API example layout

Reference only; not a runnable suite until project dependencies and an authorized test endpoint are configured.

```text
tests/
  conftest.py
  api/test_customer_profile.py
src/
  clients/customer_api.py
  config/settings.py
```

Keep base URLs and credentials in approved environment configuration, use synthetic test accounts, and separate API client helpers from test intent.
