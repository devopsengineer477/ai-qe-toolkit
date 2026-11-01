# Release Readiness Model

The toolkit provides configurable gates, not an automatic release decision.

## Example gates
- Minimum pass rate
- Maximum failed tests
- Minimum requirement coverage
- Optional performance SLO thresholds in a future adapter
- Required security scan completion
- No unresolved critical/high defects

The sample `config/release-gates.example.json` is illustrative. Teams must agree thresholds by product risk and release type.

## Decision statuses
- **PASS:** all configured gates have evidence and pass.
- **FAIL:** at least one evaluated gate fails.
- **NOT EVALUATED:** required data is missing.
- **NOT CONFIGURED:** no threshold was supplied.

Do not convert NOT EVALUATED into PASS. A release manager remains accountable for the release decision and may consider risks outside this dataset.
