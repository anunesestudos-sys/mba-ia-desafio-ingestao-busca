# 🎯 SETUP FINAL - Como Usar Tudo Junto

## 📁 Arquivos Criados (Resumo)

```
docs/
├── PRD.md                          # Requisitos do projeto
├── TASKBOARD.md                    # Lista de tarefas
├── INDICE.md                       # Mapa de navegação
├── FLUXO-RAPIDO.md                 # Guia rápido (5 min)
├── WORKFLOW.md                     # Arquitetura do sistema
│
├── BUILDER-AGENT.md                # Guia completo Builder
├── REVIEWER-AGENT.md               # Guia completo Reviewer
├── ORCHESTRATOR-GUIDE.md           # Guia completo Orchestrator
│
├── .builder-instructions.md        # Prompt customizado Builder
├── .reviewer-instructions.md       # Prompt customizado Reviewer
├── .orchestrator-instructions.md   # Prompt customizado Orchestrator
│
├── DISPATCHER.md                   # Como disparar o fluxo
├── MONITOR.md                      # Como acompanhar execução
└── SETUP-FINAL.md                  # Este arquivo
```

---

## 🚀 Setup em 5 Passos

### PASSO 1: Configure os Agentes em VS Code (10 min)

VS Code Copilot Chat permite usar prompts customizados. Aqui tem 3 formas:

#### Opção A: Usar como Prompts Customizados (RECOMENDADO)

```bash
# 1. No VS Code, abra Chat (Cmd+I ou Cmd+Shift+I)

# 2. Selecione agente (ou crie novo)

# 3. Na primeira mensagem, copie e cole conteúdo do arquivo:
   - Copie docs/.builder-instructions.md
   - Copie docs/.reviewer-instructions.md
   - Copie docs/.orchestrator-instructions.md

# 4. Chat vai lembrar do contexto para o resto da conversa
```

#### Opção B: Usar como .instructions.md

```bash
# Se VS Code reconhece .instructions.md:

# Crie um arquivo por agente:
cp docs/.builder-instructions.md .builder.instructions.md
cp docs/.reviewer-instructions.md .reviewer.instructions.md
cp docs/.orchestrator-instructions.md .orchestrator.instructions.md

# VS Code pode usar automaticamente como contexto
```

#### Opção C: Usar como Référence/Context

```bash
# 1. Abra arquivo .instructions.md no VS Code
# 2. Deixe aberto em um tab
# 3. No Chat, faça referência: 
   "Seguindo .builder-instructions.md: [sua tarefa]"
```

### PASSO 2: Crie Arquivo STATUS.md (2 min)

Na raiz do projeto:

```bash
cp docs/STATUS-TEMPLATE.md STATUS.md
# Edite conforme seu projeto
```

Ou comece com:

```markdown
# 📊 STATUS DE EXECUÇÃO

**Início**: [data]
**Última atualização**: [data]

## Progresso
```
████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0% (0/26 tarefas)
```

## Próxima Ação
- [ ] Tarefa 1.1: Fork e Setup
```

### PASSO 3: Entenda o Fluxo (5 min)

Leia nesta ordem:

1. [FLUXO-RAPIDO.md](FLUXO-RAPIDO.md) (5 min)
2. [DISPATCHER.md](DISPATCHER.md) - Como disparar (5 min)
3. [MONITOR.md](MONITOR.md) - Como acompanhar (5 min)

### PASSO 4: Inicie com Builder (AGORA!)

Comunique:

```
Olá Builder!

Você está pronto para começar?

Leia docs/.builder-instructions.md (é seu protocolo)

Próxima tarefa: 1.1 - Fork e Setup

Objetivo: Clonar https://github.com/devfullcycle/mba-ia-desafio-ingestao-busca/
          Configurar venv, testes passam

Tempo estimado: ~1.5h

Pode começar?
```

### PASSO 5: Acompanhe com Monitor (DURANTE)

Mantenha 2 tabs abertos:

