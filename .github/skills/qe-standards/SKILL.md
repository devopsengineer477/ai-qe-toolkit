---
name: qe-standards
description: Apply the toolkit's Quality Engineering principles, risk-based testing, traceability, automation design and definition of done. Use when planning or reviewing QE work.
---

# QE Standards Skill

## Purpose
Apply consistent, maintainable Quality Engineering practices across projects and technologies.

## Inputs
- Project/repository context
- Requirements, user stories or change description
- Existing test strategy, standards and automation conventions
- Relevant constraints and risks

## Workflow
1. Inspect the repository and existing QE documentation.
2. Identify the business objective, affected components and critical user journeys.
3. Identify quality attributes: functional correctness, reliability, security, performance, accessibility and compatibility as relevant.
4. Assess risk using likelihood, impact and exposure. State the rationale; do not invent numeric scoring rules.
5. Map requirements and acceptance criteria to verification activities.
6. Recommend the appropriate test levels: unit, component, API, UI, integration, contract, performance and security.
7. Identify automation candidates based on repeatability, stability, value and maintenance cost.
8. Identify test data, environment, observability and dependency needs.
9. Define exit criteria and evidence required for release confidence.
10. Review the result against `AGENTS.md`.

## Principles
- Shift testing left, but retain appropriate end-to-end and production-monitoring controls.
- Prefer the fastest test level that provides sufficient confidence.
- Keep tests deterministic, independent and diagnosable.
- Do not automate unstable or poorly understood behavior blindly.
- Do not equate test count or pass rate with product quality.
- Do not hide failures through retries or relaxed assertions.
- Distinguish a missing test from a known product defect.

## Output
Produce:
1. Context and scope
2. Assumptions and open questions
3. Risk assessment
4. Test strategy and test-level mapping
5. Requirement traceability matrix
6. Automation recommendations with rationale
7. Test data and environment needs
8. Exit criteria and residual risks

## Safety
Active testing must remain within explicitly authorized scope. Ask before destructive, load-intensive or production activity.
