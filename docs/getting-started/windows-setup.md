# Windows Setup

## Prerequisites
- Windows 10/11 or a managed Windows workstation.
- Git.
- Python 3.10+ available on PATH for repository validation.
- VS Code.
- Claude Code CLI and/or GitHub Copilot extension, subject to your organization's licensing and policies.

## Install
1. Extract the toolkit ZIP to a working folder, for example `C:\Projects\ai-qe-toolkit`.
2. Open that folder in VS Code.
3. Run `git init` if this is a new local repository, then commit the baseline.
4. Open PowerShell in the repository root.
5. Run:

```powershell
python --version
.\scripts\Validate-Toolkit.ps1
```

6. Open Claude Code from the repository root with `claude`, or use Copilot Chat in VS Code Agent mode.

## Updating skills
`skills/` contains canonical skill files. After editing a canonical skill, synchronize the native copies:

```powershell
.\scripts\Sync-Skills.ps1
python scripts\validate_skills.py
```

Do not hand-edit only one native copy; the validator will report drift.

## Project adoption
Copy or adapt `AGENTS.md` and the relevant standards into a project repository only after reviewing organization-specific policies. Do not copy secrets, internal endpoints or customer data into the toolkit.
