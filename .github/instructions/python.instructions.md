---
name: Python and pytest conventions
description: Apply when creating or modifying Python files and pytest tests.
applyTo: "**/*.py"
---
# Python and pytest conventions
- Follow the target project's Python version and dependency manager.
- Prefer type hints for public functions and non-trivial data structures.
- Name tests `test_<behavior>_<condition>`.
- Use fixtures for reusable setup and teardown; avoid hidden global state.
- Parametrize equivalent scenarios instead of duplicating test functions.
- Assert observable behavior and useful error details.
- Do not hardcode credentials, URLs for private environments or customer data.
- Run the project's formatter, linter and targeted pytest command when available.
