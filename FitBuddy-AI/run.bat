@echo off
setlocal

cd /d "%~dp0"

if not exist .venv (
  where py >nul 2>nul
  if not errorlevel 1 (
    py -m venv .venv
  ) else (
    where python >nul 2>nul
    if errorlevel 1 (
      echo Python 3.11 or newer is required. Install it from https://www.python.org/downloads/ and enable Add Python to PATH.
      pause
      exit /b 1
    )
    python -m venv .venv
  )
)

call .venv\Scripts\activate
if not exist .env copy .env.example .env >nul
python -m pip install -r requirements.txt
if errorlevel 1 exit /b 1

echo FitBuddy is starting at http://127.0.0.1:8000
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
