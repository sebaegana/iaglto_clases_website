@echo off
if "%1"=="install" (
    env\Scripts\pip install langchain chromadb pypdf langchain-community langchain-openai python-dotenv
    exit /b
)
if "%1"=="ingest" (
    env\Scripts\python ingest.py
    exit /b
)
if "%1"=="query" (
    env\Scripts\python query.py
    exit /b
)
if "%1"=="run" (
    env\Scripts\python ingest.py
    if errorlevel 1 exit /b 1
    env\Scripts\python query.py
    exit /b
)
if "%1"=="clean" (
    rmdir /S /Q chroma_db 2>nul
    exit /b
)

echo Comando desconocido o no proporcionado.
echo Uso: make [install^|ingest^|query^|run^|clean]
