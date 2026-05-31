# 📊 MONITOR - Como Acompanhar Execução em Tempo Real

## O Que é o Monitor?

Sistema para você **rastrear**, **visualizar** e **documentar** o progresso do projeto enquanto é executado.

---

## 🚀 Começar Agora

### Passo 1: Crie Arquivo de Status

Na raiz do repo, crie `STATUS.md`:

```markdown
# 📊 STATUS DE EXECUÇÃO - Desafio 01 RAG

**Última atualização**: [data e hora]
**Responsável**: [seu nome]

## ⏱️ Tempo Total
- Planejado: 26h
- Consumido: 0h
- % Completo: 0%

## 📈 Progresso Geral
```
████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0% (0/26 tarefas)
```

## 🎯 Fase Atual: FASE 1 - Setup & Infraestrutura

| # | Tarefa | Status | Builder | Reviewer | Tempo | Data |
|---|--------|--------|---------|----------|-------|------|
| 1.1 | Fork e Setup | ⬜ TODO | - | - | 0h | - |
| 1.2 | PostgreSQL | ⬜ TODO | - | - | 0h | - |
| 1.3 | Modelo Embeddings | ⬜ TODO | - | - | 0h | - |
| 1.4 | LLM Selection | ⬜ TODO | - | - | 0h | - |

## 📝 Notas Recentes
- [nenhuma ainda]

## 🚨 Bloqueadores
- [nenhum]

## 📅 Próximas Ações
1. Disparar Tarefa 1.1 com Builder
```

### Passo 2: Monitore Conforme Progride

```bash
# Quando Builder COMEÇA:
STATUS: 🟨 IN_PROGRESS (Builder trabalhando)
Data: 09:10
Tempo: 0h

# Quando Builder SUBMETE:
STATUS: ⏳ IN_REVIEW (Reviewer validando)
Data: 10:55
Tempo: 1h 45min

# Quando Reviewer APROVA:
STATUS: ✅ DONE
Data: 12:35
Tempo: 3h 25min (Builder 1h45 + Reviewer 1h40)
```

---

## 📋 Estados e Símbolos

```
⬜ TODO          = Não iniciada / bloqueada por dependência
🟨 IN_PROGRESS   = Builder executando agora
⏳ IN_REVIEW     = Reviewer validando agora
🔄 NEEDS_FIX     = Builder refazendo após feedback
✅ DONE          = Aprovada, pronta para próxima

🎯 ATUAL         = Tarefa em foco agora
📍 PRÓXIMA       = Será disparada em seguida
🚫 BLOQUEADA     = Depende de outra não concluída
```

---

## 📊 Template para Atualizar Diariamente

Use este template no STATUS.md:

```markdown
# 📊 STATUS DE EXECUÇÃO - [DATA]

**Atualizado em**: [HH:MM]
**Por**: [Você]

---

## ⏱️ Métricas

### Tempo
| Categoria | Planejado | Consumido | % |
|-----------|-----------|-----------|---|
| TOTAL | 26h | 5.5h | 21% |
| FASE 1 | 3h | 5.5h | 183% |
| FASE 2 | 6.5h | 0h | 0% |

### Qualidade
- Tarefas Completas: 2/26 (7.7%)
- Taxa de Rejeição: 5% (1 ajuste menor)
- Cobertura Média Testes: 92%
- Ritmo: 1.5 tarefas/dia

---

## 🎯 FASE 1: Setup & Infraestrutura (3h planejado)

| ID | Tarefa | Status | Builder | Reviewer | Tempo | Notas |
|---|--------|--------|---------|----------|-------|-------|
| 1.1 | Fork e Setup | ✅ DONE | 1h 45min | 1h 20min | 3h 5min | Sem problemas |
| 1.2 | PostgreSQL | 🟨 IN_PROGRESS | 1h | - | - | Próximo Reviewer 15h |
| 1.3 | Modelo Embeddings | ⬜ TODO | - | - | - | Pode iniciar 1.2 OK |
| 1.4 | LLM Selection | ⬜ TODO | - | - | - | Depende 1.2 ✅ |

---

## 📝 Log de Eventos

```
[09:00] Tarefa 1.1 disparada
[09:10] Builder começa (FASE 1: Entendimento)
[09:20] Builder prossegue (FASE 2: Planejamento)
[09:30] Builder em codificação (FASE 3)
[10:55] Builder submete com template completo
[11:05] Você valida rapidamente
[11:15] Reviewer começa validação
[12:35] Reviewer aprova ✅
[12:40] Você marca 1.1 como DONE
[12:45] Tarefa 1.2 disparada
```

---

## 🚨 Bloqueadores Atuais

[nenhum no momento]

---

## 📅 Próximas Ações

1. ⏳ Tarefa 1.2 em review até 15h
2. 📍 Após 1.2 OK, disparar 1.3
3. 📍 Se 1.2 tiver rejeição, Builder refaz
4. 🎯 FASE 1 esperada completa até sexta

---

## 💾 Histórico de Fases

### FASE 1: Setup ✅
- Status: 2/4 tarefas
- Tempo: 5.5h (vs 3h planejado)
- Observação: DB setup levou mais que planejado

### FASE 2: Ingestão ⬜
- Status: 0/6 tarefas
- Tempo: 0h
- Esperado: Próxima semana

---
```

