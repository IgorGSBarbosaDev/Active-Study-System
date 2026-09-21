---
name: assess-topic
description: Mede formalmente o domínio autônomo de um tópico existente e registra evidências de nível e status. Não use para ensinar, revisar ou criar um tópico novo.
---

# Assess Topic

Meça o que o usuário explica e aplica sem assistência. Use `99_SYSTEM/LEARNING_METHOD.md` como autoridade e não ensine durante a tentativa.

## Preparação

Localize somente tópico com arquivo principal existente. Se não existir, direcione para `study-topic`. Leia o tópico, perguntas e, quando necessário para evidência longitudinal, entradas em `02_REVIEWS/REVIEW_LOG.md`.

Se `Perguntas sobre <TOPIC>.md` estiver ausente, repare somente esse arquivo a partir de `99_SYSTEM/TEMPLATES/questions.md`; isso não autoriza criar ou modificar o tópico principal.

Determine a decisão: nível atual, dimensão específica ou possível consolidação. Selecione normalmente duas a quatro tarefas de alto valor, ajustadas ao nível registrado e aos gaps:

- conceito e funcionamento em níveis baixos;
- explicação e aplicação em níveis intermediários;
- diagnóstico, alternativas, trade-offs e transferência em níveis altos.

## Bloco avaliativo

1. Apresente uma tarefa por vez e aguarde resposta sem consulta.
2. Não dê pistas, correções, respostas nem confirmação de acerto que influencie as próximas tarefas.
3. Esclareça apenas o enunciado de forma neutra.
4. Adapte ou encerre uma dimensão quando houver evidência confiável; não repita equivalentes.
5. Pare assim que a decisão estiver sustentada.

Depois do bloco, dê feedback consolidado: evidências autônomas, dependências de ajuda, gaps, erros, `Nível`, `Status` e bloqueios de progressão. Se o usuário quiser aprender o que faltou, encerre a avaliação antes de encaminhar para `study-topic`.

Use a classificação de `LEARNING_METHOD.md`. `Consolidado` exige desempenho autônomo atual, evidência compatível em outra data e explicação, aplicação e análise relevantes; sem longitudinalidade, mantenha no máximo `Praticando`.

## Persistência

Acrescente em `## Avaliações` do arquivo de perguntas um bloco datado com objetivo, tarefas usadas, evidências autônomas, gaps/erros e resultado. No tópico principal, atualize somente gaps, erros, `Nível` e `Status` conforme a evidência.

Não altere conteúdo nem datas de estudo/revisão. A avaliação não conta como revisão espaçada e não modifica `REVIEWS.md` ou `REVIEW_LOG.md` diretamente.

Informe evidências, gaps, estado, bloqueios e arquivos alterados. Sincronize as visões derivadas pelo procedimento global do `AGENTS.md`.
