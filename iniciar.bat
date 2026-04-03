@echo off
title Histórias Guardadas
echo.
echo  Iniciando Histórias Guardadas...
echo.

call venv\Scripts\activate

python manage.py migrate --run-syncdb >nul 2>&1

start http://127.0.0.1:8000

python manage.py runserver
