# Claude Code Guide

1. Start Claude Code from the toolkit or target project root.
2. Ask it to read `AGENTS.md` and `CLAUDE.md`.
3. For broad work, invoke the `qe-orchestrator` agent.
4. Ask it to apply relevant skills from `.claude/skills/`.
5. Review proposed edits and diffs before accepting them.
6. Require explicit approval before external, state-changing, destructive, deployment or load-intensive operations.

Example: "Use qe-orchestrator to plan API regression coverage for this requirement. Inspect only; do not edit or execute tests."