```
Tab 1: STATUS.md (atualize conforme progride)
Tab 2: Chat (acompanhe mensagens)

Quando Builder submete:
- Copie template de submissão
- Atualize STATUS.md
- Encaminhe para Reviewer
```

---

## 👥 Como Usar Cada Agente

### 1️⃣ BUILDER - Você Executa Tarefas

```
ONDE: VS Code Chat (selecione agente ou copie .builder-instructions.md)

COMO:
1. Chat começa com contexto de .builder-instructions.md
2. Você descreve tarefa (ou paste do DISPATCHER)
3. Builder segue protocolo 5-fases
4. Você submete com template

ARQUIVOS DE REFERÊNCIA:
- docs/.builder-instructions.md (seu protocolo)
- docs/BUILDER-AGENT.md (detalhado)
- docs/TASKBOARD.md (qual tarefa?)
- docs/PRD.md (requisitos)

EXEMPLO:
"Builder, próxima tarefa: 1.1 - Fork e Setup
 
 Objetivo: Clonar repo, venv, testes
 
 Repositório: https://github.com/devfullcycle/...
 
 Tempo: ~1.5h
 
 Pode começar? Se tiver dúvida, pergunte!"
```

### 2️⃣ REVIEWER - Você Valida Entregas

```
ONDE: VS Code Chat (selecione agente ou copie .reviewer-instructions.md)

COMO:
1. Chat começa com contexto de .reviewer-instructions.md
2. Você cola submissão do Builder
3. Reviewer segue protocolo 8-fases
4. Reviewer fornece feedback estruturado

ARQUIVOS DE REFERÊNCIA:
- docs/.reviewer-instructions.md (seu protocolo)
- docs/REVIEWER-AGENT.md (detalhado)
- docs/PRD.md (requisitos)

EXEMPLO:
"Reviewer, preciso de validação:

[colar submissão inteira do Builder aqui]

Favor avaliar conforme .reviewer-instructions.md"
```

### 3️⃣ ORCHESTRATOR - Você Coordena

```
ONDE: Este documento + DISPATCHER.md + MONITOR.md

COMO:
1. Leia ORCHESTRATOR-GUIDE.md (seu protocolo completo)
2. Use DISPATCHER.md para disparar tarefas
3. Use MONITOR.md para acompanhar
4. Tome decisões conforme necessário

TEMPLATES:
- Briefing Builder: em DISPATCHER.md
- Aprovação: em DISPATCHER.md
- Rejeição: em DISPATCHER.md
- Atualizar STATUS: em MONITOR.md

CICLO DIÁRIO:
1. MANHÃ: Planejar, briefar Builder
2. TARDE: Validar Builder, encaminhar Reviewer
3. FIM DIA: Receber feedback, aprovar, documentar

EXEMPLO:
"Você é o maestro. Dispara tarefas com Builder,
 valida com Reviewer, coordena o fluxo."
```

---

## 🎬 Exemplo Real - Executar Primeira Tarefa

### Dia 1 - Você Dispara

```
👤 VOCÊ:
"Builder, próxima tarefa: 1.1 - Fork e Setup

Objetivo: Clonar repositório, configurar ambiente Python

Contexto: Primeira tarefa, vai preparar tudo para as próximas

Dependências: Nenhuma (primeira tarefa)

Repositório para fork:
https://github.com/devfullcycle/mba-ia-desafio-ingestao-busca/

Padrões: Use estrutura existente do repo

Tempo estimado: ~1.5 horas

Faça a leitura de docs/.builder-instructions.md 
para entender como você trabalha.

Pode começar?
Se tiver dúvida, pergunte antes!"
```

### Você Acompanha (Monitor)

Mantenha tab com `STATUS.md`:

```
Atualizar em tempo real:

## Tarefa 1.1 - Fork e Setup

Status: 🟨 IN_PROGRESS
Builder: Trabalhando (começou 09:10)
Tempo: ~1h so far

[09:10] Builder começa (FASE 1: Entendimento)
[09:25] Builder prossegue (FASE 2: Planejamento)
[09:40] Builder em código (FASE 3)
[...esperando...]
```

