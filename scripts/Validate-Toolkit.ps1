$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

Write-Host "AI QE Toolkit validation" -ForegroundColor Cyan
Write-Host "Repository: $Root"

$Python = Get-Command python -ErrorAction SilentlyContinue
if (-not $Python) {
    Write-Error "Python was not found. Install Python 3.10+ or add it to PATH."
    exit 1
}

python --version
python scripts/validate_toolkit.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python scripts/validate_skills.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "Validation completed successfully." -ForegroundColor Green
