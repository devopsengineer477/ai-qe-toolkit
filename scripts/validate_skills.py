from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "qe-standards", "test-design", "api-testing",
    "pytest-automation", "playwright-automation", "postman-newman",
    "dotnet-testing", "ci-cd-automation", "k6-performance",
    "qe-orchestration", "execution-safety",
)

def main():
    errors = []
    for skill in SKILLS:
        canonical = ROOT / "skills" / skill / "SKILL.md"
        github = ROOT / ".github" / "skills" / skill / "SKILL.md"
        claude = ROOT / ".claude" / "skills" / skill / "SKILL.md"
        if not canonical.is_file():
            errors.append(f"Missing canonical skill: {skill}")
            continue
        source = canonical.read_text(encoding="utf-8").replace("\\r\\n", "\\n").strip()
        for native in (github, claude):
            if not native.is_file():
                errors.append(f"Missing native skill copy: {native.relative_to(ROOT)}")
                continue
            content = native.read_text(encoding="utf-8").replace("\\r\\n", "\\n").strip()
            if content != source:
                errors.append(f"Skill copy differs from canonical: {native.relative_to(ROOT)}")
    if errors:
        print("Skill validation FAILED:\\n" + "\\n".join(errors))
        return 1
    print(f"Skill validation PASSED: {len(SKILLS)} canonical skills and {len(SKILLS) * 2} native copies checked.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
