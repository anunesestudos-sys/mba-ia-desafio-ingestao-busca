# Task Board - Desafio 01: RAG com PDF

## Legenda de Status
- `⬜ TODO` - Não iniciada
- `🟨 IN_PROGRESS` - Em progresso
- `✅ DONE` - Concluída

---

## FASE 1: SETUP & INFRAESTRUTURA

### 1.1 - Fork e Setup do Repositório Base ✅ DONE
**Descrição**: Fazer fork e clonar repositório do desafio, configurar ambiente Python
**Dependências**: Nenhuma
**Esforço**: 0.5h
- [x] ✅ Fazer fork de https://github.com/devfullcycle/mba-ia-desafio-ingestao-busca/
- [x] ✅ Clonar repositório localmente
- [x] ✅ Inicializar venv Python 3.14
- [x] ✅ Instalar dependencies base do requirements.txt
- [x] ✅ Verificar .gitignore e documentação inicial

### 1.2 - Configuração PostgreSQL + pgVector ✅ DONE
**Descrição**: Setup do banco de dados local ou cloud
**Dependências**: 1.1
**Esforço**: 1h
- [x] ✅ Instalar/acessar PostgreSQL (pgvector/pgvector:pg17 via Docker)
- [x] ✅ Instalar extensão pgVector 0.8.2
- [x] ✅ Criar database `rag`
- [x] ✅ Criar schema e tabelas (via PGVector.from_documents)
- [x] ✅ Configurar DATABASE_URL no .env (VPS 72.60.57.117:5433)

### 1.3 - Seleção de Modelo de Embeddings ✅ DONE
**Descrição**: Avaliar e selecionar modelo de embeddings
**Dependências**: 1.1
**Esforço**: 1h
- [x] ✅ Pesquisar modelos disponíveis (Google Gemini API)
- [x] ✅ Modelo selecionado: `models/gemini-embedding-001`
- [x] ✅ Validado em produção (67 chunks gerados)
- [x] ✅ Dependências instaladas (langchain-google-genai)

### 1.4 - Seleção de LLM ✅ DONE
**Descrição**: Avaliar e selecionar provider de LLM
**Dependências**: Nenhuma
**Esforço**: 0.5h
- [x] ✅ Provider selecionado: Google Gemini
- [x] ✅ Modelo: `gemini-2.5-flash` (temperatura 0.1)
- [x] ✅ API key configurada no .env
- [x] ✅ Validado em produção (respostas corretas)

---

## FASE 2: DESENVOLVIMENTO - MÓDULO DE INGESTÃO

### 2.1 - Módulo de Carregamento de PDF ✅ DONE
**Descrição**: Ler e extrair texto do PDF
**Dependências**: 1.1
**Esforço**: 1h
- [x] ✅ PyPDFLoader instalado via langchain-community
- [x] ✅ Carregamento de PDF via PyPDFLoader (34 páginas carregadas)
- [x] ✅ Testes unitários de chunking (test_ingest.py)

### 2.2 - Módulo de Chunking ✅ DONE
**Descrição**: Dividir texto em chunks de 1000 chars com overlap de 150
**Dependências**: 2.1
**Esforço**: 1h
- [x] ✅ RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
- [x] ✅ Validação de tamanho via testes (test_chunk_size_respects_limit)
- [x] ✅ Overlap validado (test_chunk_overlap_creates_continuity)
- [x] ✅ Edge cases cobertos (vazio, curto, múltiplos docs)
- [x] ✅ 67 chunks gerados do document.pdf

### 2.3 - Módulo de Embeddings ✅ DONE
**Descrição**: Converter texto em vetores de embeddings
**Dependências**: 1.3, 2.2
**Esforço**: 1.5h
- [x] ✅ GoogleGenerativeAIEmbeddings (models/gemini-embedding-001)
- [x] ✅ Batch processing via PGVector.from_documents
- [x] ✅ Validado em produção (67 embeddings armazenados)

### 2.4 - Módulo de Conexão PostgreSQL ✅ DONE
**Descrição**: Gerenciar conexões e operações no banco
**Dependências**: 1.2
**Esforço**: 1.5h
- [x] ✅ PGVector (langchain-postgres) com connection pooling implícito
- [x] ✅ Tabelas criadas automaticamente pelo PGVector
- [x] ✅ insert via from_documents, similarity_search via as_retriever(k=10)
- [x] ✅ Tratamento de exceções em search_prompt()
- [x] ✅ Testes unitários com mocks (test_search_unit.py)

