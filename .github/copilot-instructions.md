# GitHub Copilot — AI QE Toolkit

Read and follow `AGENTS.md` for shared engineering rules. This file adds Copilot-specific workflow guidance.

## Repository context
This is a reusable Quality Engineering toolkit, not a single application or preconfigured test framework. Inspect the target project before choosing tools or generating code.

## Preferred behavior
- For multi-file changes, explain the plan before editing.
- Use the relevant skill in `.github/skills/` for repeatable workflows.
- Use custom agents in `.github/agents/` for focused roles.
- Prefer small, reviewable changes and existing project conventions.
- Ask before installing packages, changing global settings, accessing external systems or running destructive/load tests.
- Do not invent requirements, endpoints, credentials, test outcomes or environment configuration.
- Keep secrets out of source control and logs.

## Validation
Run relevant repository checks where feasible. In the final response, list commands actually executed and distinguish passed, failed, skipped and not run. Never claim success without execution evidence.
