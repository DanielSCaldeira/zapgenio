@echo off
set PYTHONPATH=c:\git\zapgenio\backend
backend\venv\Scripts\activate
uvicorn api.main:app --reload