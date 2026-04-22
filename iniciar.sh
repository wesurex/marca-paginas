#!/bin/bash

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "╔════════════════════════════════════════╗"
echo "║     HISTÓRIAS GUARDADAS - STARTUP     ║"
echo "╚════════════════════════════════════════╝"
echo -e "${NC}"

# Verifica se o venv existe
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}⚠ Ambiente virtual não encontrado. Criando...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}✓ Ambiente virtual criado!${NC}"
fi

# Ativa o ambiente virtual
echo -e "${BLUE}→ Ativando ambiente virtual...${NC}"
source venv/bin/activate

# Instala/atualiza dependências
if [ -f "requirements.txt" ]; then
    echo -e "${BLUE}→ Verificando dependências...${NC}"
    pip install -q -r requirements.txt
    echo -e "${GREEN}✓ Dependências instaladas!${NC}"
fi

# Aplica migrations
echo -e "${BLUE}→ Aplicando migrations...${NC}"
python manage.py migrate --run-syncdb > /dev/null 2>&1
echo -e "${GREEN}✓ Banco de dados atualizado!${NC}"

# Coleta arquivos estáticos (apenas se necessário)
if [ ! -d "staticfiles" ]; then
    echo -e "${BLUE}→ Coletando arquivos estáticos...${NC}"
    python manage.py collectstatic --noinput > /dev/null 2>&1
fi

echo ""
echo -e "${GREEN}╔════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  ✓ Servidor iniciando em...           ║${NC}"
echo -e "${GREEN}║    http://127.0.0.1:8000               ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════╝${NC}"
echo ""
echo -e "${YELLOW}Pressione Ctrl+C para parar o servidor${NC}"
echo ""

# Aguarda 2 segundos antes de abrir o navegador
sleep 2

# Abre o navegador (tenta os mais comuns)
if command -v xdg-open &> /dev/null; then
    xdg-open http://127.0.0.1:8000 &
elif command -v gnome-open &> /dev/null; then
    gnome-open http://127.0.0.1:8000 &
elif command -v kde-open &> /dev/null; then
    kde-open http://127.0.0.1:8000 &
fi

# Inicia o servidor
python manage.py runserver
