# Desafio MBA Engenharia de Software com IA — Full Cycle

Sistema **RAG (Retrieval-Augmented Generation)** para ingestão e consulta de documentos PDF via CLI, desenvolvido como solução do Desafio 01 do MBA Full Cycle.

---

## Como funciona

```
PDF → chunks (1000 chars / 150 overlap) → embeddings (Gemini) → PostgreSQL/pgVector
                                                                        ↓
Pergunta → embedding → busca top-10 → prompt + contexto → Gemini 2.5 Flash Lite → resposta
```

O sistema responde **somente com base no conteúdo do PDF**. Perguntas fora do contexto retornam:
> "Não tenho informações necessárias para responder sua pergunta."

---

## Stack

| Componente | Tecnologia |
|---|---|
| PDF loading | `PyPDFLoader` via langchain-community |
| Chunking | `RecursiveCharacterTextSplitter` — 1000 chars, 150 overlap |
| Embeddings | `models/gemini-embedding-001` (Google Gemini API) |
| Vector store | PostgreSQL 17 + pgVector 0.8.2 |
| LLM | `gemini-2.5-flash-lite` (temperatura 0.1) |
| Framework | LangChain 1.x (LCEL) |
| Testes | pytest + pytest-cov (96% cobertura) |

---

## Pré-requisitos