---

## 🎯 Checklist de Monitoramento

### Diariamente (5-10 min)

```
[ ] Abri STATUS.md?
[ ] Tarefa atual está clara?
[ ] Builder tem contexto?
[ ] Reviewer está pronto?
[ ] Bloqueadores foram resolvidos?
[ ] Atualizei tempo consumido?
[ ] Atualizei estado das tarefas?
[ ] Documentei eventos importantes?
```

### Quando Builder COMEÇA

```
[ ] Status atualizado para 🟨 IN_PROGRESS
[ ] Data/hora registrada
[ ] Contexto comunicado
[ ] Builder confirmou entendimento
```

### Quando Builder SUBMETE

```
[ ] Status atualizado para ⏳ IN_REVIEW
[ ] Tempo consumido registrado
[ ] Template foi fornecido?
[ ] Você validou rapidamente?
[ ] Encaminhou para Reviewer?
[ ] Notas importantes adicionadas?
```

### Quando Reviewer RETORNA

```
[ ] Feedback lido completamente
[ ] Status será ✅ DONE ou 🔄 NEEDS_FIX?
[ ] Se DONE: próxima tarefa planejada?
[ ] Se NEEDS_FIX: Builder comunicado?
[ ] Documentei feedback importante?
```

### Ao Fim do Dia

```
[ ] STATUS.md atualizado
[ ] Progresso claramente visível
[ ] Bloqueadores documentados
[ ] Próximas ações definidas
[ ] Tempo total atualizado
[ ] Ritmo está ok?
```

---

## 📱 Visualização de Progresso

### Barra de Progresso

```
FASE 1 (3h)
████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 2/4 (50%)

FASE 2 (6.5h)
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0/6 (0%)

FASE 3 (5h)
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0/6 (0%)

FASE 4 (6.5h)
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0/4 (0%)

FASE 5 (5h)
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0/4 (0%)

TOTAL: ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 2/26 (7.7%)
```

### Timeline Visual

```
SEG   TER   QUA   QUI   SEX
[1.1] [1.2] [1.3] [1.4] [2.1]
 ✅    🟨    ⬜    ⬜    📍

Velocidade: 1.5 tarefas/dia
Ritmo: Sustentável ✅
Próxima semana: FASE 2 + 3
```

---

## 🔍 O Que Monitorar

### Performance do Builder
- Tempo por tarefa (vs planejado)
- Qualidade de submissão (template, documentação)
- Frequência de perguntas/bloqueadores
- Taxa de rejeição do Reviewer

### Performance do Reviewer
- Tempo de revisão (vs esperado)
- Critério de qualidade (muito exigente/leniente?)
- Clareza de feedback
- Consistência de decisões

### Saúde Geral do Projeto
- Ritmo sustentável?
- Qualidade mantida?
- Próximas fases alinhadas?
- Débito técnico?
- Motivação?

---

## 🚨 Quando Aumentar Vigilância

### Red Flag: Builder Muito Lento
```
Se tarefa que deveria ser 1h tomou 3h:
- Pergunte: qual foi o problema?
- Ofereça: ajuda/contexto?
- Aprenda: por que demorou?
```

### Red Flag: Reviewer Muito Rigoroso
```
Se muitas rejeições/ajustes pequenos:
- Converse: qual é o padrão?
- Calibre: o que é realmente crítico?
- Documente: critério de qualidade
```

