# Histórias Guardadas

Sistema completo para gerenciar seu progresso de leitura de livros, mangás, manhwas e manhuas. Cadastre obras, registre onde parou, busque rapidamente e organize seus links favoritos.

## ✨ Funcionalidades

- 📚 **Cadastro de Obras** - Livros, mangás, manhwas e manhuas
- 🔖 **Controle de Progresso** - Capítulo, página e URL onde parou
- 🔍 **Busca AJAX** - Encontre obras instantaneamente enquanto digita
- ⭐ **Sistema de Favoritos** - Marque obras especiais e links externos
- 🔗 **Links Externos** - Organize sites favoritos com drag & drop
- 📊 **Dashboard** - Visualize o que está lendo, pausado ou completo
- 🎨 **Dark Theme** - Interface moderna e agradável aos olhos
- 📱 **Responsivo** - Funciona perfeitamente em mobile e desktop

---

## Pré-requisitos

| | Windows | Ubuntu |
|---|---|---|
| Python | 3.10+ | 3.10+ |
| pip | incluso no Python | incluso no Python |
| Git | opcional | opcional |

---

## 🚀 Instalação Rápida

### Windows

```cmd
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar ambiente
venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Aplicar migrações
python manage.py migrate

# 5. Criar superusuário (opcional)
python manage.py createsuperuser

# 6. Iniciar servidor
iniciar.bat
```

**Ou simplesmente execute `iniciar.bat` após o passo 4!**

---

### Linux/Ubuntu

```bash
# 1. Instalar Python (se necessário)
sudo apt update && sudo apt install python3 python3-pip python3-venv -y

# 2. Criar ambiente virtual
python3 -m venv venv

# 3. Ativar ambiente
source venv/bin/activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Aplicar migrações
python manage.py migrate

# 6. Criar superusuário (opcional)
python manage.py createsuperuser

# 7. Iniciar servidor
./iniciar.sh
```

**Ou simplesmente execute `./iniciar.sh` após o passo 5!**

Acesse no navegador: **http://127.0.0.1:8000**

---

## 📖 Como usar

### 🔍 Buscar Obras
1. Digite no campo de busca no topo da home
2. Resultados aparecem instantaneamente (mínimo 2 caracteres)
3. Clique em uma obra para ver os detalhes

### 📚 Cadastrar uma Obra
1. Clique em **+ Cadastrar** no menu
2. Preencha:
   - Título, tipo (livro/manga/manhwa/manhua)
   - Autor (opcional)
   - Capa (upload ou URL)
   - Descrição e notas pessoais
   - Classificação de 1-10
3. Salve — o progresso é criado automaticamente no capítulo 1

### ⭐ Marcar como Favorito
1. Clique no ícone de estrela no card da obra
2. Obras favoritas aparecem em destaque na home

### 📊 Atualizar Progresso
1. Abra a obra pelo nome
2. Clique em **Atualizar progresso**
3. Informe:
   - Capítulo e página atual
   - URL exata onde parou
   - Status (lendo, pausado, completo, abandonado)
   - Notas (opcional)
4. Salve — o histórico é registrado automaticamente

### 🔗 Gerenciar Links Externos
1. Na home, clique no botão **+** na seção "Links Externos"
2. Preencha título, URL, descrição e escolha um ícone
3. Ou acesse `/favoritos/` para gerenciar todos os links
4. **Arraste** os itens pela grip (⋮⋮) para reordenar

### 🎯 Continuar Lendo
1. Na home, clique em **Continuar** na obra desejada
2. O sistema abre diretamente a URL salva

---

## 📁 Estrutura do Projeto

