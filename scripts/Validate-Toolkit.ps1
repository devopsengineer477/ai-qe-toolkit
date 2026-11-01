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
Write-Host "Milestone 1 + 2 + 3 validation completed successfully." -ForegroundColor Green

python scripts/validate_docs.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
\npython scripts/validate_mcp.py\nif ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }\n
python -m unittest discover -s tests -p "test_*.py"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
