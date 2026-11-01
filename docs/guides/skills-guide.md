# Skills Guide

Skills are reusable task procedures. Canonical sources live in `skills/<name>/SKILL.md`; synchronized copies are provided for Claude Code and Copilot.

## Available skills
- `qe-standards`, `test-design`, `api-testing`
- `pytest-automation`, `playwright-automation`, `postman-newman`
- `dotnet-testing`, `ci-cd-automation`, `k6-performance`
- `qe-orchestration`, `execution-safety`

## Use and maintain
Ask the AI tool to use the skill by name. Keep each skill focused on a repeatable workflow, with trigger conditions, inputs, steps, expected outputs and safety rules. Update the canonical copy and run `scripts/Sync-Skills.ps1`; then run `scripts/validate_skills.py`.
