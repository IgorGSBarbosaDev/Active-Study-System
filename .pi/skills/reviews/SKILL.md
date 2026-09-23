---
name: reviews
description: Consulta a agenda ou conduz revisão espaçada de tópicos existentes, priorizando recuperação autônoma, gaps e erros. Não use para tópico novo ou avaliação formal.
---

# Reviews

Consulte ou conduza revisões segundo `99_SYSTEM/LEARNING_METHOD.md`.

## Preparação e consulta

Leia os tópicos em `01_TOPICS`, `02_REVIEWS/REVIEWS.md` e `02_REVIEWS/REVIEW_LOG.md`. Para uma sessão, leia também o arquivo principal e `Perguntas sobre <TOPIC>.md`.

Se o pedido for somente consultar agenda ou datas, responda a partir do estado atual e encerre: não faça recuperação, não altere tópicos, não registre log e não sincronize arquivos. Informe datas inválidas encontradas.

Uma revisão explícita pode ocorrer sem data programada ou antes da data prevista.

## Sessão

1. Defina foco curto a partir dos gaps, erros e conceitos centrais necessários.
2. Escolha o menor conjunto capaz de produzir evidência útil.
3. Peça uma recuperação, explicação ou aplicação sem consulta e aguarde a tentativa; faça uma solicitação por vez.
4. Em erro pontual, ensine somente a correção necessária e use uma variação curta para verificar a mudança. Se a tentativa mostrar que o mecanismo básico não foi compreendido, registre o gap e, após encerrar a revisão, ofereça aprofundamento com `study-topic`.
5. Encerre pontos demonstrados com autonomia e pare quando as prioridades estiverem evidenciadas ou os gaps localizados.

Não transforme revisão em aula completa ou avaliação formal. Direcione conteúdo novo para `study-topic` e medição formal para `assess-topic`.

## Agendamento

Infira o estágio nesta ordem:

1. transição mais recente do tópico em `REVIEW_LOG.md`;
2. diferença entre `Data próxima revisão` e `Data última revisão`;
3. na primeira revisão, diferença entre `Data próxima revisão` e `Data último estudo`.

Na data prevista ou depois dela:

- sucesso autônomo avança um estágio;
- gap relevante reinicia em D+1;
- evidência insuficiente sem gap relevante repete o estágio;
- sucesso em D+30 mantém D+30.

Calcule a próxima data a partir da sessão. Se o estágio for indeterminado, use D+1 e registre o fallback. Em revisão antecipada, atualize a evidência e `Data última revisão`, mas não avance nem adie a data existente; gap relevante substitui a próxima data por D+1. Sem data ou estágio conhecido, use D+1.

## Persistência

No tópico, atualize somente `Data última revisão`, `Data próxima revisão`, gaps, erros e, quando a evidência justificar, `Status` e `Nível`. Não altere `Data criação`, `Data último estudo`, `## Conteúdo` ou o arquivo de perguntas.

Acrescente ao `REVIEW_LOG.md` uma entrada compacta com data, tópico, resultado, evidências autônomas, assistência, gaps/erros e transição do intervalo. Não transcreva a conversa. `Consolidado` continua exigindo evidência compatível em outra data.

Informe resultado, gaps, estado, intervalo e próxima revisão. Sincronize as visões derivadas pelo procedimento global do `AGENTS.md`.
