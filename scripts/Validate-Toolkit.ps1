$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
Write-Host "AI QE Toolkit validation" -ForegroundColor Cyan
python --version
if ($LASTEXITCODE -ne 0) { throw "Python is required and must be on PATH." }
python scripts/validate_toolkit.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python scripts/validate_skills.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "Milestone 1 + 2 validation completed successfully." -ForegroundColor Green
