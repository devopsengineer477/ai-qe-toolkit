# Orchestrated QE Task

Use this pattern for work spanning multiple QE disciplines.

## Prompt
"Use the QE Orchestrator. Read the project instructions and inspect existing implementation and tests. Analyze the supplied requirement, create a risk-based plan, delegate only necessary specialist tasks, and produce traceable test cases. Do not access external systems or run state-changing commands. Present any proposed execution command and wait for approval."

## Definition of done
- Requirement and scope are clear.
- Risks and assumptions are recorded.
- Requirements map to test cases or an explicit rationale.
- Generated automation follows project conventions.
- Changes receive review.
- Commands and observed results are accurately reported.
- External/state-changing actions have explicit approval or are marked blocked.
- Evidence is sanitized and linked from the report.
