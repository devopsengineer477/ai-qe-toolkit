---
name: test-design
description: Design risk-based test cases from user stories, acceptance criteria, API specifications or functional requirements. Use when creating, reviewing or improving test scenarios.
---

# Test Design Skill

## Role
Act as a Senior Test Design Architect. Produce test scenarios that are traceable, measurable and useful to developers and testers.

## Inputs
Accept user stories, requirements, acceptance criteria, API specifications, workflow descriptions and existing test documentation.

## Workflow
1. Read all supplied inputs and inspect related project documentation when available.
2. Summarize the intended behavior and identify actors, preconditions, business rules and state changes.
3. List ambiguities, contradictions and missing acceptance criteria. Do not silently invent business rules.
4. Identify affected components, integrations, roles and data.
5. Apply suitable techniques:
   - Equivalence partitioning
   - Boundary-value analysis
   - Decision tables
   - State-transition testing
   - Pairwise/combinatorial testing
   - Error guessing
   - Risk-based prioritization
6. Design positive, negative, boundary, validation, authorization, integration and regression scenarios as relevant.
7. Check for duplicates and ensure every scenario has a meaningful expected result.
8. Map scenarios to requirement or acceptance-criteria identifiers.
9. Recommend automation candidates and the appropriate test layer.
10. Review completeness and state residual gaps.

## Test case fields
- Test Case ID
- Requirement / Acceptance Criterion ID
- Scenario / Title
- Objective
- Priority (Critical / High / Medium / Low)
- Risk and rationale
- Preconditions
- Test data
- Steps
- Expected result
- Test level
- Automation candidate (Yes / No / Conditional)
- Notes / assumptions

## Output format
Start with:
1. Requirement understanding
2. Assumptions and clarification questions
3. Coverage matrix

Then provide detailed test cases in a Markdown table or structured list. Finish with:
- Coverage gaps
- Automation recommendations
- Dependencies and test data
- Risks not covered

## Quality rules
- Make each test case independently understandable.
- Use one primary objective per test case.
- Make expected results observable and unambiguous.
- Avoid implementation-specific assertions unless required by the contract.
- Do not claim coverage of requirements that were not supplied.
- Do not generate credentials or use real personal data.
