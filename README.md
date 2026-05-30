# Desafio MBA Engenharia de Software com IA - Full Cycle

Sistema RAG (Retrieval-Augmented Generation) para ingestão e consulta de PDFs via CLI.

## Visão Geral

```
PDF → chunks (1000 chars / 150 overlap) → embeddings (Gemini) → PostgreSQL/pgVector
Pergunta → embedding → busca top-10 → prompt + contexto → Gemini 2.5 Flash → resposta
```

Responde **somente com base no conteúdo do PDF**. Perguntas fora do contexto retornam:
> "Não tenho informações necessárias para responder sua pergunta."

## Stack

| Componente | Tecnologia |
|---|---|
| PDF loading | PyPDF via `langchain-community` |
| Chunking | `RecursiveCharacterTextSplitter` (1000 chars, 150 overlap) |
| Embeddings | `models/gemini-embedding-001` (Google Gemini) |
| Vector store | PostgreSQL 17 + pgVector 0.8.2 |
| LLM | `gemini-2.5-flash` (temperatura 0.1) |
| Framework | LangChain 1.x (LCEL) |

## Pré-requisitos

- Python 3.8+
- Docker (para PostgreSQL + pgVector na VPS)
- Google API Key — [aistudio.google.com](https://aistudio.google.com/)

## Setup Rápido

```bash
# Clone e configure
git clone https://github.com/devfullcycle/mba-ia-desafio-ingestao-busca/
cd mba-ia-desafio-ingestao-busca

# Setup automático (venv + deps + testes)
bash setup.sh

# Edite o .env
nano .env   # preencha GOOGLE_API_KEY
```

## Configuração do Banco (VPS com Docker)

```bash
# Na VPS
mkdir -p ~/rag-desafio
# Copie o docker-compose.yml para ~/rag-desafio/ e execute:
docker compose up -d
```

No `.env` local:
```
DATABASE_URL=postgresql+psycopg://postgres:postgres@IP_DA_VPS:5433/rag
```

## Variáveis de Ambiente (`.env`)

| Variável | Descrição | Exemplo |
|---|---|---|
| `GOOGLE_API_KEY` | Chave da API Google | `AIza...` |
| `GOOGLE_EMBEDDING_MODEL` | Modelo de embeddings | `models/gemini-embedding-001` |
| `DATABASE_URL` | Connection string PostgreSQL | `postgresql+psycopg://...` |
| `PG_VECTOR_COLLECTION_NAME` | Nome da coleção no banco | `rag_documents` |
| `PDF_PATH` | Caminho para o PDF | `document.pdf` |

## Como Usar

### 1. Ingerir o PDF

```bash
source venv/bin/activate
python src/ingest.py
```

Saída esperada:
```
Carregando PDF: document.pdf
Páginas carregadas: 34
Chunks gerados: 67
Gerando embeddings e armazenando no PostgreSQL...
Ingestão concluída: 67 chunks armazenados.
```

### 2. Chat Interativo

```bash
source venv/bin/activate
python src/chat.py
```

```
============================================================
  RAG Chat - Consulta de Documentos PDF
============================================================
Inicializando sistema...
Sistema pronto! Faça sua pergunta.

Você: Quais empresas estão no documento?
Assistente: As empresas listadas são: Zenith, Ágil, Magna, Matriz...

Você: Qual é a capital da França?
Assistente: Não tenho informações necessárias para responder sua pergunta.

Você: sair
Encerrando chat. Até logo!
```

**Comandos disponíveis:**
- `sair` / `exit` — encerra o chat
- `ajuda` / `help` — lista os comandos
- `Ctrl+C` — encerra graciosamente

## Estrutura do Projeto

```
desafio/
├── src/
│   ├── ingest.py     # Pipeline de ingestão (PDF → chunks → embeddings → DB)
│   ├── search.py     # Chain RAG (retriever k=10 → prompt → LLM)
│   └── chat.py       # CLI de chat interativo
├── tests/
│   ├── test_ingest.py         # Testes de chunking
│   ├── test_ingest_unit.py    # Testes ingest_pdf com mocks
│   ├── test_search.py         # Testes format_docs e prompt template
│   ├── test_search_unit.py    # Testes search_prompt com mocks
│   ├── test_chat.py           # Testes loop do chat
│   ├── test_integration.py    # Testes end-to-end (requer DB + API)
│   └── test_performance.py    # Benchmarks de latência e qualidade
├── scripts/
│   ├── run_tests.sh   # Roda suite completa de testes
│   └── reset_db.sh    # Limpa chunks do banco
├── setup.sh           # Setup automático do ambiente
├── docker-compose.yml # PostgreSQL + pgVector (para VPS)
├── .env               # Variáveis de ambiente (não versionado)
└── document.pdf       # PDF de exemplo para ingestão
```

## Testes

```bash
# Unitários (sem DB/API)
python -m pytest tests/ --ignore=tests/test_integration.py \
  --ignore=tests/test_performance.py -v --cov=src

# Integração (requer DB e API configurados)
python -m pytest tests/test_integration.py -v

# Todos (unitários + integração + performance)
bash scripts/run_tests.sh
```

**Cobertura atual:** 96% (29 testes unitários + 9 testes integração/performance)

## Troubleshooting

| Problema | Solução |
|---|---|
| `models/embedding-001 not found` | Use `models/gemini-embedding-001` no `.env` |
| `gemini-1.5-flash not found` | Use `gemini-2.5-flash` em `search.py` |
| `psycopg connection refused` | Verifique se Docker está rodando na VPS e porta 5433 está acessível |
| `PDF_PATH not set` | Configure `PDF_PATH=document.pdf` no `.env` |
