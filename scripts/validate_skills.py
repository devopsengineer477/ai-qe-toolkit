from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("qe-standards", "test-design", "api-testing")
LOCATIONS = (".github/skills", ".claude/skills")

def read_skill(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Missing skill file: {path.relative_to(ROOT)}")
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n") or "\nname:" not in content:
        raise ValueError(f"Missing YAML frontmatter/name: {path.relative_to(ROOT)}")
    return content.replace("\r\n", "\n").strip()

def main() -> int:
    errors = []
    for skill in SKILLS:
        canonical = ROOT / ".github" / "skills" / skill / "SKILL.md"
        try:
            expected = read_skill(canonical)
        except Exception as exc:
            errors.append(str(exc))
            continue
        for location in LOCATIONS[1:]:
            target = ROOT / location / skill / "SKILL.md"
            try:
                actual = read_skill(target)
                if actual != expected:
                    errors.append(f"Skill copy differs: {target.relative_to(ROOT)}")
            except Exception as exc:
                errors.append(str(exc))
    if errors:
        print("Skill validation FAILED:")
        for error in errors:
            print(f" - {error}")
        return 1
    print(f"Skill validation PASSED: {len(SKILLS)} skills match across {len(LOCATIONS)} native locations.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
