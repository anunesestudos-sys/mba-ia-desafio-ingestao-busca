# 🎯 Fluxo de Execução Multi-Agente - Guia Rápido

## O Que é Este Sistema?

Sistema de orquestração para executar o projeto RAG de forma controlada, com:
- **Builder Agent**: Executa tarefas com qualidade
- **Reviewer Agent**: Valida cada entrega criticamente
- **Você (Orchestrator)**: Coordena tudo e toma decisões

Resultado: **Projeto entregue com qualidade superior** em tempo razoável.

---

## 🚀 Como Começar AGORA

### Passo 1: Entender a Visão (5 min)
Leia [WORKFLOW.md](WORKFLOW.md) - seção "Visão Geral"

### Passo 2: Entender Seus Papéis (30 min)
- Você como Orchestrator: Leia [ORCHESTRATOR-GUIDE.md](ORCHESTRATOR-GUIDE.md)
- Builder: Leia [BUILDER-AGENT.md](BUILDER-AGENT.md)
- Reviewer: Leia [REVIEWER-AGENT.md](REVIEWER-AGENT.md)

### Passo 3: Começar Primeira Tarefa (2h)
```
1. Comunique ao Builder: "Tarefa 1.1 - Fork e Setup"
2. Builder executa (lê BUILDER-AGENT.md para protocolo)
3. Você valida rapidamente
4. Reviewer valida completamente (REVIEWER-AGENT.md)
5. Você aprova/rejeita
6. Marca DONE no TASKBOARD.md
7. Próxima tarefa!
```

---

## 📚 Arquivos de Referência

| Arquivo | Leia Quando | Tempo |
|---------|-----------|-------|
| [PRD.md](PRD.md) | Entender requirements | 10 min |
| [TASKBOARD.md](TASKBOARD.md) | Saber o que fazer depois | 5 min |
| [WORKFLOW.md](WORKFLOW.md) | Entender o fluxo | 15 min |
| [BUILDER-AGENT.md](BUILDER-AGENT.md) | Você precisa executar | 20 min |
| [REVIEWER-AGENT.md](REVIEWER-AGENT.md) | Você precisa revisar | 20 min |
| [ORCHESTRATOR-GUIDE.md](ORCHESTRATOR-GUIDE.md) | Você coordena | 30 min |

---

## 🎬 Exemplo de Ciclo (4h)

```
09:00 - VOCÊ: "Builder, tarefa 1.1 - Fork e Setup"
        (Você lê ORCHESTRATOR-GUIDE.md > seção "Scripts")

09:10 - BUILDER: Começa trabalho
        (Lê BUILDER-AGENT.md > seção "Protocolo de Execução")
        - Entendimento (10 min)
        - Planejamento (10 min)
        - Implementação (50 min)
        - Validação (10 min)

11:00 - BUILDER: "✅ Tarefa 1.1 completa, pronta para revisão"
        (Usa template em BUILDER-AGENT.md > "FASE 5")

11:10 - VOCÊ: "Valido rápido, deixa pronto para revisor"

11:20 - REVIEWER: Começa validação
        (Lê REVIEWER-AGENT.md > "Protocolo de Revisão")
        - Preparação (5 min)
        - Análise (10 min)
        - Validação Funcional (15 min)
        - Validação Código (20 min)
        - Decisão (5 min)

12:00 - REVIEWER: "✅ APROVADO - Excelente trabalho!"
        (Usa template em REVIEWER-AGENT.md > "Template de Feedback")

12:10 - VOCÊ: Marca DONE no TASKBOARD
        [ ✅ ] 1.1 - Fork e Setup: DONE

12:20 - VOCÊ: Define próxima tarefa
        (Consulta TASKBOARD.md e ORCHESTRATOR-GUIDE.md)
        "Builder, próxima: tarefa 1.2 - PostgreSQL..."

13:00 - FIM DO CICLO
```

---

## 🎯 Responsabilidades Rápidas

### Builder Faz
- ✅ Codifica com qualidade
- ✅ Inclui testes
- ✅ Documenta
- ✅ Faz commits limpos
- ✅ Submete com template

### Reviewer Faz
- ✅ Valida funcionalidade
- ✅ Revisa código
- ✅ Verifica testes
- ✅ Confirma documentação
- ✅ Aprova ou pede ajustes

### Você Faz
- ✅ Coordena fluxo
- ✅ Toma decisões
- ✅ Remove bloqueadores
- ✅ Valida arquitetura
- ✅ Marca progresso

---

## 📊 Matriz Rápida

```
              Builder     Reviewer    Orchestrator
Executa         ✅         ❌           🔍 valida
Revisa          ❌         ✅           🔍 aprova
Decide          ❌         ❌           ✅
Documenta       ✅         ✅           ✅
```

---

## 🚨 Estados das Tarefas

```
⬜ TODO          → Não começou, ou bloqueada
🟨 IN_PROGRESS   → Builder trabalhando
⏳ IN_REVIEW     → Reviewer validando
🔄 NEEDS_FIX     → Requer ajustes
✅ DONE          → Aprovada, pronta para próxima
```

