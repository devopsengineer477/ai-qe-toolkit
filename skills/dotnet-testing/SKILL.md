---
name: dotnet-testing
description: Design, implement and troubleshoot C#/.NET automated tests using the repository's existing framework such as MSTest, xUnit or NUnit. Use for test projects, VSTest, Coverlet and CI integration.
---
# C# / .NET Testing Skill

## Mission
Create maintainable .NET tests that fit the existing solution and provide reliable diagnostics and coverage evidence.

## Before implementation
1. Inspect solution/project files, target framework, SDK, nullable settings and package versions.
2. Identify existing test framework and conventions.
3. Inspect build/test commands and CI configuration.
4. Do not migrate frameworks, upgrade packages or change target frameworks without rationale and approval.

## Test design
- Use clear Arrange / Act / Assert structure and descriptive names.
- Keep tests focused, deterministic and isolated.
- Use data-driven tests for meaningful input variants.
- Avoid static mutable state and test-order dependencies.
- Use async test methods for asynchronous behavior; avoid `.Result` and `.Wait()`.
- Dispose streams, clients and other disposable resources correctly.
- Assert observable behavior and actionable error details.

## Build and execution
Inspect the repository first. Common commands:
```powershell
dotnet --info
dotnet restore
dotnet build .\YourSolution.sln --no-restore
dotnet test .\YourSolution.sln --logger "trx;LogFileName=test-results.trx"
```

## Coverage
- Use the project's approved Coverlet integration and output format.
- Distinguish line, branch and method coverage where available.
- Do not optimize only for a percentage; identify untested risk and assertion quality.
- Validate generated Cobertura/OpenCover files before publishing.
- Preserve coverage and TRX artifacts in CI.

## Troubleshooting
Classify failures as compile/build, test assertion, test discovery, dependency, environment, data or infrastructure. Use logs and exit codes as evidence.

## Safety
Never use production data or credentials. Ask before modifying shared databases or external environments.
