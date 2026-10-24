$ErrorActionPreference = 'Stop'
$backendDirectory = Join-Path $PSScriptRoot 'backend'
$backendPython = Join-Path $backendDirectory '.venv/Scripts/python.exe'
if (-not (Test-Path -LiteralPath $backendPython)) {
    throw 'Install the backend dependencies in backend/.venv first.'
}
$previousDatabaseUrl = $env:DATABASE_URL
try {
    Set-Location -LiteralPath $backendDirectory
    $env:DATABASE_URL = 'sqlite:///./clienthub-local.db'
    & $backendPython -m uvicorn app.main:app --host 127.0.0.1 --port 8000
} finally {
    $env:DATABASE_URL = $previousDatabaseUrl
}
