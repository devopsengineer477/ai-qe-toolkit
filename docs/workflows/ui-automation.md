# UI Automation Workflow

1. Use `playwright-automation` skill.
2. Inspect app structure, existing fixtures, selectors and test conventions.
3. Prefer role, label and stable test-id locators; use web-first assertions.
4. Isolate test data and make cleanup explicit.
5. Avoid fixed sleeps and blanket retries.
6. Run against local or approved test environments only.
7. Attach traces/screenshots on failure while redacting sensitive content.
