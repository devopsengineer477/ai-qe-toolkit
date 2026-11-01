---
name: playwright-automation
description: Design, implement and debug browser UI automation using Playwright. Use for end-to-end workflows, page objects, fixtures, locators, traces and CI execution.
---
# Playwright Automation Skill

## Mission
Create stable, accessible, isolated browser tests that verify user-visible behavior.

## Before implementation
1. Inspect repository instructions, Playwright version, language, config and existing patterns.
2. Identify the authorized base URL, test-account strategy and target environment.
3. Review application semantics and existing test IDs/accessibility labels.
4. Do not assume a supplied URL is safe to test.

## Design and locator standards
- Prioritize critical user journeys and high-risk business rules.
- Keep tests independent and avoid ordering dependencies.
- Prefer `getByRole`, `getByLabel`, `getByPlaceholder` and stable test IDs.
- Avoid brittle CSS/XPath selectors where semantic locators exist.
- Use web-first assertions and locator auto-waiting.
- Avoid fixed sleeps; wait for a meaningful state, locator or response.
- Assert observable outcomes, not implementation details.

## Architecture
- Use fixtures for browser/context/page lifecycle and shared setup.
- Use page/component objects when they reduce duplication; avoid unnecessary abstractions.
- Keep environment configuration and secrets outside test code.
- Never commit authenticated storage-state files.
- Capture traces and screenshots on failure; preserve reports as CI artifacts.

## Execution workflow
1. List/discover tests.
2. Run one focused test in an authorized test environment.
3. Run the relevant suite.
4. Inspect traces/screenshots for failures.
5. Confirm cleanup and data isolation.

## Example commands
```powershell
npx playwright test --list
npx playwright test tests/example.spec.ts --project=chromium
npx playwright test --reporter=list
```

## Safety
Do not run destructive workflows, load tests or production tests without explicit authorization and approval.
