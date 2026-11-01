# AI QE Toolkit

A reusable, Windows-friendly foundation for AI-assisted Quality Engineering with Claude Code and VS Code + GitHub Copilot.

**Milestone 1 scope:** shared QE instructions, three core skills, specialist agents, technology standards, templates, and local validation scripts.

## Supported technology areas

- Python / pytest
- Playwright
- Postman / Newman
- C# / .NET
- Jenkins / GitHub Actions
- k6 performance testing

## Repository principles

1. Keep shared engineering policy in `AGENTS.md`.
2. Keep Claude-specific workflow guidance in `CLAUDE.md`.
3. Keep Copilot-specific guidance in `.github/copilot-instructions.md`.
4. Skills are task playbooks, not substitutes for project instructions.
5. Agents are focused roles; restrict tools and permissions where possible.
6. Never claim a test passed unless it was actually executed and its result observed.
7. Use only explicitly authorized environments for active testing.

## Quick start (Windows PowerShell)

```powershell
# 1. Extract this archive, then open the extracted folder in VS Code.
cd C:\Projects\ai-qe-toolkit

# 2. Initialize Git.
git init
git add .
git commit -m "chore: initialize AI QE Toolkit"

# 3. Validate the repository content.
.\scripts\Validate-Toolkit.ps1

# 4. Open Claude Code from the repository root.
claude

# 5. In Claude Code, inspect available skills and run a safe test-design task.
```

## Skill locations

The same three skills are included in both native locations so each tool can discover them without relying on custom path settings:

- Claude Code: `.claude/skills/<skill-name>/SKILL.md`
- VS Code / GitHub Copilot: `.github/skills/<skill-name>/SKILL.md`

`skills/` contains the canonical copies. Run `python scripts/validate_skills.py` to check that native copies match the canonical source.

## Suggested first prompts

### Claude Code

```text
Read AGENTS.md and CLAUDE.md. Inspect this repository without changing files.
Explain the toolkit structure, list the three available skills and agents,
and identify any configuration or validation gaps.
```

### Copilot Chat (Agent mode)

```text
Read AGENTS.md and .github/copilot-instructions.md.
Use the test-design skill to analyze examples/sample-api-requirement.md.
Do not modify files. Produce test cases and a traceability matrix.
```

## Important limitations

- This is a reusable starter kit, not a ready-made test framework or a live Jira/Jenkins integration.
- MCP servers are intentionally not preconfigured. Add only approved servers and credentials for your organization.
- No credentials, API keys, production endpoints, or real customer data belong in this repository.
- Claude Code and Copilot features evolve. Verify command availability in your installed versions.

## Roadmap

- **Milestone 1:** foundation and core skills (this release).
- **Milestone 2:** technology-specific skills for pytest, Playwright, Newman, .NET, CI/CD and k6 (included in v0.2.0).
- **Milestone 3:** specialist agents, controlled execution workflows and review gates.
- **Milestone 4:** approved MCP integrations for Jira, Confluence, GitHub and Jenkins.
- **Milestone 5:** reporting, metrics, reusable demos and team adoption.