```
marca-paginas/
├── core/                           # App principal
│   ├── models.py                   # Obra, Progresso, Histórico, Gênero, Favorito
│   ├── views.py                    # Lógica das páginas + AJAX
│   ├── forms.py                    # Formulários (Obra, Progresso, Favorito)
│   ├── urls.py                     # Rotas do app
│   ├── admin.py                    # Configuração do admin
│   ├── static/core/js/             # JavaScript
│   │   ├── search.js               # Busca AJAX
│   │   ├── favoritos.js            # Modal + drag & drop
│   │   └── obras.js                # Toggle favoritos
│   ├── templates/core/             # Templates HTML
│   │   ├── base.html               # Template base (dark theme)
│   │   ├── index.html              # Home
│   │   ├── obras/                  # Templates de obras
│   │   └── favoritos/              # Templates de favoritos
│   └── migrations/                 # Migrações do banco
├── library/                        # Configurações Django
├── media/                          # Uploads (capas)
├── db.sqlite3                      # Banco de dados SQLite
├── requirements.txt                # Dependências Python
├── iniciar.bat                     # Script de inicialização (Windows)
├── iniciar.sh                      # Script de inicialização (Linux)
└── manage.py                       # Django CLI
```

## 🎨 Tecnologias

### Backend
- Python 3.11+
- Django 6.0.3
- Pillow (processamento de imagens)

### Frontend
- Bootstrap 5.3.3 (CSS/JS framework)
- Bootstrap Icons 1.11.3
- SortableJS 1.15.0 (drag & drop)
- Vanilla JavaScript (sem jQuery)

### Banco de Dados
- SQLite (desenvolvimento)
- Suporta PostgreSQL/MySQL (produção)

## 🔧 Configurações Avançadas

### Ícones para Links Externos
Use classes do [Bootstrap Icons](https://icons.getbootstrap.com/):
- `bi-book` - Livros/Leitura
- `bi-github` - GitHub
- `bi-code-slash` - Código/Dev
- `bi-link-45deg` - Link genérico
- `bi-star` - Favoritos

### Personalizar Tema
Edite as variáveis CSS em `core/templates/core/base.html`:
```css
:root {
  --bg:       #0c0c0e;
  --surface:  #141418;
  --purple:   #8b6fd4;
  --text:     #f0eeff;
  --muted:    #888899;
}
```

## 📄 Documentação Adicional

- **IMPLEMENTACAO_COMPLETA.md** - Detalhes técnicos da implementação
- **requirements.txt** - Lista de dependências Python

## 🐛 Troubleshooting

### Servidor não inicia
```bash
# Verifique se o ambiente virtual está ativo
# Windows: venv\Scripts\activate
# Linux: source venv/bin/activate

# Reinstale dependências
pip install -r requirements.txt
```

### Busca AJAX não funciona
- Abra DevTools (F12) → Console
- Verifique se há erros JavaScript
- Teste endpoint: `/ajax/obras/search/?q=test`

### Drag & Drop não funciona
- Verifique se SortableJS carregou (Network tab)
- Acesse `/favoritos/` diretamente
- Limpe cache do navegador (Ctrl + Shift + R)

## 📝 Licença

Este projeto é de código aberto e está disponível para uso pessoal e educacional.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests

---

**Desenvolvido com Django + Bootstrap** 💜

---

## 🗺️ Rotas Disponíveis

### Principais
| URL | Descrição |
|-----|-----------|
| `/` | Dashboard — busca, favoritos, obras em leitura e pausadas |
| `/obras/` | Biblioteca completa com filtros |
| `/obras/criar/` | Cadastrar nova obra |
| `/obras/<id>/` | Detalhe da obra com histórico |
| `/obras/<id>/editar/` | Editar dados da obra |
| `/obras/<id>/deletar/` | Remover obra |
| `/obras/<id>/progresso/` | Atualizar progresso de leitura |

### Favoritos (Links Externos)
| URL | Descrição |
|-----|-----------|
| `/favoritos/` | Gerenciar links externos (drag & drop) |
| `/favoritos/criar/` | Adicionar novo link |
| `/favoritos/<id>/editar/` | Editar link |
| `/favoritos/<id>/deletar/` | Remover link |

### AJAX
| URL | Descrição |
|-----|-----------|
| `/ajax/obras/search/?q=<query>` | Busca de obras (JSON) |
| `/ajax/obras/<id>/toggle-favorito/` | Marcar/desmarcar favorito |
| `/favoritos/reordenar/` | Salvar ordem dos links |

### Administração
| URL | Descrição |
|-----|-----------|
| `/admin/` | Painel de administração Django |
