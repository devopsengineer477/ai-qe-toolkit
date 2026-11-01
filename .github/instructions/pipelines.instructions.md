---
name: CI pipeline conventions
description: Apply when editing Jenkinsfiles, GitHub Actions workflows or pipeline YAML.
applyTo: "**/{Jenkinsfile,*.yml,*.yaml}"
---
# CI pipeline conventions
- Use least-privilege identities and secrets stores; never print secrets.
- Prefer explicit inputs, pinned or controlled action/plugin versions and clear timeouts.
- Preserve test reports and diagnostic artifacts on failure where practical.
- Make failure conditions explicit; do not swallow non-zero exit codes.
- Separate build, test, security scan and deployment stages.
- Require approval and environment protection for sensitive deployments.
