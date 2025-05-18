@echo off
set PYTHONPATH=c:\git\zapgenio\backend
backend\venv\Scripts\activate
echo Iniciando FastAPI (uvicorn)...
start cmd /k "cd backend && uvicorn api.main:app --reload --port 8000"

timeout /t 3 >nul
echo Iniciando LocalTunnel...
python localtunnel_run.py
