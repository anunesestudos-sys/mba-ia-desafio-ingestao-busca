# Orchestrator Guide - Seu Manual de Coordenação

## 🎯 Sua Missão

Você é o maestro deste fluxo. Sua responsabilidade é:

1. **Coordenar** o fluxo Builder → Reviewer
2. **Tomar decisões** arquiteturais
3. **Remover bloqueadores**
4. **Validar qualidade** (visão geral)
5. **Manter ritmo** sustentável
6. **Documentar** progresso
7. **Otimizar** processo conforme aprende

---

## 📋 Ciclo Diário Recomendado

### MANHÃ (15-30 min)

```
1. PLANEJAMENTO DO DIA
   [ ] Abra TASKBOARD.md
   [ ] Identifique próxima tarefa não feita
   [ ] Verifique dependências
   [ ] Verifique se Builder está disponível

2. BRIEFING COM BUILDER (10 min)
   Comunique:
   - Qual tarefa executar (ID e nome)
   - Por quê é importante (contexto PRD)
   - Dependências que devem estar prontas
   - Padrões/patterns existentes
   - Prazos de entrega esperados
   
   Exemplo:
   "Builder, agora você vai fazer tarefa 2.1.
    É o módulo de carregamento de PDF.
    Depende da 1.1 que está pronta.
    Use pdfplumber se achar melhor.
    Esperamos ~2 horas.
    Aqui está o contexto: [links para TASKBOARD, PRD]"

3. REVISOR DISPONÍVEL?
   - Comunique ao Reviewer que uma tarefa está em progresso
   - Se Reviewer está ocupado, pode paralelizar com Builder diferente
```

### TARDE (10-20 min)

```
1. BUILDER SUBMETE
   [ ] Receba submissão do Builder
   [ ] Valide que template foi preenchido
   [ ] Leia rapidamente se funcionalidade faz sentido
   [ ] Se parecer errado, peça esclarecimento

2. ENVIE PARA REVIEWER
   [ ] Reencaminhe submissão para Reviewer
   [ ] Comunique: "Pronto para revisão: Tarefa [ID]"
   [ ] Reviewer começa validação
   
3. PROXIMA TAREFA?
   [ ] Se há tarefas independentes, inicie nova com Builder/3
   [ ] Caso contrário, fique atento ao feedback do Reviewer
```

### FIM DO DIA (10 min)

```
1. FEEDBACK DO REVIEWER
   [ ] Receba feedback completo
   [ ] Se APROVADO: marca ✅ no TASKBOARD
   [ ] Se REQUER AJUSTES: comunica Builder para refazer
   [ ] Se REJEITA: conversa sobre o que fazer

2. ATUALIZAR PROGRESSO
   [ ] Update no README ou arquivo de status
   [ ] Documente métricas: tarefas feitas, tempo, qualidade

3. PLANEJAMENTO AMANHÃ
   [ ] Defina próxima tarefa ou sequência
   [ ] Identifique possível paralelização
```

---

## 🔄 Estados das Tarefas

Acompanhe no TASKBOARD.md:

```
⬜ TODO          = Não iniciada, ou bloqueada por dependência
🟨 IN_PROGRESS   = Builder trabalhando
⏳ IN_REVIEW     = Reviewer validando (você pode fazer outra coisa)
🔄 NEEDS_FIX     = Requer ajustes, Builder refazendo
✅ DONE          = Aprovada e pronta para próxima fase
```

### Template de Atualização

```markdown
## Status de Execução

### FASE 1: Setup & Infraestrutura (3h)
- [x] 1.1 - Fork e Setup: ✅ DONE (2h)
- [x] 1.2 - PostgreSQL: ✅ DONE (1.5h)
- [🟨] 1.3 - Modelo Embeddings: 🟨 IN_PROGRESS (Builder trabalhando)
- [ ] 1.4 - LLM Selection: ⬜ TODO (aguardando 1.3)

**Tempo Total Gasto**: 3.5h  
**Progresso**: 2/4 tarefas FASE 1  
**Qualidade**: 100% aprovadas  
**Próxima Revisão**: 1.3 amanhã às 15h
```

---

## 🎯 Tipos de Decisão que Você Toma

### ARQUITETURA & DESIGN

