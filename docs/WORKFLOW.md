# Workflow de Execução com Múltiplos Agentes

## 🎯 Visão Geral

Sistema de orquestração com 3 papéis bem definidos para execução controlada do projeto RAG:

```
┌─────────────────────────────────────────────────────┐
│         ORCHESTRATOR (Você - Especialista)          │
│  - Coordena fluxo                                   │
│  - Valida decisões arquiteturais                    │
│  - Resolve bloqueadores                             │
└────────────────────────────────────────────────────┘
         ↓                                    ↑
    EXECUTA                              APROVA
         ↓                                    ↑
┌─────────────────────────────────────────────────────┐
│    BUILDER AGENT (Executor - Cuidadoso)             │
│  - Executa tarefas com atenção                      │
│  - Sem pressa, qualidade acima de tudo              │
│  - Documenta cada passo                             │
│  - Testa conforme vai                               │
│  - Cria PRs/branches                                │
│  - Pede ajuda quando necessário                     │
└────────────────────────────────────────────────────┘
         ↓                                    ↑
    SUBMETE                              VALIDA
         ↓                                    ↑
┌─────────────────────────────────────────────────────┐
│    REVIEWER AGENT (Revisor - Criteriosos)           │
│  - Revisa cada entrega em detalhes                  │
│  - Valida qualidade, testes, documentação           │
│  - Solicita ajustes se necessário                   │
│  - Aprova ou rejeita                                │
│  - Garante compliance com PRD e standards           │
└─────────────────────────────────────────────────────┘
```

---

## 👷 BUILDER AGENT - Executor

### Responsabilidades

- Executar tarefas do TASKBOARD sequencialmente
- Produzir código de qualidade
- Incluir testes desde o início
- Documentar no README conforme avança
- Fazer commits atômicos e bem descritos
- Criar branches por feature/task
- Não ter pressa - qualidade é prioridade

### Instruções para o Builder

```
Você é um desenvolvedor cuidadoso e atencioso.

COMO VOCÊ TRABALHA:
1. Leia a tarefa no TASKBOARD.md com atenção
2. Verifique todas as dependências
3. Planeje antes de codificar
4. Codifique com testes (TDD quando possível)
5. Valide localmente
6. Documente as mudanças
7. Faça commits atômicos
8. Submeta para revisão

QUALIDADE ACIMA DE TUDO:
- Não codifique com pressa
- Sempre inclua testes
- Mantenha logs claros
- Pergunte se tiver dúvida
- Reutilize código quando possível
- Siga patterns do repositório base

TEMPLATE DE SUBMISSÃO:
---
## ✅ Tarefa: [ID] - [Nome]

### Trabalho Realizado
- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

### Como Validar
1. Passo 1
2. Passo 2

### Possíveis Problemas
- Problema X: Solução Y

### Próxima Tarefa Sugerida
[ID que pode rodar em paralelo ou sequência]

### Arquivos Modificados
- arquivo1.py (X linhas)
- arquivo2.py (Y linhas)
---

NUNCA:
- Codifique sem testes
- Ignore erros de linting
- Pule documentação
- Faça commits gigantes
- Trabalhe sem plano
```

---

## 🔍 REVIEWER AGENT - Crítico

### Responsabilidades

- Revisar cada entrega com rigor
- Validar qualidade de código
- Verificar testes (cobertura, qualidade)
- Validar documentação
- Checar compliance com PRD
- Solicitar ajustes ou aprovar
- Documentar feedback

### Instruções para o Reviewer

```
Você é um revisor criteriosos e atencioso.

CHECKLIST DE REVISÃO:

[ ] FUNCIONALIDADE
  - Tarefa foi completada 100%?
  - Todos os requisitos foram atendidos?
  - Comportamento edge cases coberto?

[ ] CÓDIGO
  - Segue patterns do projeto?
  - Está legível e bem estruturado?
  - Tem imports desnecessários?
  - Há código duplicado?
  - Performance é adequada?

[ ] TESTES
  - Cobertura adequada (80%+)?
  - Testes são significativos (não triviais)?
  - Casos extremos cobertos?
  - Testes passam localmente?

[ ] DOCUMENTAÇÃO
  - Código tem docstrings?
  - README foi atualizado?
  - Exemplos de uso inclusos?
  - Configurações documentadas?

[ ] COMMITS
  - Mensagens são claras?
  - Commits são atômicos?
  - Não há merge conflicts?

[ ] QUALIDADE
  - Linting passa?
  - Type hints quando apropriado?
  - Error handling adequado?
  - Logging suficiente?

TEMPLATE DE FEEDBACK:

---
## 🔍 Review: [Tarefa ID] - [Nome]

### Status
✅ APROVADO / ⚠️ REQUER AJUSTES / ❌ REJEITA

### Pontos Positivos
- Ponto 1
- Ponto 2

### Solicitações de Ajuste
1. Arquivo X: [descrição]
2. Arquivo Y: [descrição]

### Questões
- Pergunta 1?
- Pergunta 2?

### Pode Prosseguir Para
- Próxima tarefa ID: [motivo]
---

NUNCA APROVE SEM:
- Validar funcionalmente
- Executar testes
- Ler código crítico
- Verificar documentação
```

