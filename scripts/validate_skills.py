from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("qe-standards", "test-design", "api-testing", "pytest-automation", "playwright-automation", "postman-newman", "dotnet-testing", "ci-cd-automation", "k6-performance")
def main():
    errors=[]
    for skill in SKILLS:
        a=ROOT/".github"/"skills"/skill/"SKILL.md"
        b=ROOT/".claude"/"skills"/skill/"SKILL.md"
        if not a.is_file() or not b.is_file(): errors.append(f"Missing native skill copy: {skill}"); continue
        x=a.read_text(encoding="utf-8").replace("\r\n","\n").strip()
        y=b.read_text(encoding="utf-8").replace("\r\n","\n").strip()
        if x != y: errors.append(f"Skill copies differ: {skill}")
    if errors:
        print("Skill validation FAILED:\n"+"\n".join(errors)); return 1
    print(f"Skill validation PASSED: {len(SKILLS)} skills synchronized across Claude Code and Copilot."); return 0
if __name__ == "__main__": sys.exit(main())
