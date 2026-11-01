# Python / pytest Standards

- Follow the repository's Python version and dependency manager.
- Use `pytest` fixtures for shared setup and teardown.
- Prefer parametrization for related input variants.
- Keep tests independent and deterministic.
- Use descriptive test names and meaningful assertions.
- Use timeouts for network calls and avoid unbounded waits.
- Load configuration from environment variables or approved config files.
- Never commit secrets; mask sensitive values in logs.
- Run targeted tests first, then the relevant suite.