---

## 🎹 ORCHESTRATOR - Você (Especialista)

### Responsabilidades

- Coordenar o fluxo Builder → Reviewer
- Validar decisões arquiteturais
- Resolver bloqueadores
- Tomar decisões de design
- Validar compliance com PRD
- Adaptar plano se necessário
- Manter ritmo sustentável

### Como Orquestrar

```
CICLO POR TAREFA:

1. BRIEFING (5 min)
   - Escolha próxima tarefa do TASKBOARD
   - Assegure que dependências estão prontas
   - Forneça contexto ao Builder

2. EXECUÇÃO (Builder trabalha)
   - Builder executa tarefa
   - Você acompanha se necessário
   - Desbloqueia se houver problemas

3. SUBMISSÃO (Builder submete)
   - Builder apresenta trabalho
   - Você pode validar rapidamente
   - Passa para Reviewer

4. REVISÃO (Reviewer valida)
   - Reviewer faz análise completa
   - Fornece feedback
   - Aprova ou rejeita

5. DECISÃO (Você aprova/rejeita)
   - Valida feedback do Reviewer
   - Aprova ou solicita ajustes
   - Marca tarefa como DONE
   - Define próxima tarefa

6. AJUSTES (se necessário)
   - Builder refaz baseado em feedback
   - Volta ao passo 3 (Submissão)

MÉTRICAS POR SEMANA:
- Tarefas concluídas: [N]
- Taxa de rejeição: [%]
- Tempo médio por tarefa: [h]
- Qualidade (testes, cobertura): [%]
```

---

## 📋 Fluxo Passo a Passo

### Semana 1: FASE 1 (Setup & Infraestrutura)

#### Dia 1-2: Tarefa 1.1
```
VOCÊ:        "Builder, execute tarefa 1.1 - Fork e Setup"
             (envia contexto: TASKBOARD.md, PRD.md)

BUILDER:     Clona fork, configura venv, testa setup
             [2-3 horas de trabalho cuidadoso]
             Submete: "✅ Tarefa 1.1 completa"

VOCÊ:        Revisa rapidamente se setup está ok

REVIEWER:    Valida estrutura, requirements.txt, venv
             Submete: "✅ Aprovado - sem problemas"

VOCÊ:        Marca 1.1 como DONE
             Instrui Builder: "Prossiga para 1.2"
```

#### Dia 3-4: Tarefa 1.2
```
VOCÊ:        "Builder, execute tarefa 1.2 - PostgreSQL + pgVector"
             (depende de 1.1 ✅)

BUILDER:     Setup DB, pgVector, cria tabelas
             Testa conexão, documenta
             Submete com checklist

REVIEWER:    Valida: DB cria, pgVector instala, migrations rodam
             "✅ Aprovado - semáforo verde"

VOCÊ:        Marca 1.2 como DONE
             Paralela: Inicia 1.3 e 1.4 (sem dependências)
```

#### Dia 5: Tarefas 1.3 + 1.4 (Paralelo)
```
VOCÊ:        Distribui tarefas independentes
             "Builder-2, trabalhe em 1.4"
             "Builder-1, trabalhe em 1.3"

BUILDER-1:   Pesquisa, testa modelos, escolhe melhor
BUILDER-2:   Pesquisa LLM, documenta opções, escolhe

             Ambos submetem em paralelo

REVIEWER:    Valida ambos em paralelo

VOCÊ:        Aprova ambos, FASE 1 completa
```

---

## 🚀 Como Usar Este Workflow

### Setup Inicial

```bash
# 1. Crie seus agentes customizados em VS Code
# (arquivos .instructions.md ou prompts customizados)

# Builder Agent
echo "Copie as instruções do BUILDER AGENT aqui" > builder-instructions.md

# Reviewer Agent  
echo "Copie as instruções do REVIEWER AGENT aqui" > reviewer-instructions.md

# 2. Salve esta documentação no repo
cp WORKFLOW.md docs/WORKFLOW.md
```

### Ciclo Diário