```
Exemplo 1:
BUILDER: "Qual tecnologia usar: SqlAlchemy ou Raw SQL?"
VOCÊ: "Use Raw SQL com psycopg3 para este projeto 
       (simplicidade, controle direto). 
       Pense em migrations com alembic."

Exemplo 2:
BUILDER: "Devo cachear embeddings computados?"
VOCÊ: "Sim, recomendo Redis in-memory para sessão,
       ou arquivo JSON local."
```

### PRIORIZAÇÃO & SEQUÊNCIA

```
Quando Builder termina tarefa e pede próxima:

VOCÊ analisa:
- [ ] Quais tarefas dependem desta?
- [ ] Quais tarefas são independentes?
- [ ] O que maximiza paralelização?
- [ ] O que desbloqueia outras coisas?

Decisão: "Faça 3.2 depois. Enquanto isso, 
         Builder-2 pode fazer 4.1 em paralelo."
```

### QUALIDADE & RETRABALHO

```
Quando Reviewer rejeita ou pede ajustes:

Você decide:
- [ ] Isso é crítico? (requer refazer tudo)
- [ ] Isso é ajuste? (10-20% tempo Builder)
- [ ] Isso é pattern learning? (comunicar para futuro)

Comunicado ao Builder:
"Revisor solicita [ajuste X].
 Severidade é BAIXA.
 Refaça em 30 min, pronto?"
```

### TIMING & RITMO

```
Você monitora:
- [ ] Velocidade: ~2 tarefas/dia é sustentável?
- [ ] Qualidade: Taxa de rejeição está ok?
- [ ] Fadiga: Builder está cansado? Precisa break?

Decisão: "Vamos reduzir para 1 tarefa/dia, 
         focando em qualidade. 
         Tempo de revisão está muito alto."
```

---

## 🚀 Sessão Exemplo: Primeira Semana

### DIA 1 - Segunda (Tarde)

```
14:00 - BRIEFING BUILDER
"Vamos começar com tarefa 1.1 - Fork e Setup.
 Clonar o repo que está aqui, configurar venv, testes rodam.
 É curto, deve levar ~1.5 horas.
 Use pdfplumber para PDF, até confirm qual embedding model."

16:00 - BUILDER SUBMETE
✅ Tarefa 1.1 - Fork e Setup
   - Repo clonado
   - venv configurado
   - pytest passa
   - README atualizado
   Tempo: 1h 45min

16:10 - VOCÊ VALIDA RÁPIDO
"Perfeito, deixa pronto para revisão"

16:20 - REVIEWER COMEÇA
🔍 Revisão de Tarefa 1.1

17:00 - REVIEWER RETORNA
✅ APROVADO
   Pontos positivos: setup limpo, bem documentado
   Nenhum ajuste necessário
   Pronto para 1.2

17:05 - VOCÊ MARCA DONE
[ x] 1.1: ✅ DONE

17:10 - INICIA 1.2
"Builder, agora 1.2 - PostgreSQL + pgVector
 Setup local ou cloud. Precisa migrations rodar ok."
```

### DIA 2 - Terça

```
09:00 - BUILDER AINDA TRABALHANDO em 1.2
 (DB setup é mais complexo que tarefa curta)
 
 Você pode:
 - Trabalhar em documentação de design
 - Preparar tarefas futuras
 - Revisar código existente do fork

11:00 - BUILDER SUBMETE 1.2
⚠️ Tarefa 1.2 - PostgreSQL
   Setup ok, migrations rodam
   Mas... "Tive dúvida em credenciais, 
   deixei hard-coded em config.py"

11:15 - VOCÊ CONVERSA
"Ah, boa catch. Reviewer vai reclama disso.
 Refaz usando variáveis de ambiente?
 Deve levar 15 min."

11:30 - BUILDER REFAZ
✅ Resubmete com env vars

11:45 - REVIEWER APROVA
✅ APROVADO com ajuste pequeno

12:00 - VOCÊ MARCA DONE
[ x] 1.2: ✅ DONE

12:05 - INICIA 1.3 + 1.4 EM PARALELO
"Builder-A: tarefa 1.3 - Modelo Embeddings  
 Builder-B: tarefa 1.4 - LLM Selection
 Ambas independentes, 1h cada aprox.
 Vocês podem trabalhar em paralelo!"
 
 (ou se só tem 1 Builder)
 
 "Builder: dá pra fazer 1.3 e 1.4 em sequência?
  Deve dar ~2h total."
```

