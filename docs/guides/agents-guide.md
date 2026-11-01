# Agents Guide

Agents are specialist roles, not independent authorities. Use the QE Orchestrator for multi-step work and delegate bounded subtasks to specialists.

Claude Code agent definitions are in `.claude/agents/`. Copilot agent definitions are in `.github/agents/`. Review available tool permissions and adapt them to your installed product versions and organizational policy.

Recommended pattern:
1. Orchestrator owns the plan and final integration.
2. Specialists own clearly assigned analysis or implementation tasks.
3. One agent owns each file set during parallel work.
4. Human approval remains with the user; an agent cannot approve its own risky action.
