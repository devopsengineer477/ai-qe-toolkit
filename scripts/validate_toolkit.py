from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    ".github/skills/qe-standards/SKILL.md",
    ".github/skills/test-design/SKILL.md",
    ".github/skills/api-testing/SKILL.md",
    ".claude/skills/qe-standards/SKILL.md",
    ".claude/skills/test-design/SKILL.md",
    ".claude/skills/api-testing/SKILL.md",
    ".github/agents/test-architect.agent.md",
    ".github/agents/api-test-designer.agent.md",
    ".claude/agents/test-architect.md",
    ".claude/agents/api-test-designer.md",
]

def main() -> int:
    missing = [item for item in REQUIRED if not (ROOT / item).is_file()]
    if missing:
        print("Toolkit validation FAILED. Missing files:")
        for item in missing:
            print(f" - {item}")
        return 1

    # Lightweight frontmatter checks; this is not a full YAML parser.
    skills = list((ROOT / ".github" / "skills").glob("*/SKILL.md"))
    bad = []
    for path in skills:
        content = path.read_text(encoding="utf-8")
        folder = path.parent.name
        match = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", content)
        if not content.startswith("---\n") or not match or match.group(1) != folder:
            bad.append(str(path.relative_to(ROOT)))
    if bad:
        print("Invalid skill metadata:")
        for item in bad:
            print(f" - {item}")
        return 1

    print(f"Toolkit structure validation PASSED: {len(REQUIRED)} required files and {len(skills)} skill metadata entries checked.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
