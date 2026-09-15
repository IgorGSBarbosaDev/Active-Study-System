---
name: assess-topic
description: Avalia o domínio real de um tópico já estudado no Active Study System e registra evidências de nível e status. Não use para ensinar, revisar conteúdo programado ou criar um tópico.
---

# Assess Topic

Meça o que o usuário consegue explicar e aplicar com autonomia. Use `99_SYSTEM/LEARNING_METHOD.md` como autoridade pedagógica; durante a tentativa, atue como avaliador e não como professor.

## Preparação

1. Leia `99_SYSTEM/LEARNING_METHOD.md`, `99_SYSTEM/TEMPLATES/topic.md` e `99_SYSTEM/TEMPLATES/questions.md`.
2. Normalize o nome solicitado apenas durante a pesquisa: compare sem distinguir maiúsculas, acentos ou pontuação e procure títulos, nomes de pastas, aliases e links no Vault.
3. Avalie somente um tópico existente com seu arquivo principal. Se não houver correspondência, informe que falta um tópico estudado e direcione o usuário para `study-topic`; não crie arquivos. Se houver mais de uma correspondência plausível, mostre as candidatas e peça que o usuário escolha.
4. Leia o arquivo principal e `Perguntas sobre {{TOPIC}}.md`. Considere conteúdo central, histórico, gaps, erros, datas, status, nível e evidências anteriores. Consulte as entradas do tópico em `02_REVIEWS/REVIEW_LOG.md` quando precisar verificar evidência autônoma em outra data.
5. Preserve todo conteúdo válido. Texto entre `<!-- USER-NOTES:START -->` e `<!-- USER-NOTES:END -->` é propriedade do usuário e nunca pode ser substituído, movido, normalizado ou reorganizado.

## Delimitação

Determine qual decisão a avaliação precisa sustentar: medir o nível atual, verificar uma dimensão específica ou examinar possível consolidação. Pergunte somente pelo que não estiver claro no pedido ou no estado registrado.

Selecione o menor conjunto suficiente de questões de alto valor, normalmente entre duas e quatro. Cubra dimensões diferentes sem transformar a sessão em uma bateria:

- nível baixo: conceito, definição e funcionamento;
- nível intermediário: explicação com palavras próprias e aplicação;
- nível alto: diagnóstico de erro, comparação de alternativas, decisões, trade-offs e transferência para outro cenário.

Use o nível existente como ponto de partida, não como conclusão. Priorize conceitos centrais e gaps capazes de alterar a classificação.

## Condução

1. Apresente uma questão ou tarefa por vez e espere a resposta sem consulta.
2. Não ensine antes da tentativa, não dê pistas que entreguem a resposta e não revele se cada resposta está correta enquanto isso puder influenciar as próximas.
3. Faça apenas esclarecimentos neutros sobre o enunciado. Não complete o raciocínio do usuário.
4. Adapte a próxima questão à evidência já obtida ou encerre uma dimensão quando ela estiver demonstrada. Não repita perguntas equivalentes.
5. Encerre assim que houver evidência confiável para a decisão proposta; não prolongue a avaliação para buscar exaustividade.

Depois de concluir o bloco avaliativo, apresente feedback consolidado. Separe o que foi demonstrado com autonomia, o que ficou incompleto ou dependeu de ajuda, os gaps e erros relevantes, o nível e status resultantes e o que ainda impede progressão. Correções e explicações pertencem a esse feedback posterior, nunca à tentativa avaliada.

Se o usuário quiser aprender os pontos ausentes depois do feedback, encerre a avaliação e encaminhe o aprofundamento para `study-topic`. Não converta silenciosamente a avaliação em aula ou revisão.

## Classificação

Use somente `Não iniciado`, `Estudando`, `Praticando` ou `Consolidado` em `Status`. Mantenha `Status` e `Nível` independentes e altere ambos somente a partir de evidência observada.

Classifique `Nível` assim:

- `0` — não compreendeu;
- `1` — reconhece;
- `2` — entende com ajuda;
- `3` — explica corretamente;
- `4` — aplica corretamente;
- `5` — analisa trade-offs, diagnostica problemas e lida com casos não óbvios.

Não aumente o nível por respostas assistidas, reconhecimento ou conteúdo apenas apresentado. Se a evidência contradisser o nível ou status existente, registre o gap e reclassifique o tópico.

Para marcar `Consolidado`, exija cumulativamente:

- desempenho autônomo na avaliação atual;
- evidência autônoma compatível registrada em outra sessão e outra data;
- explicação dos conceitos centrais, aplicação e análise relevante ao tópico.

Uma única avaliação pode elevar o nível numérico, mas não comprova consolidação. Se faltar evidência longitudinal, mantenha no máximo `Praticando` e informe explicitamente o que falta.

## Persistência

No arquivo `Perguntas sobre {{TOPIC}}.md`, use ou crie ao final a seção `## Avaliações` sem mover as seções existentes. Acrescente um bloco compacto e datado:

```markdown
### YYYY-MM-DD — Avaliação

- Objetivo: decisão avaliada e nível inicial.
- Questões: síntese das tarefas de alto valor usadas.
- Evidências autônomas: o que foi explicado, aplicado ou diagnosticado sem ajuda.
- Gaps e erros: pontos relevantes observados.
- Resultado: nível, status e evidência ainda necessária para progressão.
```

Não transcreva a conversa nem registre respostas irrelevantes.

Atualize o arquivo principal sem apagar conteúdo válido:

- mantenha em `## Gaps` os gaps relevantes ainda abertos;
- registre em `## Erros` erros relevantes, sua causa observada e o modelo correto apresentado no feedback final;
- atualize `Nível` e `Status` somente conforme a evidência;
- não altere `Data criação`, `Data último estudo`, `Data última revisão` ou `Data próxima revisão`;
- não altere `## Conteúdo` nem o bloco `USER-NOTES`.

Não altere `02_REVIEWS/REVIEWS.md` ou `02_REVIEWS/REVIEW_LOG.md`. A avaliação não conta como revisão espaçada.

Ao terminar, informe sucintamente as evidências autônomas, gaps, nível, status, bloqueios de progressão e arquivos atualizados.

## Limites

- Não crie tópicos, não conduza revisão programada e não ensine durante a tentativa.
- Não altere templates, `LEARNING_METHOD.md`, arquivos de `99_SYSTEM/METHOD`, `99_SYSTEM/STRATEGY` ou notas fora do tópico avaliado.
- Não confunda bom desempenho pontual com retenção longitudinal.
