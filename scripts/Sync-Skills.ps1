# Copy canonical skills to Claude Code's native project skill directory.
# Copilot's canonical copies are stored in .github/skills.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$SourceRoot = Join-Path $Root ".github\skills"
$TargetRoot = Join-Path $Root ".claude\skills"

New-Item -ItemType Directory -Force -Path $TargetRoot | Out-Null
Get-ChildItem -Path $SourceRoot -Directory | ForEach-Object {
    $targetDir = Join-Path $TargetRoot $_.Name
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
    Copy-Item -Path (Join-Path $_.FullName "SKILL.md") -Destination $targetDir -Force
}
Write-Host "Synchronized skills to .claude/skills."
