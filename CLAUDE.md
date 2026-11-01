# Claude Code — AI QE Toolkit

Read `AGENTS.md` first. It is the shared engineering policy and takes precedence over convenience.

## How to work in this repository
- Start by inspecting the relevant files; do not assume the repository is a runnable automation framework.
- For non-trivial tasks, use plan-first behavior: inspect, propose steps, wait for approval when the task is broad or risky, then implement.
- Use the relevant skill in `.claude/skills/` when the task matches its description.
- Use specialist agents in `.claude/agents/` for focused analysis. Respect their tool restrictions.
- Do not create MCP configuration or request credentials unless the user asks for a specific integration.
- Before running commands, explain any potentially destructive, network-intensive or environment-changing effect.
- Do not run tests against production or external systems without explicit scope and authorization.
- Do not install dependencies or alter global machine configuration without approval.

## Validation and reporting
- Prefer repository-local validation scripts.
- Run only relevant checks; do not imply that every technology stack has been installed.
- Report commands, exit status and meaningful output.
- Separate verified facts from hypotheses.
- Never state that tests passed if they were not executed.

## Skills
Available skills:
- `qe-standards`
- `test-design`
- `api-testing`

Claude Code project skills are stored in `.claude/skills/`.

- For cross-functional QE work, start with the `qe-orchestrator` agent and `qe-orchestration` skill.
- Apply `execution-safety` before running commands that access external systems, mutate data, deploy, or generate load.

- MCP configuration templates are under `integrations/mcp/templates/`; never copy credentials into tracked files.
- Before using MCP, inspect the provider's permissions and follow `integrations/mcp/README-SECURITY.md`.
