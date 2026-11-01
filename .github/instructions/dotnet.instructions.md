---
name: C# and .NET conventions
description: Apply when creating or modifying C# and .NET files.
applyTo: "**/*.cs"
---
# C# and .NET conventions
- Follow the solution's target framework, nullable settings and existing style.
- Prefer clear names, small methods, explicit dependencies and deterministic tests.
- Use async APIs consistently; do not block on async work with `.Result` or `.Wait()`.
- Keep test arrange/act/assert sections clear.
- Dispose resources correctly and avoid shared mutable test state.
- Do not change package versions or target frameworks without explaining the impact.