- Python 3.8+
- Docker instalado (localmente ou em VPS)
- Google API Key — obtenha gratuitamente em [aistudio.google.com](https://aistudio.google.com/)

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/anunesestudos-sys/mba-ia-desafio-ingestao-busca.git
cd mba-ia-desafio-ingestao-busca
```

### 2. Execute o setup automático

```bash
bash setup.sh
```

O script cria o `venv`, instala todas as dependências e roda os testes unitários para confirmar que tudo está funcionando.

### 3. Configure as variáveis de ambiente

Edite o arquivo `.env` gerado na raiz:

```env
GOOGLE_API_KEY=sua_chave_aqui
GOOGLE_EMBEDDING_MODEL=models/gemini-embedding-001
DATABASE_URL=postgresql+psycopg://postgres:postgres@SEU_HOST:5433/rag
PG_VECTOR_COLLECTION_NAME=rag_documents
PDF_PATH=document.pdf
```

| Variável | Descrição |
|---|---|
| `GOOGLE_API_KEY` | Chave da API Google (obrigatório) |
| `DATABASE_URL` | Connection string do PostgreSQL com pgVector |
| `PG_VECTOR_COLLECTION_NAME` | Nome da coleção vetorial no banco |
| `PDF_PATH` | Caminho para o PDF a ingerir |

### 4. Suba o banco de dados (PostgreSQL + pgVector)

```bash
# Na máquina com Docker (local ou VPS)
docker compose up -d
```

Aguarde o container ficar `healthy` (~10s). Para verificar:

```bash
docker ps --filter name=postgres_rag
```

> O `docker-compose.yml` já inclui a instalação automática da extensão `pgvector`.

---

## Como usar

### Ingerir o PDF

```bash
source venv/bin/activate
python src/ingest.py
```

```
Carregando PDF: document.pdf
Páginas carregadas: 34
Chunks gerados: 67
Gerando embeddings e armazenando no PostgreSQL...
Ingestão concluída: 67 chunks armazenados.
```

### Iniciar o chat

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
Comandos: 'sair' para encerrar, 'ajuda' para mais opções.
------------------------------------------------------------

Você: Quais empresas estão no documento?
🔍 Estou buscando os dados ⣾
🤔 Estou pensando ⣽

Assistente: As empresas listadas são: Zenith, Ágil, Magna, Matriz...

Você: Qual é a soma dos valores?
🔢 Estou calculando ⣾

Assistente: R$ 35.997.075.370,47

Você: sair
Encerrando chat. Até logo!
```

**Comandos:**
| Comando | Ação |
|---|---|
| `sair` / `exit` | Encerra o chat |
| `ajuda` / `help` | Lista os comandos |
| `Ctrl+C` | Encerra graciosamente |

---

## Melhoria: suporte a cálculos matemáticos

Por padrão, sistemas RAG restritivos bloqueiam qualquer processamento além da leitura direta do contexto — inclusive **somas, médias e contagens** — por interpretar cálculos como "interpretação" ou "invenção".

Esta solução adiciona uma exceção explícita no prompt do sistema:

```
REGRAS:
...
- Você PODE realizar cálculos matemáticos (somas, médias, contagens) sobre
  valores e dados presentes no CONTEXTO. Isso não é invenção — é processamento
  dos dados fornecidos.
```

Com isso, perguntas como as abaixo passam a funcionar corretamente:

| Pergunta | Resposta |
|---|---|
| `"Qual é a soma de todos os valores?"` | `R$ 35.997.075.370,47` |
| `"Quantas empresas estão listadas?"` | `120` |
| `"Qual é a média dos valores?"` | calcula com base no contexto |

A regra de não inventar informações externas ao documento **permanece intacta** — o modelo só opera sobre dados que estão no contexto recuperado.

---

## Melhorias de performance

| Melhoria | Impacto |
|---|---|
| **Streaming** (`chain.stream`) | Resposta aparece palavra por palavra — percepção de velocidade imediata |
| **Animação de loading** | Mensagens progressivas: `🔍 buscando → 🤔 pensando → 🔢 calculando` |
| **Modelo `gemini-2.5-flash-lite`** | ~5× mais rápido que `gemini-2.5-flash` com qualidade equivalente para RAG |

Latência antes: **~15s** → Latência depois: **~3s** (primeiro token em ~2.6s)

---

## Testes

```bash
# Unitários (sem DB/API) — 29 testes, 96% cobertura
python -m pytest tests/ --ignore=tests/test_integration.py \
  --ignore=tests/test_performance.py -v --cov=src

# Integração (requer DB e API configurados)
python -m pytest tests/test_integration.py -v

# Suite completa (unitários + integração + benchmarks)
bash scripts/run_tests.sh
```

---

## Estrutura do projeto

```
├── src/
│   ├── ingest.py          # Pipeline: PDF → chunks → embeddings → DB
│   ├── search.py          # Chain RAG: retriever k=10 → prompt → LLM
│   └── chat.py            # CLI interativo com streaming e animação
├── tests/
│   ├── test_ingest.py         # Chunking (tamanho, overlap, edge cases)
│   ├── test_ingest_unit.py    # ingest_pdf com mocks
│   ├── test_search.py         # format_docs e prompt template
│   ├── test_search_unit.py    # search_prompt com mocks
│   ├── test_chat.py           # Loop do chat (comandos, EOF, stream)
│   ├── test_integration.py    # End-to-end com DB + API reais
│   └── test_performance.py    # Benchmarks de latência e qualidade
├── scripts/
│   ├── run_tests.sh       # Roda suite completa de testes
│   └── reset_db.sh        # Limpa chunks do banco
├── setup.sh               # Setup automático do ambiente
├── docker-compose.yml     # PostgreSQL 17 + pgVector
├── .env.example           # Template de variáveis de ambiente
└── document.pdf           # PDF de exemplo
```

---

## Troubleshooting

| Problema | Solução |
|---|---|
| `models/embedding-001 not found` | Use `models/gemini-embedding-001` no `.env` |
| `gemini-1.5-flash not found` | Modelo descontinuado — use `gemini-2.5-flash-lite` |
| `psycopg connection refused` | Verifique se o container Docker está rodando e a porta acessível |
| `PDF_PATH not set` | Configure `PDF_PATH=document.pdf` no `.env` |
| Testes de integração pulando | Verifique se `DATABASE_URL` e `GOOGLE_API_KEY` estão no `.env` |