### Red Flag: Taxa Rejeição Alta
```
Se > 10% das submissões são rejeitadas:
- Problema no briefing?
- Builder não entendeu requisitos?
- Reviewer muito exigente?
- Falta comunicação?
```

### Red Flag: Ritmo Caindo
```
Se tarefas por dia caem significativamente:
- Builder está cansado?
- Reviewer sobrecarregado?
- Tarefas ficando mais complexas?
- Precisamos paralelizar mais?
```

---

## 📊 Metricas que Importam

### Rastreie Diariamente

```
Data    | Tarefas | Tempo | % Complete | Taxa Rej. | Ritual |
--------|---------|-------|-----------|-----------|--------|
Seg     | 1       | 3h    | 4%        | 0%        | Bom ✅ |
Ter     | 1.5     | 4.5h  | 10%       | 5%        | Ok ✅  |
Qua     | 2       | 5h    | 18%       | 0%        | Bom ✅ |
Qui     | 1       | 3h    | 22%       | 0%        | Ok ✅  |
Sex     | 1       | 2.5h  | 26%       | 0%        | Bom ✅ |

Semana 1: 6.5 tarefas em 17.5h = 1.85 tasks/dia ✅
```

### Calculat Projeção

```
Atual: 6.5 tarefas em 17.5h
Taxa: 1.85 tarefas/dia
Restante: 19.5 tarefas
Dias Faltando: 19.5 / 1.85 = 10.5 dias
Data Conclusão: ~2 semanas ✅
```

---

## 📝 Template de Nota Diária

Copie e atualize diariamente:

```markdown
## [DATA] - Resumo do Dia

**Início**: 09:00
**Fim**: 18:00

### Tarefas do Dia
- [x] 1.1: ✅ DONE
- [🟨] 1.2: 🟨 Builder trabalhando (40% progresso)

### Métricas
- Tempo Builder: 1h 45min
- Tempo Reviewer: 1h 20min
- Taxa Rejeição: 0%
- Qualidade: ⭐⭐⭐⭐⭐

### Observações
- Setup foi mais rápido que planejado
- Reviewer e Builder alinhados perfeitamente
- Ritmo sustentável
- Sem bloqueadores

### Próximo Dia
- [ ] Finalizar 1.2
- [ ] Disparar 1.3 se 1.2 OK
- [ ] Paralelizar 1.3 + 1.4?

### Notas Importantes
- Builder entendeu bem o padrão
- Reviewer calibrado corretamente
- Nenhuma rejeição, um ajuste menor em 1.2 esperado
```

---

## 🎯 Exemplos de Monitores Reais

### Cenário 1: Tudo Normal ✅

```
[09:00] Você dispara 1.1
[09:10] Builder começa
        STATUS: 🟨 IN_PROGRESS

[10:55] Builder submete
        STATUS: ⏳ IN_REVIEW
        Tempo: 1h 45min

[11:15] Reviewer começa
[12:35] Reviewer aprova ✅
        STATUS: ✅ DONE
        Tempo Reviewer: 1h 20min
        Tempo Total: 3h 5min

[12:45] Você dispara 1.2
        Tudo conforme esperado!
```

### Cenário 2: Builder Bloqueado 🔴

```
[09:00] Você dispara 1.2
[09:10] Builder começa
        STATUS: 🟨 IN_PROGRESS

[10:30] Builder para
        Pergunta: "Dúvida em [X]?"
        
[10:35] Você responde
        Builder continua
        
[12:00] Builder submete
        STATUS: ⏳ IN_REVIEW
        Tempo: 2h 50min (mais lento por bloqueador)
```

### Cenário 3: Reviewer Rejeita ⚠️

```
[tera] Builder submete 1.3
        STATUS: ⏳ IN_REVIEW

[terca] Reviewer rejeita
        Problema: "Testes insuficientes"
        STATUS: 🔄 NEEDS_FIX
        
[terça 15:00] Você comunica Builder
        "Reviewer solicitou mais testes"
        
[terça 16:00] Builder refazendo
        STATUS: 🟨 IN_PROGRESS
        
[terça 17:30] Builder resubmete
        STATUS: ⏳ IN_REVIEW
        
[quarta] Reviewer aprova ✅
        STATUS: ✅ DONE
        Tempo Total: ~1 dia (atraso de 4h)
```

---

## 💾 Arquivo de Histórico