### DIA 3 - Quarta

```
09:00 - BUILDER TERMINA 1.3 E 1.4
✅ Tarefa 1.3 - Modelo Embeddings
   Escolheu: sentence-transformers + MiniLM
   Testes de similaridade ok
   Tempo: 1h 15min

✅ Tarefa 1.4 - LLM Selection
   Escolheu: OpenAI GPT-4 + fallback 3.5
   Documentado porque selecionou
   Tempo: 45min

10:30 - REVIEWER APROVA AMBAS
✅ AMBAS APROVADAS

11:00 - VOCÊ MARCA FASE 1 COMPLETA
✅ FASE 1: Setup & Infraestrutura
   [x] 1.1: ✅ DONE (1h 45min)
   [x] 1.2: ✅ DONE (1h 30min)
   [x] 1.3: ✅ DONE (1h 15min)
   [x] 1.4: ✅ DONE (45min)
   
   **Total FASE 1**: 5h 15min (vs 3h planejado)
   **Qualidade**: 100% aprovadas (1 ajuste menor)
   **Ritmo**: Bom! Sem pressa, bem feito.

11:30 - INICIA FASE 2
"Builder, agora começamos FASE 2 - Módulo de Ingestão.
 Próxima tarefa é 2.1 - Módulo de Carregamento PDF.
 Você conhece pdfplumber já. Deve levar ~2h.
 Vamos começar?"
```

---

## 📊 Métricas para Acompanhar

### Por Tarefa

```
- Tempo planejado vs realizado
- Status: ⬜ → 🟨 → 🔄/✅ (rejeições)
- Taxa de rejeição: quantas vezes foi rejeitada?
- Tempo de revisão: quanto o Reviewer levou?
```

### Por Fase

```
- Progresso: X/Y tarefas completas
- Tempo acumulado
- Taxa média de rejeição
- Qualidade média de testes
```

### Por Projeto

```
# Status Geral

| Métrica | Valor |
|---------|-------|
| Tarefas Completas | 4/26 (15%) |
| Tempo Total | 5.5h / 26h estimado (21%) |
| Taxa de Rejeição | 5% (1 ajuste) |
| Cobertura Testes | 92% média |
| Ritmo | 1.5 tarefas/dia |
| Próximo Milestone | FASE 1 completa ✅ |
```

---

## 🎯 Checklist de Orquestrador

### DIÁRIO

- [ ] Revisou TASKBOARD.md pela manhã
- [ ] Definiu próxima tarefa com Builder
- [ ] Acompanhava progresso Builder
- [ ] Recebeu submissão Builder
- [ ] Validou rapidamente funcionalidade
- [ ] Encaminhou para Reviewer
- [ ] Recebeu feedback Reviewer
- [ ] Tomou decisão: aprova/rejeita/ajusta
- [ ] Marcou status no TASKBOARD
- [ ] Atualizou progresso em algum lugar visível

### SEMANAL

- [ ] Revisou métricas gerais
- [ ] Avaliou ritmo (rápido/lento demais?)
- [ ] Conversou com Builder: feedback, dificuldades
- [ ] Conversou com Reviewer: calibração critério
- [ ] Otimizou sequência se necessário
- [ ] Documentou lessons learned
- [ ] Planejou próxima semana

### MENSAL

- [ ] Revisou projeto completo
- [ ] Validou compliance com PRD
- [ ] Avaliou qualidade geral
- [ ] Planejou melhorias no processo
- [ ] Celebrou progresso! 🎉

---

## 💬 Scripts de Comunicação

### Quando Inicia Tarefa

```
"Builder, próxima tarefa: [ID] - [Nome]

Objetivo: [descrição breve do que fazer]

Contexto: [por quê é importante]

Dependências: ✅ [lista de tarefas que devem estar prontas]

Padrões/Referências:
- Use [padrão X] conforme visto em [tarefa Y]
- Evite [anti-pattern Z]

Tempo esperado: ~[N] horas

Pronto para começar?"
```

### Quando Recebe Submissão

```
"Obrigado pela submissão, Builder!
 
 Vou validar rapidamente:
 ✅ Funcionalidade faz sentido
 ✅ Commits estão bem documentados
 ✅ Testes inclusos
 
 Encaminhando para Reviewer agora.
 Esperamos feedback até [horário]."
```

