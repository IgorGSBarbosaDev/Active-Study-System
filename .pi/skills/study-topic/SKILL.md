---
name: study-topic
description: Ensina ou aprofunda um tópico por diagnóstico curto, blocos progressivos e verificação ativa, persistindo o progresso no Active Study System. Não use para revisão ou avaliação isolada.
---

# Study Topic

Conduza uma sessão de estudo ativa. Use `99_SYSTEM/LEARNING_METHOD.md` como autoridade pedagógica e os templates `topic.md` e `questions.md` para persistência.

## Preparação

Localize o tópico pelas regras do `AGENTS.md`. Se for novo, crie:

- `01_TOPICS/<TOPIC>/<TOPIC>.md` a partir de `99_SYSTEM/TEMPLATES/topic.md`;
- `01_TOPICS/<TOPIC>/Perguntas sobre <TOPIC>.md` a partir de `99_SYSTEM/TEMPLATES/questions.md`.

Preencha `Data criação`, `Status: Não iniciado` e `Nível: 0`; deixe datas futuras vazias. Se existir somente um arquivo do par, preserve-o e crie o ausente. Para tópico existente, leia os dois arquivos e use conteúdo, histórico, gaps, erros e estado como ponto de partida.

Pesquisa externa é opcional. Quando necessária para ensinar conteúdo atual ou sensível, priorize documentação oficial, especificações e fontes primárias.

## Sessão

Determine objetivo, motivo e tempo somente quando isso não estiver claro. Reduza o escopo se não couber na sessão.

Faça um diagnóstico mínimo: comece com uma solicitação ampla, esclareça apenas incertezas que mudem o ensino e pare assim que distinguir base demonstrada e gaps principais. Registre uma síntese em `## Diagnóstico inicial`; não transforme o diagnóstico em avaliação formal.

Escolha o percurso:

- com pouca base, ensine o fundamento indispensável em blocos curtos;
- com conhecimento prévio, pule o que já foi demonstrado e comece pelos gaps ou próximo passo relevante.

Depois de cada bloco relevante, peça uma explicação, aplicação ou verificação curta. Corrija a causa do erro, use no máximo uma variação focada e avance quando houver evidência suficiente. Faça uma solicitação por vez e não obrigue o usuário a descobrir conteúdo ainda não ensinado.

Antes de encerrar, faça uma verificação integradora breve. Persista o diagnóstico quando concluído e consolide o restante somente no encerramento.

## Persistência

Em `Perguntas sobre <TOPIC>.md`, atualize:

- `## Perguntas adaptativas`: verificações relevantes, síntese das tentativas e feedback decisivo;
- `## Resultado`: evidências e assistência necessária;
- `## Gaps identificados`: gaps ainda abertos.

No arquivo principal, atualize sem apagar conteúdo válido:

- `## Conteúdo`: conhecimento confirmado ou corrigido;
- `## Gaps`: gaps relevantes;
- `## Erros`: raciocínio incorreto, causa e correção verificada;
- `Data último estudo`: data atual;
- `Data próxima revisão`: D+1 quando houver conhecimento novo ou gap relevante;
- `Status` e `Nível`: conforme a evidência definida em `LEARNING_METHOD.md`.

Não altere `Data última revisão`. Não eleve nível por conteúdo apenas apresentado.

## Handoff e encerramento

Crie resumo somente se o usuário o pedir, usando `study-summary`. Não inicie exercícios automaticamente: quando houver base útil, ofereça `practice-set` e aguarde concordância, salvo se o pedido original já incluir prática.

Informe objetivo coberto, evidências, gaps, estado, próxima revisão e arquivos alterados. Sincronize as visões derivadas pelo procedimento global do `AGENTS.md`.

Não execute revisão ou avaliação independente e não altere estratégia, método, templates ou notas fora do tópico.