Mantenha `HISTORY.md`:

```markdown
# 📜 Histórico de Execução

## SEMANA 1

### Segunda 30/05
- [09:00] Projeto iniciado
- [09:10] Tarefa 1.1 disparada
- [12:40] Tarefa 1.1: ✅ DONE
- [12:45] Tarefa 1.2 disparada

### Terça 31/05
- [...]

## Marcos Importantes
- [30/05 12:40] Primeira tarefa completa ✅
- [31/05 17:30] FASE 1 completada 🎉
- [02/06 16:00] FASE 2 completada 🎉
- [...]
```

---

## 🎯 Seu Checklist de Monitor

### Por Hora
- [ ] Builder está progredindo?
- [ ] Algum bloqueador?
- [ ] Reviewer pronto para receber?

### Por Dia
- [ ] STATUS.md atualizado?
- [ ] Tempos registrados?
- [ ] Notas diárias adicionadas?
- [ ] Próximas ações claras?

### Por Semana
- [ ] Métricas consolidadas?
- [ ] Ritmo sustentável?
- [ ] Qualidade ok?
- [ ] Projeção atualizada?
- [ ] Lições aprendidas?

---

**Monitoramento completo! Você terá visibilidade total da execução! 📊**

---

---

# 📊 EXECUÇÃO REAL — 30/05/2026

**Atualizado em**: 30/05/2026 — sessão única (projeto completo)
**Por**: Anderson Nunes

---

## ⏱️ Métricas

### Tempo
| Categoria | Planejado | Consumido | % |
|-----------|-----------|-----------|---|
| TOTAL | 26h | ~6h | 100% tarefas |
| FASE 1 | 3h | ~1h | ✅ 4/4 |
| FASE 2 | 6.5h | ~1.5h | ✅ 6/6 |
| FASE 3 | 5h | ~1h | ✅ 6/6 |
| FASE 4 | 6.5h | ~2h | ✅ 4/4 |
| FASE 5 | 5h | ~0.5h | ✅ 4/4 |

### Qualidade
- Tarefas Completas: **26/26 (100%)**
- Taxa de Rejeição: 1 ciclo (faltavam testes → corrigido → aprovado)
- Cobertura Testes: **96%** (unitários) | 5 integração | 4 performance
- Total de testes: **38**

---

## 🎯 FASE 1: Setup & Infraestrutura ✅ DONE (4/4)

| ID | Tarefa | Status | Builder | Reviewer | Tempo | Notas |
|---|--------|--------|---------|----------|-------|-------|
| 1.1 | Fork e Setup | ✅ DONE | ~20min | ✅ | ~20min | venv Python 3.14 |
| 1.2 | PostgreSQL | ✅ DONE | ~15min | ✅ | ~15min | Docker VPS 72.60.57.117:5433, pgVector 0.8.2 |
| 1.3 | Modelo Embeddings | ✅ DONE | ~5min | ✅ | ~5min | gemini-embedding-001 |
| 1.4 | LLM Selection | ✅ DONE | ~5min | ✅ | ~5min | gemini-2.5-flash, temp=0.1 |

## 🎯 FASE 2: Módulo de Ingestão ✅ DONE (6/6)

| ID | Tarefa | Status | Builder | Reviewer | Tempo | Notas |
|---|--------|--------|---------|----------|-------|-------|
| 2.1 | Carregamento PDF | ✅ DONE | — | ✅ | — | PyPDFLoader, 34 páginas |
| 2.2 | Chunking | ✅ DONE | — | ✅ | — | 1000/150 → 67 chunks |
| 2.3 | Embeddings | ✅ DONE | — | ✅ | — | GoogleGenerativeAIEmbeddings |
| 2.4 | Conexão PostgreSQL | ✅ DONE | — | ✅ | — | PGVector langchain-postgres |
| 2.5 | Pipeline Ingestão | ✅ DONE | — | ✅ | — | ingest_pdf() completo |
| 2.6 | CLI Ingestão | ✅ DONE | — | ✅ | — | python src/ingest.py |

## 🎯 FASE 3: Módulo de Consulta ✅ DONE (6/6)