---

## 💡 Dicas Ouro

### Para ter SUCESSO:

1. **Builder não tem pressa**
   - Qualidade > velocidade
   - Melhor 2h bem feito que 1h ruim

2. **Reviewer é critériosos**
   - Não aprova lixo
   - Feedback é construtivo

3. **Você coordena, não micro-gerencia**
   - Deixa Builder trabalhar
   - Deixa Reviewer revisar
   - Você toma decisões arquiteturais

4. **Comunicação clara**
   - Use templates fornecidos
   - Seja específico em feedback
   - Documente tudo

5. **Celebre vitórias**
   - Cada tarefa DONE é win
   - Reconheça bom trabalho
   - Mantenha motivação

---

## 📞 Quando Pedir Ajuda

### Builder para Você
- "Não entendo requisito X"
- "Qual padrão usar?"
- "Estou bloqueado"
- "Dúvida arquitetura"

### Reviewer para Você
- "Discordo da qualidade esperada"
- "Qual é o critério exato?"
- "Como calibro severidade?"

### Você para Builder/Reviewer
- "Vamos paralelizar"
- "Próxima tarefa é..."
- "Feedback é este aqui"

---

## 🎓 Checklist - Primeira Semana

### Dia 1
- [ ] Leu [WORKFLOW.md](WORKFLOW.md)
- [ ] Leu [ORCHESTRATOR-GUIDE.md](ORCHESTRATOR-GUIDE.md)
- [ ] Communicou Builder para tarefa 1.1
- [ ] Builder começou trabalho

### Dia 2
- [ ] Tarefa 1.1 recebida, validada, revisada
- [ ] Tarefa 1.1 aprovada ✅
- [ ] Comunicou Builder para tarefa 1.2
- [ ] Startou 1.3 (se tiver Builder-2) ou 1.2 em sequência

### Dia 3-5
- [ ] Completou FASE 1 (tarefas 1.1 a 1.4) ✅
- [ ] Documentou progresso
- [ ] Iniciou FASE 2

### Métricas Esperadas
- Tarefas completas: 4-6
- Taxa de rejeição: ~5-10% (normal)
- Qualidade: 80%+ (bom)
- Ritmo: 1-1.5 tarefas/dia

---

## 🚀 Próximos Passos

### AGORA:
1. Configure agentes em VS Code (ou use como templates)
2. Comunique ao Builder para começar 1.1
3. Fique disponível para suporte

### DEPOIS:
1. Calibre critério após primeira revisão
2. Otimize paralelização
3. Documente lessons learned

---

## 🎯 Visão do Projeto Completo

```
SEMANA 1: FASE 1 + início FASE 2
SEMANA 2: FASE 2 + FASE 3
SEMANA 3: FASE 4 + FASE 5
SEMANA 4: Testes finais, ajustes, entrega

Total: ~26 horas de trabalho = ~1 semana com dedicação full-time
       ou ~4 semanas com 1h/dia
```

---

## 📌 Lembre-se

> **Builder é cuidadoso, Reviewer é critériosos, você é maestro.**
>
> Este sistema não é para fazer rápido. É para fazer BEM.
> 
> Qualidade superior + ritmo sustentável = SUCESSO.

---

## 🤔 FAQ Rápido

**P: E se Builder ficar bloqueado?**
A: Você desbloqueia com contexto/decisão. Ver ORCHESTRATOR-GUIDE.md

**P: E se Reviewer for muito exigente?**
A: Calibre em conversa. Qual era o critério esperado?

**P: Dá para paralelizar?**
A: Sim! Tarefas independentes podem rodar em paralelo.

**P: Quanto tempo vai levar?**
A: ~26 horas de Builder + 10h Reviewer + 5h Você = ~40h total
   Se full-time: ~1 semana. Se part-time: ~4 semanas.

**P: Preciso ser especialista em tudo?**
A: Você (Orchestrator) sim. Builder não, Reviewer aprende enquanto valida.

---

## 📧 Templates Rápidos

### Você para Builder Começar
```
"Próxima tarefa: [ID] - [Nome]
 Objetivo: [breve]
 Esperado: ~[N]h
 Dependências: ✅
 Pronto?"
```

### Você para Reviewer Revisar
```
"Tarefa [ID] pronta para revisão.
 Builder entregou com [qualidade esperada].
 Pode validar?"
```

### Você Aprovando
```
"✅ Tarefa [ID] APROVADA
 Marcando DONE no TASKBOARD
 Próxima: [ID] - [Nome]"
```

---

**Tudo pronto. Você está equipado para orquestrar! 🎯**

Qualquer dúvida, volte a este arquivo.
Qualquer decisão, leia o ORCHESTRATOR-GUIDE.md.
Qualquer feedback, use os templates em BUILDER-AGENT.md e REVIEWER-AGENT.md.

Boa sorte! 🚀
