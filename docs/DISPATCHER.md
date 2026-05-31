# 🚀 DISPATCHER - Como Iniciar e Disparar o Fluxo

## O Que é o Dispatcher?

Sistema para você **iniciar** e **acompanhar** a execução do projeto RAG com múltiplos agentes.

---

## ⚡ Início Rápido (5 min)

### Passo 1: Prepare Agentes em VS Code (UMA VEZ)

```bash
# Crie os 3 agentes customizados em VS Code:

1. BUILDER AGENT
   - File: docs/.builder-instructions.md
   - Use como prompt customizado

2. REVIEWER AGENT
   - File: docs/.reviewer-instructions.md
   - Use como prompt customizado

3. ORCHESTRATOR (você)
   - File: docs/.orchestrator-instructions.md
   - Guia de referência

# Para usar em VS Code Copilot Chat:
# 1. Abra chat (Cmd+I ou Cmd+Shift+I)
# 2. Selecione agente
# 3. Cole o conteúdo do arquivo como prompt inicial
# Ou: Use as instruções como templates para customizar agentes
```

### Passo 2: Você Inicia o Fluxo (AGORA!)

```
👤 VOCÊ (Orchestrator):
"Builder, você está pronto?
 Próxima tarefa: 1.1 - Fork e Setup
 
 Objetivo: Clonar repo, configurar venv, testes rodam
 
 Dependências: ✅ Nenhuma (primeira tarefa)
 
 Repositório: https://github.com/devfullcycle/mba-ia-desafio-ingestao-busca/
 
 Tempo estimado: ~1.5h
 
 Pode começar?"
```

### Passo 3: Builder Começa

```
👷 BUILDER:
Segue protocolo em .builder-instructions.md:
1. ENTENDIMENTO (10 min) - lê tarefa
2. PLANEJAMENTO (10 min) - faz plano
3. IMPLEMENTAÇÃO (50 min) - codifica
4. VALIDAÇÃO (10 min) - testa
5. SUBMISSÃO (5 min) - entrega com template

[Builder trabalha...]
```

### Passo 4: Builder Submete

```
👷 BUILDER (após ~2h):
"## ✅ Tarefa 1.1 - Fork e Setup

### 📝 Trabalho Realizado
- [x] Fork do repositório
- [x] Repo clonado
- [x] venv configurado
- [x] pytest passa
- [x] README.md atualizado

### 🔍 Como Validar
1. cd /path/to/repo
2. python -m pytest
3. source venv/bin/activate

### 📊 Métricas
- Linhas adicionadas: 0 (só setup)
- Testes: 10/10 passando
- Cobertura: N/A (setup)
- Tempo: 1h 45min

[... resto do template ...]

STATUS: ✅ PRONTO PARA REVISÃO"
```

### Passo 5: Você Valida

```
👤 VOCÊ:
"Obrigado Builder!

Validei rapidamente:
✅ Funcionalidade ok
✅ Commits bem documentados
✅ Setup pronto

Encaminhando para Reviewer agora."
```

### Passo 6: Reviewer Valida

```
🔍 REVIEWER:
Segue protocolo em .reviewer-instructions.md:
1. PREPARAÇÃO (5 min)
2. ANÁLISE SUBMISSÃO (5 min)
3. VALIDAÇÃO FUNCIONAL (15 min) - testa localmente
4. VALIDAÇÃO CÓDIGO (20 min) - lê código
5. VALIDAÇÃO TESTES (15 min)
6. VALIDAÇÃO DOCS (10 min)
7. COMPLIANCE PRD (10 min)
8. DECISÃO (5 min)

[Reviewer trabalha...]
```

### Passo 7: Reviewer Retorna

```
🔍 REVIEWER (após ~1.5h):
"## 🔍 Review: Tarefa 1.1 - Fork e Setup

### ✅ Status: APROVADO

### 👍 Pontos Positivos
- Setup limpo e bem organizado
- Documentação clara
- Sem problemas identificados

Pronto para próxima tarefa.

Tempo de revisão: 75 minutos"
```

### Passo 8: Você Aprova

```
👤 VOCÊ:
"🎉 Tarefa 1.1 APROVADA!

Reviewer validou: ✅ Excelente trabalho

Marcando DONE no TASKBOARD

Próxima tarefa: 1.2 - PostgreSQL + pgVector

Builder, pode começar?"
```

---

## 📋 Template de Disparo (Copie e Cole)

Quando for disparar uma tarefa, use este template:

