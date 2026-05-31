# Product Requirements Document (PRD)
## Desafio 01 - Ingestão e Consulta de PDF com RAG

### 1. Visão Geral

Desenvolver um sistema de Retrieval-Augmented Generation (RAG) que permita ingerir documentos PDF, armazená-los como embeddings em banco de dados vetorial e consultar informações através de uma interface CLI.

---

### 2. Requisitos Funcionais

#### 2.1 Ingestão do PDF

- **Divisão em Chunks**: O PDF deve ser dividido em **chunks de 1000 caracteres** com **overlap de 150 caracteres**.
- **Geração de Embeddings**: Cada chunk deve ser convertido em embedding usando um modelo de embeddings.
- **Armazenamento Vetorial**: Os vetores devem ser armazenados no banco de dados **PostgreSQL** com a extensão **pgVector**.
- **Rastreabilidade**: Cada chunk deve manter referência ao documento original e posição no documento.

#### 2.2 Consulta via CLI

- **Interface de Chat**: Criar um script Python para simular um chat no terminal.
- **Fluxo de Processamento**: Ao receber uma pergunta, o sistema deve:
  1. **Vetorizar a pergunta** usando o mesmo modelo de embeddings.
  2. **Buscar os 10 resultados mais relevantes (k=10)** no banco vetorial através de busca por similaridade.
  3. **Montar o prompt** concatenando os resultados com as regras e contexto.
  4. **Chamar a LLM** para gerar a resposta.
  5. **Retornar a resposta** ao usuário de forma formatada.

---

### 3. Especificações Técnicas

#### 3.1 Processamento de Chunks

- **Tamanho do Chunk**: 1000 caracteres
- **Overlap**: 150 caracteres
- **Estratégia**: Sliding window com sobreposição para manter contexto entre chunks

#### 3.2 Banco de Dados

- **SGBD**: PostgreSQL
- **Extensão**: pgVector
- **Campos Obrigatórios**:
  - `id` (UUID): Identificador único do chunk
  - `content` (TEXT): Conteúdo do chunk
  - `embedding` (vector): Vetor de embeddings
  - `document_name` (VARCHAR): Nome do documento original
  - `chunk_index` (INTEGER): Índice do chunk no documento
  - `created_at` (TIMESTAMP): Data de criação

#### 3.3 Modelo de Embeddings

- Modelo: A ser definido (ex: sentence-transformers, OpenAI embedding, etc.)
- Dimensionalidade: A ser definida conforme o modelo escolhido

#### 3.4 LLM

- Modelo: A ser definido (ex: GPT-4, Claude, Gemini, etc.)
- Temperatura: A ser ajustada para respostas mais consistentes

---

### 4. Prompt do Sistema

```
CONTEXTO:
{resultados concatenados do banco de dados}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta do usuário}

RESPONDA A "PERGUNTA DO USUÁRIO"
```

---

### 5. Arquitetura do Sistema

```
┌─────────────┐
│  PDF Input  │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│ Chunking         │
│ (1000 chars + 150 overlap)
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Embedding        │
│ Generation       │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ PostgreSQL       │
│ + pgVector       │
└──────────────────┘

┌──────────────────┐
│ User Question    │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Question         │
│ Embedding        │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Vector Search    │
│ (Top 10 results) │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Prompt Assembly  │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ LLM Call         │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Response to User │
└──────────────────┘
```

---

### 6. Critérios de Aceitação

- [ ] PDF é dividido em chunks de exatamente 1000 caracteres com 150 de overlap
- [ ] Embeddings são gerados com sucesso para cada chunk
- [ ] Dados são armazenados corretamente no PostgreSQL com pgVector
- [ ] CLI aceita perguntas do usuário
- [ ] Sistema retorna top-10 resultados mais relevantes
- [ ] LLM é chamada com prompt formatado corretamente
- [ ] Respostas respeitam as regras de contexto (não inventam informações)
- [ ] Sistema é resiliente a perguntas fora do contexto

---

### 7. Escopo

#### Fora do Escopo

- Suporte a múltiplos formatos de arquivo (apenas PDF inicialmente)
- Interface web ou API REST (apenas CLI)
- Histórico de conversas persistente
- Autenticação de usuários

---

### 8. Dependências

- Python 3.8+
- PostgreSQL 12+
- pgVector extension
- Modelo de embeddings (ex: sentence-transformers)
- LLM (ex: OpenAI API, Anthropic API, etc.)

---

### 9. Próximas Etapas

1. Selecionar modelo de embeddings
2. Selecionar provider de LLM
3. Configurar ambiente PostgreSQL + pgVector
4. Implementar módulo de ingestão
5. Implementar CLI de consultas
6. Testes de end-to-end
7. Validação de respostas
