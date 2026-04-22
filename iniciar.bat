@echo off
chcp 65001 >nul
title Histórias Guardadas - Startup

color 0B
cls
echo.
echo ╔════════════════════════════════════════╗
echo ║     HISTÓRIAS GUARDADAS - STARTUP     ║
echo ╚════════════════════════════════════════╝
echo.

:: Verifica se o venv existe
if not exist "venv\" (
    echo ⚠ Ambiente virtual não encontrado. Criando...
    python -m venv venv
    echo ✓ Ambiente virtual criado!
    echo.
)

:: Ativa o ambiente virtual
echo → Ativando ambiente virtual...
call venv\Scripts\activate

:: Instala/atualiza dependências
if exist "requirements.txt" (
    echo → Verificando dependências...
    pip install -q -r requirements.txt
    echo ✓ Dependências instaladas!
)

:: Aplica migrations
echo → Aplicando migrations...
python manage.py migrate --run-syncdb >nul 2>&1
echo ✓ Banco de dados atualizado!

:: Coleta arquivos estáticos (apenas se necessário)
if not exist "staticfiles\" (
    echo → Coletando arquivos estáticos...
    python manage.py collectstatic --noinput >nul 2>&1
)

echo.
echo ╔════════════════════════════════════════╗
echo ║  ✓ Servidor iniciando em...           ║
echo ║    http://127.0.0.1:8000               ║
echo ╚════════════════════════════════════════╝
echo.
echo Pressione Ctrl+C para parar o servidor
echo.

:: Aguarda 2 segundos antes de abrir o navegador
timeout /t 2 /nobreak >nul

:: Abre o navegador
start http://127.0.0.1:8000

:: Inicia o servidor
python manage.py runserver

pause
