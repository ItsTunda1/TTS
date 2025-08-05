@echo off
setlocal

REM Get the absolute path to this script's directory
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Activate the virtual environment
call "%SCRIPT_DIR%venv\Scripts\activate.bat"

REM Set PYTHONPATH so the TTS module is found
set PYTHONPATH=%SCRIPT_DIR%

REM Start the TTS server in the background
start "" python TTS\server\server.py

REM Wait a few seconds for the server to start, then open browser
timeout /t 5 /nobreak >nul
start http://localhost:5002

pause