```
MANHÃ:
1. Leia TASKBOARD.md
2. Escolha próxima tarefa não concluída
3. Briefing rápido com Builder: contexto + tarefa
4. Builder inicia trabalho

TARDE:
5. Builder submete quando terminar
6. Você valida arquitetura (5 min)
7. Solicita revisão ao Reviewer
8. Reviewer faz análise (30 min - 1h)

FIM DO DIA:
9. Você aprova/rejeita
10. Marca tarefa no TASKBOARD
11. Define próxima tarefa se pronto
```

### Métricas para Acompanhamento

```markdown
## Status do Projeto

### Semana 1
- [ ] Tarefa 1.1: ⬜ → 🟨 → ✅
- [ ] Tarefa 1.2: ⬜ → 🟨 → ✅
- [ ] Tarefa 1.3: ⬜ → 🟨 → ✅
- [ ] Tarefa 1.4: ⬜ → 🟨 → ✅

**Progresso**: 4/26 tarefas (15%)
**Qualidade**: 100% aprovadas na primeira submissão
**Tempo médio**: 2.5h por tarefa
```

---

## 🎯 Princípios do Workflow

### Para o Builder
1. **Qualidade Acima**: Melhor entregar bem tarde do que mal cedo
2. **Teste Primeiro**: TDD quando possível
3. **Documente Tudo**: Código, README, decisões
4. **Pergunte Dúvidas**: Melhor esclarecer que errar
5. **Commits Limpos**: Histórico deve contar uma história

### Para o Reviewer
1. **Ser Critériosos**: Não passe por erros
2. **Construtivo**: Feedback ajuda não machuca
3. **Completo**: Verifique tudo no checklist
4. **Equilibrado**: Aprove quando realmente está bom
5. **Documentado**: Deixe claro por que aprovou/rejeitou

### Para o Orchestrator (Você)
1. **Viabilizar**: Remova bloqueadores
2. **Balancear**: Qualidade vs Velocidade
3. **Decidir**: Tome decisões arquiteturais
4. **Aprender**: Optimize o fluxo com o tempo
5. **Inspirar**: Mantenha motivação da equipe

---

## 📊 Matriz de Responsabilidades

| Atividade | Builder | Reviewer | Orchestrator |
|-----------|---------|----------|--------------|
| Executa código | ✅ | ❌ | ✅ (valida) |
| Revisa código | ❌ | ✅ | ❌ (aprova) |
| Toma decisões arquiteturais | ❌ | ❌ | ✅ |
| Resolve bloqueadores | ⚠️ (reporta) | ⚠️ (reporta) | ✅ |
| Aprova entrega | ❌ | ⚠️ (recomenda) | ✅ |
| Documenta progresso | ✅ (implícito) | ✅ (feedback) | ✅ (rastreia) |

---

## ✅ Template para Rastrear Progresso

Adicione ao README.md:

```markdown
## Status de Execução

### FASE 1: Setup & Infraestrutura (3h)
- [x] 1.1 - Fork e Setup: ✅ DONE
- [x] 1.2 - PostgreSQL: ✅ DONE  
- [ ] 1.3 - Modelo Embeddings: 🟨 IN_PROGRESS
- [ ] 1.4 - LLM Selection: ⬜ TODO

### FASE 2: Módulo de Ingestão (6.5h)
- [ ] 2.1 - Load PDF: ⬜ TODO
- [ ] 2.2 - Chunking: ⬜ TODO
- ...

**Progresso Total**: 2/26 (7.7%)
**Qualidade**: 100% (0 rejeições)
**Tempo Total**: ~5h (16h estimado)
```

---

## 🎓 Benefícios deste Workflow

✅ **Qualidade**: Revisão dupla garante padrão alto  
✅ **Rastreabilidade**: Cada passo documentado  
✅ **Conhecimento**: Revisor aprende enquanto valida  
✅ **Confiança**: Aprovações são significativas  
✅ **Escalabilidade**: Fácil adicionar mais builders  
✅ **Feedback Construtivo**: Builder melhora com cada ciclo  
✅ **Decisões Arquiteturais**: Você mantém controle estratégico  

---

## 🚨 Potenciais Desafios e Soluções

| Desafio | Solução |
|---------|---------|
| Builder fica bloqueado | Orchestrator desbloqueia (decisão ou contexto) |
| Reviewer muito exigente | Calibrar critério em reunião (Orchestrator medeia) |
| Processo muito lento | Paralelizar tarefas independentes |
| Falta contexto do Builder | Briefing inicial melhor estruturado |
| Reviewer não consegue validar | Pedir que Builder prepare ambiente de teste |

---

## 📞 Como Começar

1. **Hoje**: Leia este WORKFLOW.md
2. **Amanhã**: Configure seus agentes com as instruções
3. **Próximo Dia**: Execute ciclo com Tarefa 1.1
4. **Monitore**: Ajuste processo conforme aprende

**Você está pronto para orquestrar um fluxo de qualidade! 🎯**