| ID | Tarefa | Status | Builder | Reviewer | Tempo | Notas |
|---|--------|--------|---------|----------|-------|-------|
| 3.1 | Vetorização Perguntas | ✅ DONE | — | ✅ | — | via retriever |
| 3.2 | Busca Vetorial | ✅ DONE | — | ✅ | — | k=10 validado em teste |
| 3.3 | Montagem Prompt | ✅ DONE | — | ✅ | — | template exato do PRD |
| 3.4 | Integração LLM | ✅ DONE | — | ✅ | — | ChatGoogleGenerativeAI |
| 3.5 | Pipeline Consulta | ✅ DONE | — | ✅ | — | LCEL chain completa |
| 3.6 | CLI Chat | ✅ DONE | — | ✅ | — | python src/chat.py |

## 🎯 FASE 4: Testes & Validação ✅ DONE (4/4)

| ID | Tarefa | Status | Builder | Reviewer | Tempo | Notas |
|---|--------|--------|---------|----------|-------|-------|
| 4.1 | Testes Unitários | ✅ DONE | ~30min | ✅ (1 rejeição → resubmissão) | ~45min | 29 testes, 96% cobertura |
| 4.2 | Testes Integração | ✅ DONE | ~20min | ✅ | ~20min | 5/5, DB + API reais |
| 4.3 | Testes Performance | ✅ DONE | ~15min | ✅ | ~15min | latência ~15s, overlap 6/10 |
| 4.4 | Validação Qualidade | ✅ DONE | ~10min | ✅ | ~10min | 4/4 QA pairs corretos |

## 🎯 FASE 5: Documentação & Deploy ✅ DONE (4/4)

| ID | Tarefa | Status | Builder | Reviewer | Tempo | Notas |
|---|--------|--------|---------|----------|-------|-------|
| 5.1 | Documentação Técnica | ✅ DONE | ~15min | ✅ | ~15min | README completo |
| 5.2 | Guia de Usuário | ✅ DONE | — | ✅ | — | CLI guide + troubleshooting |
| 5.3 | Scripts Automação | ✅ DONE | ~10min | ✅ | ~10min | setup.sh, run_tests.sh, reset_db.sh |
| 5.4 | Review Final | ✅ DONE | ~10min | ✅ | ~10min | pyflakes zero warnings |

---

## 📝 Log de Eventos

```
[13:00] Orchestrator dispara Tarefa 1.1 — "Builder, clone e configure o ambiente"
[13:05] Builder começa (FASE 1: Entendimento — lê TASKBOARD + PRD)
[13:10] Builder clona https://github.com/devfullcycle/mba-ia-desafio-ingestao-busca/
        STATUS: 🟨 IN_PROGRESS
[13:15] Builder cria venv, instala dependências (psycopg-binary 3.2.9 falha no py3.14)
        Bloqueador: versão incompatível → resolve instalando sem pin
[13:20] Builder configura VPS: docker compose up -d (PostgreSQL 5433)
[13:25] Builder instala pgVector manualmente (bootstrap container falhou)
[13:30] Builder configura .env: GOOGLE_API_KEY, DATABASE_URL
[13:35] Builder implementa ingest.py, search.py, chat.py (FASES 2+3)
[13:40] Bloqueador: embedding-001 → NOT FOUND na API v1beta
        Builder resolve: gemini-embedding-001
[13:45] Bloqueador: gemini-1.5-flash → not available to new users
        Builder resolve: gemini-2.5-flash
[13:50] Builder testa: pipeline funcionando — 67 chunks armazenados
        STATUS (2.1–3.6): ⏳ IN_REVIEW

[13:55] Reviewer inicia revisão (8 fases)
        FASE 1–2: template completo ✅, commits ✅, instruções ✅
        FASE 3: funcionalidade ✅ (in-context e out-of-context corretos)
        FASE 4: linting ✅ (pyflakes zero)
        FASE 5: RED FLAG — ZERO testes encontrados ❌
        DECISÃO: ⚠️ REQUER AJUSTES — "Criar tests/ com cobertura ≥80%"
        STATUS: 🔄 NEEDS_FIX

[14:05] Orchestrator comunica Builder: "Reviewer solicitou testes"
[14:08] Builder cria tests/ — 29 testes unitários, cobertura 96%
        Builder adiciona docstrings em todas as funções públicas
        STATUS: ⏳ IN_REVIEW (segunda submissão)

[14:15] Reviewer valida segunda submissão
        FASE 5: 29/29 testes ✅, cobertura 96% ✅
        DECISÃO: ✅ APROVADO
[14:18] Orchestrator aprova — marca FASES 1-4.1 como DONE
        Commits: ef25e57, d11f95e, aedd4c9

--- Execução das tarefas pendentes ---

[15:00] Orchestrator dispara 4.2 — Testes de Integração
[15:02] Builder implementa test_integration.py (5 testes — DB + API reais)
        Bloqueador: skipif avalia antes do load_dotenv → testes pulados
        Builder resolve: load_dotenv() antes do skipif
[15:08] 5/5 testes integração passando (35s de execução)
        STATUS: ⏳ IN_REVIEW
[15:10] Reviewer valida — APROVADO ✅

[15:12] Orchestrator dispara 4.3 — Performance
[15:13] Builder implementa test_performance.py (4 benchmarks)
        Resultado: latência ~15s (limite 30s) ✅, overlap semântico 6/10 ✅
[15:20] 4/4 passando (67s de execução)
        STATUS: ⏳ IN_REVIEW
[15:22] Reviewer valida — APROVADO ✅

[15:23] Orchestrator dispara 4.4 — Validação Qualidade
[15:24] Builder roda dataset 4 perguntas/respostas esperadas
        Resultado: 4/4 corretos
        STATUS: ⏳ IN_REVIEW
[15:25] Reviewer valida — APROVADO ✅
        Commit: fa9dce5

[15:27] Orchestrator dispara FASE 5 (5.1+5.2+5.3+5.4)
[15:28] Builder atualiza README completo (arquitetura, CLI guide, troubleshooting)
[15:32] Builder cria setup.sh, scripts/run_tests.sh, scripts/reset_db.sh
[15:36] Builder limpa imports desnecessários (pyflakes: 9 → 0 warnings)
[15:38] 29 testes unitários ainda passando após limpeza
        STATUS: ⏳ IN_REVIEW
[15:40] Reviewer valida — APROVADO ✅
        Commits: 03191a4, 7c918bd

[15:45] Orchestrator atualiza TASKBOARD.md (26/26 ✅ DONE)
[15:50] Orchestrator atualiza STATUS.md com log completo
[15:55] Orchestrator atualiza MONITOR.md com execução real ← AGORA
```

