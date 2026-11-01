---
name: pytest-automation
description: Design, implement, debug and improve Python test automation using pytest. Use for fixtures, parametrization, API tests, test data, reporting and CI execution.
---
# Pytest Automation Skill

## Mission
Build reliable, maintainable and diagnosable Python automation that follows the target repository's conventions.

## Before implementation
1. Inspect AGENTS.md, README, Python version, dependency manager and existing tests.
2. Identify the test target, authorized environment, API contract and test-data strategy.
3. Inspect existing fixtures, clients, helpers, markers and reporting configuration.
4. Ask before installing packages, changing dependency versions or calling an unfamiliar target.

## Design and implementation
- Separate test intent, API/client helpers, fixtures, configuration and test data.
- Use fixtures for lifecycle management and explicit teardown.
- Use parametrization for meaningful input partitions.
- Keep tests independent; avoid execution-order dependencies and shared mutable state.
- Use descriptive names: `test_<behavior>_<condition>`.
- Prefer type hints in reusable helpers and public interfaces.
- Set explicit network timeouts; validate status, headers, schema and business invariants.
- Avoid broad exception swallowing and arbitrary retries.
- Keep environment values outside source code; mask tokens, cookies and personal data in logs.

## Execution workflow
1. Run collection or a narrow test selection first.
2. Run targeted tests, then relevant lint/type checks already used by the project.
3. Run broader suites only when safe and practical.
4. Preserve JUnit, coverage and diagnostic artifacts where configured.
5. Classify failures as product, test, data, environment, dependency or infrastructure.

## Example commands (adapt to the project)
```powershell
python -m pytest --collect-only -q
python -m pytest tests/api/test_customers.py -q
python -m pytest -m "not slow" --junitxml=artifacts/junit.xml
```

## Output
Report changed files, design choices, commands actually executed, results, skipped checks, risks and gaps.

## Safety
Run only against explicitly authorized environments. Do not perform destructive or high-volume tests without approval.