### 2.5 - Pipeline Completo de Ingestão ✅ DONE
**Descrição**: Orquestrar todo o fluxo PDF -> Chunks -> Embeddings -> DB
**Dependências**: 2.1, 2.2, 2.3, 2.4
**Esforço**: 1.5h
- [x] ✅ ingest_pdf() orquestra todo o pipeline
- [x] ✅ Logging de progresso (páginas, chunks, status)
- [x] ✅ Validação de variáveis de ambiente
- [x] ✅ pre_delete_collection=True para re-ingestão limpa
- [x] ✅ 67 chunks armazenados com sucesso

### 2.6 - CLI para Ingestão ✅ DONE
**Descrição**: Criar comando linha para ingerir PDFs
**Dependências**: 2.5
**Esforço**: 0.5h
- [x] ✅ python src/ingest.py executa o pipeline completo
- [x] ✅ Validação de PDF_PATH e DATABASE_URL
- [x] ✅ Feedback ao usuário via print statements

---

## FASE 3: DESENVOLVIMENTO - MÓDULO DE CONSULTA

### 3.1 - Módulo de Vetorização de Perguntas ✅ DONE
**Dependências**: 1.3, 2.3 | **Esforço**: 0.5h
- [x] ✅ Vetorização via retriever (mesmo modelo de embeddings)
- [x] ✅ Pergunta normalizada via strip() antes de invoke

### 3.2 - Módulo de Busca Vetorial ✅ DONE
**Dependências**: 2.4, 3.1 | **Esforço**: 1h
- [x] ✅ as_retriever(search_kwargs={"k": 10})
- [x] ✅ k=10 validado em teste (test_retriever_uses_k_equals_10)
- [x] ✅ Ordenação por similaridade implícita no PGVector

### 3.3 - Módulo de Montagem de Prompt ✅ DONE
**Dependências**: 3.2 | **Esforço**: 0.5h
- [x] ✅ PromptTemplate.from_template(PROMPT_TEMPLATE) — template exato do PRD
- [x] ✅ Testes: contexto e pergunta preenchidos corretamente

### 3.4 - Módulo de Integração com LLM ✅ DONE
**Dependências**: 1.4, 3.3 | **Esforço**: 1.5h
- [x] ✅ ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)
- [x] ✅ Retry gerenciado pelo SDK do Google
- [x] ✅ Exceções capturadas em search_prompt()

### 3.5 - Pipeline Completo de Consulta ✅ DONE
**Dependências**: 3.1–3.4 | **Esforço**: 1h
- [x] ✅ LCEL chain: retriever | format_docs | prompt | llm | StrOutputParser
- [x] ✅ Tratamento de exceções com retorno None
- [x] ✅ Casos extremos testados (entrada vazia, EOF)

### 3.6 - CLI de Chat Interativo ✅ DONE
**Dependências**: 3.5 | **Esforço**: 1h
- [x] ✅ Loop input/output com python src/chat.py
- [x] ✅ Comandos: sair, exit, ajuda, help
- [x] ✅ Ctrl+C e EOF tratados graciosamente
- [x] ✅ 7 testes cobrindo todos os fluxos do chat

---

## FASE 4: TESTES & VALIDAÇÃO

### 4.1 - Testes Unitários (Cobertura 80%+) ✅ DONE
**Descrição**: Testes isolados de cada módulo
**Dependências**: 2.1 a 3.6 | **Esforço**: 3h
- [x] ✅ 29 testes — chunking, embeddings mock, DB mock, busca k=10, prompt, chat
- [x] ✅ Cobertura total: **96%** (meta: 80%)
- [x] ✅ ingest.py: 97% | search.py: 100% | chat.py: 86%

### 4.2 - Testes de Integração ✅ DONE
**Dependências**: 4.1 | **Esforço**: 2h
- [x] ✅ test_query_in_context_returns_answer
- [x] ✅ test_query_out_of_context_returns_standard_message
- [x] ✅ test_multiple_questions_in_sequence
- [x] ✅ test_fabricated_question_is_refused
- [x] ✅ test_ingest_pipeline_stores_67_chunks
- [x] ✅ 5/5 testes passando (requerem DB + API)