### Quando Aprovado

```
"🎉 Tarefa [ID] APROVADA!

 Reviewer deu feedback positivo:
 - [ponto positivo 1]
 - [ponto positivo 2]
 
 Marcando como ✅ DONE no TASKBOARD.
 
 Próxima tarefa: [ID] - [Nome]
 Mesmo ritmo? Quer começar logo?"
```

### Quando Requer Ajustes

```
"Tarefa [ID] requer pequenos ajustes.

 Reviewer solicitou:
 1. [ajuste 1] - severidade BAIXA (~15 min)
 2. [ajuste 2] - severidade BAIXA (~10 min)
 
 Não é nada crítico. Consegue refazer
 hoje ainda? Depois resubmete."
```

### Quando Rejeitada

```
"Tarefa [ID] não está pronta ainda.

 Reviewer identificou:
 - [problema 1 - crítico]
 - [problema 2 - crítico]
 
 Precisa de trabalho adicional.
 
 Vamos conversar:
 - Está ok com o escopo?
 - Precisa ajuda/contexto?
 - Quanto tempo estima para refazer?"
```

---

## 🚨 Quando Intervir

### Você DEVE intervir quando:

```
❌ Builder está completamente bloqueado
   → Ajude com contexto/decisão

❌ Builder e Reviewer discordam
   → Mediar e decidir

❌ Ritmo está sustentável?
   → Ajustar carga

❌ Qualidade caindo
   → Conversar com Reviewer sobre critério

❌ Dívida técnica aparecendo
   → Ajuste plano futuro

❌ Arquitetura não faz sentido
   → Intervenha antes de prosseguir

❌ Motivação está baixa
   → Acompanhe, ajude, celebre vitórias
```

### Você NÃO deve intervir quando:

```
✅ Builder resolvendo problema sozinho
   → Deixe aprender

✅ Reviewer fazendo seu trabalho
   → Não interfira na revisão

✅ Ritmo está bom
   → Não mude o que funciona

✅ Qualidade é boa
   → Confie no Reviewer
```

---

## 📈 Como Otimizar o Processo

### Semana 1-2: Calibrar

```
- Aprenda o ritmo natural
- Calibre critério Reviewer
- Documente patterns
- Identifique bloqueadores comuns
```

### Semana 3+: Otimizar

```
1. PARALELIZAÇÃO
   - Identifique tarefas independentes
   - Use múltiplos Builders se possível
   
2. TEMPLATES
   - Crie templates para tipos de tarefa
   - Reducer tempo de briefing
   
3. AUTOMATION
   - Linting automático?
   - Testes automáticos?
   
4. COMUNICAÇÃO
   - Padronize templates de feedback
   - Crie atalhos de comunicação
```

---

## 🎓 Você Como Especialista

Você não é só orquestrador, mas especialista técnico. Use seu conhecimento para:

```
✅ Validar decisões arquiteturais do Builder
✅ Sugerir padrões quando solicitado
✅ Esclarecer requisitos PRD
✅ Resolver conflitos técnicos Builder vs Reviewer
✅ Orientar sobre best practices
✅ Calibrar critério de qualidade Reviewer
```

Exemplo:

```
REVIEWER: "Builder usou string concatenation 
           para montar SQL. Rejeito?"

VOCÊ: "Não, pode aprovar. Para este projeto
       é apropriado (queries simples, não dinâmicas).
       Se fosse queries complexas, sim, ParameterizedQuery.
       Deixa um TODO para futuro."

REVIEWER: "Ah, entendi. ✅ APROVADO com TODO adicionado."
```

---

## 🏁 Marcos do Projeto

Celebre quando atingir:

```
✅ FASE 1 COMPLETA (Setup)
   Reunião rápida: o que aprendemos?

✅ FASE 2 COMPLETA (Ingestão)
   Primeira pipeline de PDF funcionando!

✅ FASE 3 COMPLETA (Consulta)
   Sistema RAG completo conversando!

✅ FASE 4 COMPLETA (Testes)
   Produto pronto para usar!

✅ FASE 5 COMPLETA (Documentação)
   Projeto entregue! 🎉

🎊 PROJETO CONCLUÍDO
```

---

**Você é o maestro. Coordene com maestria, lidere com confiança, e entregue excelência!** 🎯

Agora: Quer começar com tarefa 1.1?
