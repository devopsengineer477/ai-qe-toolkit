# First Workflow: Requirement to Test Design

1. Open the target application repository in your AI coding tool.
2. Ask the tool to read `AGENTS.md` and the applicable project instructions.
3. Provide a sanitized requirement or user story with acceptance criteria.
4. Ask the QE Orchestrator to inspect the existing tests and propose a plan.
5. Ask the Test Architect to create risk-based coverage and traceability.
6. Ask the relevant automation specialist to draft tests consistent with the existing framework.
7. Review the diff and run repository-local validation.
8. Approve external or state-changing execution separately, with exact target and command.
9. Request a report that distinguishes generated tests, executed tests, passed/failed checks and checks not run.

## Example prompt
"Use the QE Orchestrator. Analyze `examples/sample-api-requirement.md`. Inspect existing test conventions first. Produce a plan, risk-based test cases and a requirement-to-test matrix. Do not call any external service or modify files."
