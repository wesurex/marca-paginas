# Marca Páginas

Sistema para salvar o progresso de leitura de livros, mangás, manhwas e manhuas. Cadastre obras, registre o capítulo/página onde parou e volte de onde saiu com um clique.

---

## Pré-requisitos

| | Windows | Ubuntu |
|---|---|---|
| Python | 3.10+ | 3.10+ |
| pip | incluso no Python | incluso no Python |
| Git | opcional | opcional |

---

## Instalação no Windows

Abra o **Prompt de Comando** ou **PowerShell** na pasta do projeto.

### 1. Criar o ambiente virtual

```cmd
python -m venv venv
```

### 2. Ativar o ambiente virtual

```cmd
venv\Scripts\activate
```

> O terminal deve mostrar `(venv)` no início da linha.

### 3. Instalar as dependências

```cmd
pip install django==6.0.3 pillow
```

### 4. Aplicar as migrações do banco de dados

```cmd
python manage.py migrate
```

### 5. Criar o usuário administrador (opcional)

```cmd
python manage.py createsuperuser
```

### 6. Rodar o servidor

```cmd
python manage.py runserver
```

Acesse no navegador: **http://127.0.0.1:8000**

Painel admin: **http://127.0.0.1:8000/admin**

---

## Instalação no Ubuntu

Abra o terminal na pasta do projeto.

### 1. Instalar o Python (caso não tenha)

```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv -y
```

### 2. Criar o ambiente virtual

```bash
python3 -m venv venv
```

### 3. Ativar o ambiente virtual

```bash
source venv/bin/activate
```

> O terminal deve mostrar `(venv)` no início da linha.

### 4. Instalar as dependências

```bash
pip install django==6.0.3 pillow
```

### 5. Aplicar as migrações do banco de dados

```bash
python manage.py migrate
```

### 6. Criar o usuário administrador (opcional)

```bash
python manage.py createsuperuser
```

### 7. Rodar o servidor

```bash
python manage.py runserver
```

Acesse no navegador: **http://127.0.0.1:8000**

Painel admin: **http://127.0.0.1:8000/admin**

---

## Como usar

### Cadastrar uma obra
1. Clique em **Cadastrar** no menu ou no botão da tela inicial
2. Preencha o título, tipo (livro/manga/manhwa/manhua), autor e capa
3. Salve — o progresso é criado automaticamente no capítulo 1

### Atualizar onde você parou
1. Abra a obra pelo nome
2. Clique em **Atualizar progresso**
3. Informe o capítulo, página e cole a **URL exata** onde parou
4. Salve

### Continuar lendo
1. Na tela inicial, clique em **Continuar** na obra desejada
2. O sistema abre diretamente a URL salva

### Gêneros
Gêneros são gerenciados pelo painel admin (`/admin`). Crie os gêneros lá e eles aparecerão como opções no formulário de cadastro.

---

## Estrutura de pastas

```
besteirinha/
├── core/               # App principal
│   ├── models.py       # Obra, Progresso, Histórico, Gênero
│   ├── views.py        # Lógica das páginas
│   ├── forms.py        # Formulários
│   ├── urls.py         # Rotas do app
│   └── templates/      # HTML das páginas
├── library/            # Configurações do projeto Django
├── media/              # Imagens de capa enviadas (criado automaticamente)
├── db.sqlite3          # Banco de dados (criado após migrate)
└── manage.py
```

---

## Rotas disponíveis

| URL | Descrição |
|-----|-----------|
| `/` | Dashboard — obras em leitura e pausadas |
| `/obras/` | Biblioteca completa com filtros |
| `/obras/criar/` | Cadastrar nova obra |
| `/obras/<id>/` | Detalhe da obra |
| `/obras/<id>/editar/` | Editar dados da obra |
| `/obras/<id>/deletar/` | Remover obra |
| `/obras/<id>/progresso/` | Atualizar progresso de leitura |
| `/admin/` | Painel de administração |
