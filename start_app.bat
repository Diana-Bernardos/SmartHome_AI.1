@echo off
echo ===================================================
echo    Iniciando Asistente Domotico Inteligente v2.0
echo ===================================================
echo.

:: 1. Iniciar Backend (Python/FastAPI)
echo [1/2] Iniciando Servidor Backend (Puerto 8000)...
start "Backend API" cmd /k "python -m uvicorn api:app --reload --host 0.0.0.0 --port 8000"

:: Esperar unos segundos para que el backend arranque
timeout /t 3 /nobreak >nul

:: 2. Iniciar Frontend (React/Vite)
echo [2/2] Iniciando Interface Frontend (Puerto 5173)...
cd frontend
start "Frontend UI" cmd /k "npm run dev"

echo.
echo ===================================================
echo    Sistema Iniciado! Abre tu navegador si no se
echo    abrio automaticamente: http://localhost:5173
echo ===================================================
echo.
pause