---

## 🚨 Bloqueadores Encontrados e Soluções

| Bloqueador | Impacto | Solução |
|---|---|---|
| `psycopg-binary==3.2.9` sem wheel para Python 3.14 | 1.1 atrasou ~5min | Instalar sem pin de versão |
| `models/embedding-001` removido da API v1beta | 2.3 falhou em produção | Usar `models/gemini-embedding-001` |
| `gemini-1.5-flash` não disponível para novos usuários | 3.4 falhou em produção | Usar `gemini-2.5-flash` |
| `docker compose` sem daemon local | 1.2 não rodou localmente | Usar VPS 72.60.57.117 com Docker |
| `skipif` avaliado antes do `load_dotenv()` | 4.2 todos testes pulados | Chamar `load_dotenv()` antes do `pytest.mark.skipif` |
| Zero testes nas fases 2+3 | Rejeição do Reviewer | Adicionados 29 testes + 9 integração/perf |

---

## 📅 Próximas Ações

```
✅ Projeto 100% completo — todas 26 tarefas DONE
🎉 Entrega pronta para submissão
```

---

## 💾 Histórico de Fases

### FASE 1: Setup ✅
- Status: **4/4 tarefas** em ~45min
- Bloqueadores resolvidos: 2 (psycopg versão, Docker local)
- Observação: PostgreSQL na VPS, não localmente

### FASE 2: Ingestão ✅
- Status: **6/6 tarefas** em ~90min
- Bloqueador crítico: modelo de embeddings renomeado na API
- PDF ingerido: 34 páginas → 67 chunks armazenados

### FASE 3: Consulta ✅
- Status: **6/6 tarefas** em ~60min
- Bloqueador crítico: gemini-1.5-flash descontinuado para novos usuários
- Chain LCEL funcionando, regras do PRD respeitadas

### FASE 4: Testes ✅
- Status: **4/4 tarefas** em ~90min
- 1 ciclo de rejeição → correção → aprovação (faltavam testes)
- 38 testes no total: 29 unit (96% cov) + 5 integration + 4 perf

### FASE 5: Documentação ✅
- Status: **4/4 tarefas** em ~30min
- README completo, scripts de automação, linting zero warnings

---