### 4.3 - Testes de Performance ✅ DONE
**Dependências**: 2.5, 3.5 | **Esforço**: 1.5h
- [x] ✅ Latência média de consulta: ~15s (limite: 30s)
- [x] ✅ 3 consultas sequenciais: média 15.15s
- [x] ✅ Overlap semântico consultas similares: 6/10 (mínimo 5)
- [x] ✅ Consultas diferentes têm baixo overlap (3/10)
- [x] ✅ 4/4 benchmarks passando

### 4.4 - Validação de Qualidade ✅ DONE
**Dependências**: 3.6 | **Esforço**: 2h
- [x] ✅ Dataset validado: 4/4 pares pergunta/resposta corretos
- [x] ✅ Sistema retorna dados reais do documento (empresas, valores)
- [x] ✅ Não inventa informações (testado com "Zenith em 2030")
- [x] ✅ Regra "Não tenho informações" aplicada corretamente

---

## FASE 5: DOCUMENTAÇÃO & DEPLOYMENT

### 5.1 - Documentação Técnica ✅ DONE
**Dependências**: Todas | **Esforço**: 2h
- [x] ✅ README.md completo com arquitetura, stack, setup
- [x] ✅ Estrutura de diretórios documentada
- [x] ✅ Todas as variáveis de ambiente documentadas
- [x] ✅ Exemplos de uso com saída esperada

### 5.2 - Guia de Usuário ✅ DONE
**Dependências**: 2.6, 3.6 | **Esforço**: 0.5h
- [x] ✅ Guia de ingestão de PDF no README
- [x] ✅ Guia de chat com exemplos reais
- [x] ✅ Comandos documentados (sair, exit, ajuda, help)
- [x] ✅ Seção troubleshooting com erros comuns

### 5.3 - Scripts de Automação ✅ DONE
**Dependências**: Todas | **Esforço**: 1h
- [x] ✅ setup.sh — venv + deps + testes unitários
- [x] ✅ scripts/run_tests.sh — suite completa
- [x] ✅ scripts/reset_db.sh — limpar chunks do banco
- [x] ✅ Scripts com permissão de execução (chmod +x)

### 5.4 - Review Final & Limpeza ✅ DONE
**Dependências**: 5.1–5.3 | **Esforço**: 1.5h
- [x] ✅ pyflakes zero warnings em src/ e tests/
- [x] ✅ Imports desnecessários removidos
- [x] ✅ 29 testes unitários passando
- [x] ✅ 5 integração + 4 performance passando

---

## SUMÁRIO DE ESFORÇO

| Fase | Tarefa | Horas Planejado | Status |
|------|--------|-----------------|--------|
| 1 | Setup & Infraestrutura | 3.0h | ✅ DONE (4/4) |
| 2 | Módulo de Ingestão | 6.5h | ✅ DONE (6/6) |
| 3 | Módulo de Consulta | 5.0h | ✅ DONE (6/6) |
| 4 | Testes & Validação | 6.5h | ✅ DONE (4/4) |
| 5 | Documentação & Deploy | 5.0h | ✅ DONE (4/4) |
| **TOTAL** | | **26.0h** | **✅ 26/26 tarefas** |

---

## DEPENDÊNCIAS CRÍTICAS

```
1.1, 1.2, 1.3, 1.4 (Setup)
    ↓
2.1 → 2.2 → 2.3 → 2.4 → 2.5 → 2.6 (Pipeline de Ingestão)
    ↓
3.1 → 3.2 → 3.3 → 3.4 → 3.5 → 3.6 (Pipeline de Consulta)
    ↓
4.1 → 4.2 → 4.3 → 4.4 (Testes)
    ↓
5.1 → 5.2 → 5.3 → 5.4 (Finalização)
```

---

## PARALELIZAÇÃO POSSÍVEL

**Podem ser feitas em paralelo após FASE 1:**
- 2.1 + 3.6 (módulos de input/output não dependem um do outro inicialmente)

**Podem ser feitas em paralelo após FASE 2.4:**
- 2.5 + 3.1 (não têm dependência direta)

---

## NOTAS

- Total de 26 horas de esforço estimado
- Cada tarefa é a menor unidade eficiente para qualidade e rastreamento
- Inclui testes em todas as etapas (não apenas no final)
- Documentação integrada no desenvolvimento
- Scripts de automação reduzem overhead operacional
