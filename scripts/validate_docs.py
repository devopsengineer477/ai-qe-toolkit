from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
def main():
    required = [
        "docs/architecture/overview.md",
        "docs/architecture/agent-orchestration.md",
        "docs/architecture/execution-flow.md",
        "docs/getting-started/windows-setup.md",
        "docs/getting-started/first-workflow.md",
        "docs/guides/skills-guide.md",
        "docs/guides/agents-guide.md",
        "docs/guides/claude-code-guide.md",
        "docs/guides/copilot-guide.md",
        "docs/guides/mcp-guide.md",
        "docs/workflows/api-testing.md",
        "docs/workflows/ui-automation.md",
        "docs/workflows/pipeline-debugging.md",
        "docs/workflows/performance-testing.md",
        "docs/workflows/orchestrated-qe-task.md",
        "CHANGELOG.md",
        "docs/integrations/mcp-architecture.md",
        "docs/integrations/atlassian-jira-confluence.md",
        "docs/integrations/github.md",
        "docs/integrations/jenkins.md",
        "docs/integrations/client-setup.md",
        "docs/integrations/qe-workflows.md",
        "docs/integrations/references.md",
        "integrations/mcp/README.md",
        "integrations/mcp/README-SECURITY.md",
    ]
    missing = [p for p in required if not (ROOT / p).is_file()]
    readme = README.read_text(encoding="utf-8")
    for heading in ["Proposed architecture", "Quick start", "How to use it", "Skills catalogue", "Agent catalogue", "Safety and data handling", "Milestone 4 — MCP integrations"]:
        if heading not in readme:
            missing.append(f"README missing section: {heading}")
    if missing:
        print("Documentation validation FAILED:\n" + "\n".join(" - " + x for x in missing))
        return 1
    print(f"Documentation validation PASSED: {len(required)} documentation/release files and README sections checked.")
    return 0
if __name__ == "__main__":
    sys.exit(main())