### Builder Submete

```
👷 BUILDER:
"## ✅ Tarefa 1.1 - Fork e Setup

### 📝 Trabalho Realizado
- [x] Fork do repositório
- [x] Repositório clonado localmente
- [x] venv Python configurado
- [x] Requirements instalados
- [x] pytest executado com sucesso
- [x] README.md revisado

### 🔍 Como Validar
1. cd /path/to/repo
2. source venv/bin/activate
3. python -m pytest

### 📊 Métricas
- Linhas modificadas: 5 (.gitignore)
- Testes: 10/10 passando
- Cobertura: N/A (setup)
- Tempo: 1h 45min

### 🔗 Arquivos
- venv/ (Python 3.8)
- .gitignore (atualizado)
- requirements.txt (existente, ok)

### ✨ Commits
commit a1b2c3d: Initial fork and setup
commit e4f5g6h: Configure venv and dependencies

### 🚀 Próxima Tarefa Sugerida
1.2 - PostgreSQL + pgVector

STATUS: ✅ PRONTO PARA REVISÃO"
```

### Você Valida Rapidamente

```
👤 VOCÊ:
"Obrigado Builder!

Validei rapidamente:
✅ Setup completo
✅ Dependências ok
✅ Testes passam
✅ Documentação clara

Encaminhando para Reviewer agora.
Esperamos feedback em ~1h."
```

### Reviewer Valida

```
🔍 REVIEWER:
[Segue protocolo 8-fases de .reviewer-instructions.md]

[Testa localmente - tudo funciona]
[Revisa código - clean]
[Valida testes - ok]
[Confirma docs - ok]
[Compliance PRD - ok]

Resultado: APROVADO ✅

"## 🔍 Review: Tarefa 1.1 - Fork e Setup

### ✅ Status: APROVADO

### 👍 Pontos Positivos
- Setup limpo e bem organizado
- Documentação clara
- Sem problemas identificados

Este trabalho está pronto para próxima fase.

Tempo de revisão: 65 minutos"
```

### Você Aprova e Próxima

```
👤 VOCÊ:
"🎉 Tarefa 1.1 APROVADO!

Reviewer validou: ✅ Excelente trabalho

Marcando DONE no TASKBOARD

Próxima tarefa: 1.2 - PostgreSQL + pgVector

Builder, pode começar?"

[Atualiza STATUS.md]
- Tarefa 1.1: ✅ DONE (3h 10min)
- Próxima: 1.2 (disparada 12:45)
```

---

## 📊 Dashboard Visual - STATUS.md

Mantenha um arquivo bem organizado:

```markdown
# 📊 STATUS DE EXECUÇÃO

**Data**: 30/05/2026 | **Última atualização**: 16:45

---

## ⏱️ Tempo

| Categoria | Planejado | Consumido | % |
|-----------|-----------|-----------|---|
| **TOTAL** | **26h** | **3.2h** | **12%** |
| FASE 1 | 3h | 3.2h | 107% |
| FASE 2 | 6.5h | 0h | 0% |
| Resto | 16.5h | 0h | 0% |

---

## 🎯 Progresso

### FASE 1: Setup & Infraestrutura
- [x] 1.1 - Fork e Setup: ✅ DONE (3h 10min) 
- [ ] 1.2 - PostgreSQL: 🟨 IN_PROGRESS (Builder 1h so far)
- [ ] 1.3 - Embeddings: ⬜ TODO
- [ ] 1.4 - LLM: ⬜ TODO

**Progresso FASE 1**: ████░░░░░ 25% (1/4 done)

### FASE 2: Ingestão
- [ ] 2.1-2.6: ⬜ TODO

**Progresso FASE 2**: ░░░░░░░░░░ 0% (0/6)

### FASE 3: Consulta
- [ ] 3.1-3.6: ⬜ TODO

**Progresso FASE 3**: ░░░░░░░░░░ 0% (0/6)

### FASE 4: Testes
- [ ] 4.1-4.4: ⬜ TODO

### FASE 5: Docs
- [ ] 5.1-5.4: ⬜ TODO

---

## 📈 Métricas

- **Tarefas Completas**: 1/26 (3.8%)
- **Taxa de Rejeição**: 0%
- **Qualidade Média**: ⭐⭐⭐⭐⭐
- **Ritmo**: ~0.3 tarefas/h (on track)

---

## 📝 Log Recente

```
[09:00] Tarefa 1.1 disparada
[09:10] Builder começa
[10:55] Builder submete
[11:05] Você valida
[11:15] Reviewer começa
[12:20] Reviewer aprova ✅
[12:25] Tarefa 1.1: DONE
[12:30] Tarefa 1.2 disparada
[12:35] Builder começa 1.2
```

---

## 🚨 Bloqueadores

[nenhum]

---

## 📅 Próximas Ações

1. ⏳ Tarefa 1.2 em review (Builder finaliza ~14h)
2. 📍 Após 1.2 OK, iniciar 1.3
3. 🎯 FASE 1 esperada completa sexta
4. 📍 FASE 2 inicia segunda próxima

---

## 🎓 Notas

- Ritmo bom, Builder e Reviewer alinhados
- Sem rejeições, tudo fluindo bem
- Próxima semana: FASE 2 (Ingestão) - maior complexidade

---
```

---

## 🎯 Checklist Final - Está Tudo Pronto?

- [ ] Entendi o que é cada agente?
- [ ] Li FLUXO-RAPIDO.md?
- [ ] Li DISPATCHER.md (como disparar)?
- [ ] Li MONITOR.md (como acompanhar)?
- [ ] Tenho acesso aos agentes VS Code?
- [ ] Criei arquivo STATUS.md?
- [ ] Entendi o protocolo 5-fases do Builder?
- [ ] Entendi o protocolo 8-fases do Reviewer?
- [ ] Entendi ciclo diário de Orchestrator?
- [ ] Estou pronto para disparar Tarefa 1.1?

Se tudo ✅, **você está pronto!**

---

## 🚀 Comece AGORA

### Seu Primeiro Comando

Abra VS Code Chat e escreva:

```
Olá Builder!

Você está pronto para começar o desafio RAG?

Leia docs/.builder-instructions.md (é seu protocolo)

Próxima tarefa: 1.1 - Fork e Setup

Objetivo: 
- Fork https://github.com/devfullcycle/mba-ia-desafio-ingestao-busca/
- Clonar repositório
- Configurar venv Python 3.8+
- Todos os testes devem passar
- README.md revisado

Tempo estimado: ~1.5 horas

Dependências: Nenhuma (primeira tarefa)

Padrões: Use estrutura existente do repositório

Pode começar? Se tiver dúvida, pergunte!
```

---

## 📞 Referência Rápida

| Você quer | Leia isto |
|-----------|-----------|
| Começar rápido | FLUXO-RAPIDO.md |
| Disparar tarefa | DISPATCHER.md |
| Acompanhar | MONITOR.md |
| Entender arquitetura | WORKFLOW.md |
| Índice tudo | INDICE.md |
| Seu protocolo | ORCHESTRATOR-GUIDE.md |
| Builder vê | docs/.builder-instructions.md |
| Reviewer vê | docs/.reviewer-instructions.md |
| Qual tarefa fazer | TASKBOARD.md |
| Requisitos projeto | PRD.md |

---

**TUDO PRONTO! Você tem:**
- ✅ 3 agentes configurados
- ✅ Protocolo definido
- ✅ Sistema de dispatcher
- ✅ Sistema de monitor
- ✅ Documentação completa
- ✅ Primeira tarefa pronta

**Próximo passo: Dispare Tarefa 1.1 com Builder! 🚀**

