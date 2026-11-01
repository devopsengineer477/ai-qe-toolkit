# Execution Flow and Approval Gates

```mermaid
flowchart TD
    A[Request] --> B[Inspect repository and scope]
    B --> C[Plan and map requirements]
    C --> D[Generate or update tests]
    D --> E[Review standards and risks]
    E --> F{Execution class?}
    F -->|A: read-only| G[Proceed]
    F -->|B: local safe| H[State command and run locally]
    F -->|C: external or state-changing| I[Request explicit approval]
    F -->|D: high impact| J[Require specific authorization and safe plan]
    I --> K{Approved?}
    J --> K
    K -->|No| L[Blocked: approval required]
    K -->|Yes| M[Run exact approved scope]
    G --> N[Capture observed results]
    H --> N
    M --> N
    L --> O[Report blocker and safe alternatives]
    N --> P[Traceability and QE report]
```

## Execution classes
- **A:** read-only local inspection and repository validators.
- **B:** local tests/simulations without external access or shared-state mutation.
- **C:** API mutations, shared test environments, deployments, DAST, data changes.
- **D:** production, destructive, broad scanning or high-load activity.

See `execution-safety` skill for the complete approval checklist and safe defaults.