```
👤 ORCHESTRATOR:
"Builder, próxima tarefa: [ID] - [Nome Tarefa]

📌 Objetivo
[Descrição breve: o que fazer]

📚 Contexto
[Por quê é importante / qual é o problema que resolve]

✅ Dependências
- [Tarefa X]: ✅ DONE
- [Tarefa Y]: ✅ DONE

🎨 Padrões / Referências
- Use [padrão X] conforme em [tarefa Y]
- Evite [anti-pattern Z]

⏱️ Tempo Estimado
~[N] horas

📖 Documentação
- Leia: [arquivo 1, arquivo 2]
- Referência: [link ou arquivo]

❓ Dúvidas?
Pergunte antes de começar!

🚀 Pode começar?"
```

---

## 🔄 Ciclo Completo (Tempo Real)

### DIA 1 - SEGUNDA

```
09:00 - VOCÊ DISPARA TAREFA 1.1
Comunica ao Builder (5 min)

09:10 - BUILDER COMEÇA
Segue protocolo (1h 45min)

10:55 - BUILDER SUBMETE
Com template completo

11:05 - VOCÊ VALIDA
Rapidamente (5 min)

11:15 - REVIEWER COMEÇA
Segue protocolo (1h 20min)

12:35 - REVIEWER RETORNA
Com feedback

12:40 - VOCÊ APROVA
Marca DONE no TASKBOARD

12:45 - VOCÊ DISPARA TAREFA 1.2
Para o Builder

13:00 - BUILDER COMEÇA 1.2
[...]
```

### DIA 2 - TERÇA

```
[BUILDER continua 1.2...]

14:00 - BUILDER SUBMETE 1.2
[...]

14:20 - REVIEWER VALIDA 1.2
[...]

15:30 - REVIEWER RETORNA
Aprova 1.2

15:35 - VOCÊ APROVA 1.2
Marca DONE

15:40 - VOCÊ DISPARA 1.3 + 1.4
(Tarefas independentes!)
"Builder-A, faça 1.3"
"Builder-B, faça 1.4"
(ou mesmo Builder em sequência)

[...]
```

---

## 📊 Status do Fluxo - Template para Acompanhar

Crie arquivo `STATUS.md` no repo:

```markdown
# 📊 Status de Execução - [DATA]

## Hoje

| Tarefa | Status | Builder | Reviewer | Tempo | Notas |
|--------|--------|---------|----------|-------|-------|
| 1.1 | ✅ DONE | 1.75h | 1.25h | 3h | Sem problemas |
| 1.2 | 🟨 IN_PROGRESS | 1.5h | - | - | Próximo Reviewer |

## Resumo do Dia

- **Tarefas Completas**: 1/26 (4%)
- **Tempo Gasto**: 3h
- **Tempo Estimado**: 26h
- **Taxa de Rejeição**: 0%
- **Qualidade**: 100%
- **Ritmo**: ~1 tarefa/dia ✅

## Próximas Ações

- [ ] Tarefa 1.2 será revisada amanhã ~15h
- [ ] Após 1.2, iniciar 1.3 + 1.4 em paralelo
- [ ] Semana que vem iniciar FASE 2

## Observações

- Tudo correndo conforme planejado
- Builder e Reviewer calibrados bem
- Ritmo sustentável
```

---

## 🎯 Checklist de Disparo

Antes de disparar uma tarefa, confirme:

```
[ ] Tarefa está no TASKBOARD.md?
[ ] Dependências estão ✅ DONE?
[ ] Builder está disponível?
[ ] Contexto está claro?
[ ] Padrões foram comunicados?
[ ] Tempo estimado faz sentido?
[ ] Arquivo de STATUS.md vai ser atualizado?
[ ] Reviewer está pronto para receber?
```

---

## 🚨 Estados do Fluxo

### Tudo Normal ✅

```
Builder executa → Submete → Reviewer valida → Aprova → Próxima tarefa
```

### Builder Bloqueado 🔴

```
Builder: "Estou bloqueado em X"
   ↓
VOCÊ: [fornece contexto/decisão/referência]
   ↓
Builder: "Ah, agora entendi. Continuando..."
   ↓
[Fluxo continua]
```

### Reviewer Rejeita ⚠️

```
Reviewer: "Requer ajustes em X"
   ↓
VOCÊ: Comunica Builder
   ↓
Builder: "Refazendo..."
   ↓
Builder: Resubmete
   ↓
Reviewer: [nova revisão]
```

### Tarefas Independentes 🟨

