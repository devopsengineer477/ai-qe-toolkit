from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
SKILLS=("qe-standards","test-design","api-testing","pytest-automation","playwright-automation","postman-newman","dotnet-testing","ci-cd-automation","k6-performance","qe-orchestration","execution-safety")
REQUIRED=("AGENTS.md","CLAUDE.md",".github/copilot-instructions.md",".github/agents/test-architect.agent.md",".github/agents/api-test-designer.agent.md",".github/agents/automation-developer.agent.md",".github/agents/ci-pipeline-reviewer.agent.md",".claude/agents/test-architect.md",".claude/agents/api-test-designer.md",".claude/agents/automation-developer.md",".claude/agents/ci-pipeline-reviewer.md",".claude/agents/qe-orchestrator.md",".github/agents/qe-orchestrator.agent.md")
def main():
    missing=[p for p in REQUIRED if not (ROOT/p).is_file()]
    for skill in SKILLS:
        for loc in (".github/skills",".claude/skills"):
            p=ROOT/loc/skill/"SKILL.md"
            if not p.is_file(): missing.append(str(p.relative_to(ROOT)))
            else:
                txt=p.read_text(encoding="utf-8")
                m=re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$",txt)
                if not txt.startswith("---\n") or not m or m.group(1)!=skill: missing.append(f"Invalid skill metadata: {p.relative_to(ROOT)}")
    if missing:
        print("Toolkit validation FAILED:\n"+"\n".join(" - "+x for x in missing)); return 1
    print(f"Toolkit validation PASSED: {len(REQUIRED)} required files and {len(SKILLS)*2} native skill files checked."); return 0
if __name__ == "__main__": sys.exit(main())
