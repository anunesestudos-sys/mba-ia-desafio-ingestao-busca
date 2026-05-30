# Desafio MBA Engenharia de Software com IA - Full Cycle

Sistema RAG (Retrieval-Augmented Generation) para ingestão e consulta de PDFs via CLI, usando Google Gemini e PostgreSQL + pgVector.

## Pré-requisitos

- Python 3.8+
- Docker Desktop (para PostgreSQL + pgVector)
- Google API Key ([obtenha aqui](https://aistudio.google.com/))

## Setup

### 1. Ambiente Python

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Variáveis de ambiente

Edite o arquivo `.env` na raiz do projeto:

```
GOOGLE_API_KEY=sua_chave_aqui
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rag
PG_VECTOR_COLLECTION_NAME=rag_documents
PDF_PATH=document.pdf
```

### 3. PostgreSQL + pgVector

```bash
docker compose up -d
```

Aguarde o container ficar saudável (~10s).

## Como usar

### Ingerir o PDF

```bash
source venv/bin/activate
python src/ingest.py
```

### Chat interativo

```bash
source venv/bin/activate
python src/chat.py
```

Comandos dentro do chat:
- `sair` / `exit` — encerra o chat
- `ajuda` / `help` — lista os comandos

## Arquitetura

```
PDF → chunks (1000 chars, overlap 150) → embeddings (Gemini) → PostgreSQL/pgVector
Pergunta → embedding → busca top-10 → prompt + contexto → Gemini → resposta
```
