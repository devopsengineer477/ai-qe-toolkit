# Agent Orchestration

## Roles
| Role | Responsibility | Expected artifact |
|---|---|---|
| QE Orchestrator | Intake, plan, delegate, integrate, report | Work plan and final QE summary |
| Test Architect | Risk, coverage, strategy, traceability | Strategy and coverage matrix |
| API Test Designer | API scenarios and contracts | API test cases/spec |
| Automation Developer | Framework-aligned automation | Test code and supporting fixtures |
| CI Pipeline Reviewer | Pipeline quality, secrets, permissions, artifacts | Review findings and safe recommendations |

## Interaction model
1. Orchestrator inspects context and scopes the task.
2. Specialists work on bounded outputs with explicit assumptions.
3. Orchestrator checks consistency and merges the outputs.
4. Review findings are addressed or recorded as accepted risks.
5. Human approval is obtained for actions beyond read-only/local-safe work.
6. Final report links requirements, tests, execution results and evidence.

## Avoiding agent sprawl
Delegate only when a distinct specialist capability materially improves the result. Small tasks should be completed directly. Avoid multiple agents editing the same files concurrently. Assign file ownership in the plan for parallel work.

## Failure handling
If a specialist output is incomplete or contradictory, ask for clarification or resolve with documented rationale. If a required tool, credential or permission is unavailable, stop at a useful artifact and state the blocker; do not simulate a successful integration.
