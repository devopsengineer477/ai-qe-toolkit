---
name: Playwright conventions
description: Apply when creating or modifying Playwright tests.
applyTo: "**/*.{spec,test}.{ts,tsx,js,jsx}"
---
# Playwright conventions
- Prefer role, label and test-id locators; avoid fragile CSS/XPath selectors.
- Use web-first assertions and locator auto-waiting.
- Avoid fixed sleeps; wait for a meaningful state or response.
- Keep tests isolated and independent.
- Use fixtures for reusable setup and teardown.
- Capture traces, screenshots and useful diagnostics on failure.
- Never point tests at production unless explicitly authorized.
