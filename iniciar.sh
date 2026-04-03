#!/bin/bash
echo ""
echo " Iniciando Histórias Guardadas..."
echo ""

source venv/bin/activate

python manage.py migrate --run-syncdb > /dev/null 2>&1

# Abre o navegador (tenta os mais comuns)
if command -v xdg-open &> /dev/null; then
    xdg-open http://127.0.0.1:8000 &
elif command -v gnome-open &> /dev/null; then
    gnome-open http://127.0.0.1:8000 &
fi

python manage.py runserver