```
Após tarefa 1.2 OK:

VOCÊ: "Fazer 1.3 + 1.4"
   ↓
Builder-A: 1.3 (paralelo)
Builder-B: 1.4 (paralelo)
   ↓
Ambos submetem
   ↓
Reviewer revisa ambos
   ↓
Você aprova ambos
```

---

## 📱 Como Monitorar Em Tempo Real

### Opção 1: Arquivo STATUS.md

Atualize a cada mudança:

```bash
# Editar STATUS.md conforme tarefas progridem
# Status = ⬜ → 🟨 → ⏳ → ✅
```

### Opção 2: Notas Rápidas

Mantenha arquivo `PROGRESS.txt`:

```
[09:00] Tarefa 1.1 disparada
[09:10] Builder começa
[10:55] Builder submete
[11:05] Você valida
[11:15] Reviewer começa
[12:35] Reviewer aprova ✅
[12:40] Tarefa 1.1: DONE
[12:45] Tarefa 1.2 disparada
[...]
```

### Opção 3: Chat em Tempo Real

Mantenha conversa aberta em VS Code:

```
👤 VOCÊ: "Builder, qual é o status de 1.1?"

👷 BUILDER: "Estou na FASE 3, implementação rodando bem. 
            Testes passando. Deve estar pronto em 30 min."

👤 VOCÊ: "Ótimo! Assim que submeter, encaminho para Reviewer."
```

---

## 💡 Dicas de Disparo

### ✅ BOM
```
"Próxima tarefa: 2.1 - Módulo de Carregamento PDF
 
 Objetivo: Ler e extrair texto de PDF usando pdfplumber
 
 Dependências: ✅ 1.1, 1.2, 1.3 concluídas
 
 Padrão: Use estrutura src/core/ conforme tarefa 2.0 (já existe)
 
 Tempo: ~2h
 
 Pronto?"
```

### ❌ RUIM
```
"Faça próxima tarefa"
```

### ✅ BOM
```
"Se tiver dúvida, pergunte antes de começar.
 Melhor esclarecer cedo que refazer depois."
```

### ❌ RUIM
```
"Resolve rápido"
```

---

## 🎬 Exemplo Completo - Primeira Semana

```
SEGUNDA:
09:00 - Dispara 1.1
11:00 - Builder submete
12:30 - Reviewer aprova
12:45 - Dispara 1.2

TERÇA:
09:00 - 1.2 em progresso
14:00 - Builder submete
15:30 - Reviewer aprova
15:45 - Dispara 1.3 + 1.4

QUARTA:
09:00 - 1.3 + 1.4 em progresso
11:00 - Ambos submetem
11:45 - Ambos aprovados
12:00 - FASE 1 COMPLETA! 🎉
12:15 - Dispara 2.1

QUINTA:
09:00 - 2.1 em progresso
11:00 - Builder submete
12:00 - Reviewer aprova
12:15 - Dispara 2.2

SEXTA:
09:00 - 2.2 em progresso
11:30 - Builder submete
12:30 - Reviewer aprova
13:00 - Review semanal
13:30 - Planejamento próxima semana

RESUMO SEMANA 1:
- ✅ Tarefas: 1.1, 1.2, 1.3, 1.4, 2.1, 2.2 = 6/26
- ✅ Tempo: ~12h
- ✅ Taxa rejeição: 0%
- ✅ Qualidade: 100%
- 📈 Próxima semana: FASE 2 + FASE 3
```

---

## 🎯 Sua Checklist de Dispatcher

### Por Tarefa
- [ ] Disparei tarefa?
- [ ] Builder começou?
- [ ] Acompanhei progresso?
- [ ] Builder submeteu?
- [ ] Validei rapidamente?
- [ ] Encaminhei para Reviewer?
- [ ] Reviewer validou?
- [ ] Aprovei?
- [ ] Atualizei STATUS?
- [ ] Próxima tarefa pronta?

### Por Dia
- [ ] Comecei com planejamento
- [ ] Disparei tarefas
- [ ] Monitorei execução
- [ ] Atualizei STATUS.md
- [ ] Reportei bloqueadores
- [ ] Tomei decisões
- [ ] Documentei progresso

### Por Semana
- [ ] Completi tarefas planejadas?
- [ ] Ritmo está sustentável?
- [ ] Qualidade está ok?
- [ ] Devo paralelizar mais?
- [ ] Agentes estão alinhados?
- [ ] Aprendi algo novo?
- [ ] Próxima semana planejada?

---

**Tudo pronto para disparar! 🚀 Comece com Tarefa 1.1 quando estiver pronto!**

