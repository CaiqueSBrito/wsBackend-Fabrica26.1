# Pokédex — Desafio Fábrica de Software - Caique Brito

API REST e interface web para gerenciamento de pokémons, com integração à PokeAPI e autenticação de usuários.

---

## Tecnologias

- **Backend**: Python 3.14, Django 6.0, Django REST Framework
- **Banco de dados**: PostgreSQL via Supabase
- **Cache**: Django LocMemCache
- **HTTP assíncrono**: httpx + asyncio
- **Containerização**: Docker + Docker Compose

---

## Screenshots

<img width="1919" height="943" alt="image" src="https://github.com/user-attachments/assets/cc56a91a-6842-4083-b44d-25f05912c258" />
<img width="1919" height="921" alt="image" src="https://github.com/user-attachments/assets/de19fa9c-7393-4ef3-8924-936c2670e8de" />
<img width="1919" height="945" alt="image" src="https://github.com/user-attachments/assets/6fa75812-05f2-480b-81b7-2f5558f6f9ff" />


---

## Requisitos

- Python 3.12+
- pip
- Docker (opcional)

---

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/CaiqueSBrito/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1/projeto_pokedex
```

### 2. Criar e ativar ambiente virtual

```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto (`projeto_pokedex/`):

```env
SECRET_KEY=sua-secret-key-aqui
DEBUG=True
DATABASE_URL=postgresql://postgres.SEU_PROJECT_REF:SUA_SENHA@aws-0-us-east-1.pooler.supabase.com:5432/postgres
DB_NAME=postgres
DB_HOST=aws-0-us-east-1.pooler.supabase.com
DB_PASS=SUA_SENHA
DB_PORT=5432
DB_USER=postgres.SEU_PROJECT_REF
```

### 5. Rodar as migrations

```bash
python manage.py migrate
```

### 6. Criar superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 7. Rodar o servidor

```bash
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000`

---

## Rodando com Docker

```bash
docker-compose up --build
```

---

## Endpoints

### Pokémons do usuário (`/api/pokebag/`)

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| GET | `/api/pokebag/` | Lista pokémons do usuário logado | Sim |
| POST | `/api/pokebag/` | Cria um novo pokémon | Sim |
| GET | `/api/pokebag/{id}/` | Detalhe de um pokémon | Não |
| PATCH | `/api/pokebag/{id}/` | Atualiza um pokémon | Sim |
| DELETE | `/api/pokebag/{id}/` | Deleta um pokémon | Sim |

### PokeAPI (`/poke_list/`)

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/poke_list/` | Lista pokémons da PokeAPI com paginação |

**Parâmetros:**

```
/poke_list/?limit=20&offset=0
```

### Autenticação

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/registro/` | Criar conta |
| POST | `/login/` | Entrar |
| GET | `/logout/` | Sair |

### Páginas

| Endpoint | Descrição |
|----------|-----------|
| `/` | Home — CRUD de pokémons |
| `/pokemons/` | Lista todos os pokémons da PokeAPI |
| `/pokemon/{id}/` | Detalhes de um pokémon cadastrado |
| `/pokemons/{id}/` | Detalhes de um pokémon da PokeAPI |
| `/login/` | Página de login |
| `/registro/` | Página de cadastro |

---

## Estrutura do Projeto

```
projeto_pokedex/
├── app_pokedex/
│   ├── migrations/
│   ├── static/app_pokedex/css/
│   │   ├── style.css
│   │   ├── animations.css
│   │   └── auth.css
│   ├── templates/app_pokedex/
│   │   ├── home.html
│   │   ├── pokemon_details.html
│   │   ├── pokemons_list.html
│   │   ├── login.html
│   │   └── registro.html
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── forms.py
├── projeto_pokedex/
│   ├── settings.py
│   └── urls.py
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
└── requirements
```

---

## Modelo de dados

### Pokemon

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | UUID | Identificador único |
| usuario | ForeignKey | Usuário dono do pokémon |
| name | CharField | Nome |
| sprite_img | ImageField | Imagem do sprite |
| type1 | CharField | Tipo primário |
| type2 | CharField | Tipo secundário (opcional) |
| hp | IntegerField | Pontos de vida |
| attack | IntegerField | Ataque |
| defense | IntegerField | Defesa |
| speed | IntegerField | Velocidade |
| abilities | TextField | Habilidades |

---

## Variáveis de ambiente

| Variável | Descrição |
|----------|-----------|
| `SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | Modo debug (`True` ou `False`) |
| `DATABASE_URL` | URL de conexão completa com o PostgreSQL |
| `DB_NAME` | Nome do banco de dados |
| `DB_HOST` | Host do banco de dados (Supabase) |
| `DB_PASS` | Senha do banco de dados |
| `DB_PORT` | Porta do banco de dados |
| `DB_USER` | Usuário do banco de dados |
