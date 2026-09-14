---
name: study-topic
description: Conduz uma sessão ativa quando o usuário quer estudar ou aprender um tópico, diagnosticando antes de ensinar e persistindo progresso no Active Study System. Não use para uma revisão ou avaliação isolada.
---

# Study Topic

Conduza uma sessão de estudo ativa e mantenha o estado durável do tópico no Vault. Use `99_SYSTEM/LEARNING_METHOD.md` como autoridade pedagógica; não replique suas explicações.

## Preparação

1. Leia `99_SYSTEM/LEARNING_METHOD.md` e os templates `99_SYSTEM/TEMPLATES/topic.md` e `99_SYSTEM/TEMPLATES/questions.md`.
2. Extraia e normalize o nome solicitado apenas para pesquisa. Compare sem distinguir maiúsculas, acentos ou pontuação e procure títulos, nomes de pastas, aliases e links em todo o Vault.
3. Se uma correspondência for inequívoca, reutilize-a. Se houver mais de uma correspondência plausível, mostre as candidatas e peça ao usuário que escolha. Não crie duplicata enquanto houver ambiguidade.
4. Se o tópico for novo, crie `01_TOPICS/{{TOPIC}}/{{TOPIC}}.md` e `01_TOPICS/{{TOPIC}}/Perguntas sobre {{TOPIC}}.md` a partir dos templates e substitua `{{TOPIC}}` pelo nome apresentado ao usuário. Preserve um nome legível e remova somente caracteres inválidos para arquivos do Windows. Use datas ISO `YYYY-MM-DD`, defina `Status: Não iniciado` e `Nível: 0` e deixe datas ainda não ocorridas vazias.
5. Se existir, leia os dois arquivos e considere conteúdo, histórico, gaps, erros, datas, status e nível. Se apenas um arquivo do par existir, preserve-o e crie somente o ausente a partir do template correspondente. Texto entre `<!-- USER-NOTES:START -->` e `<!-- USER-NOTES:END -->` é propriedade do usuário: nunca o substitua, mova, normalize ou reorganize.

Pesquisa externa não é obrigatória. Quando for necessária para corrigir ou ensinar conteúdo técnico com segurança, priorize documentação oficial, especificações e outras fontes primárias.

## Delimitação da sessão

Determine o objetivo do estudo, por que ele importa agora e o tempo disponível. Pergunte apenas pelo que não estiver claro no pedido ou no estado do tópico. Restrinja a sessão a um tópico e reduza o objetivo se ele não couber no tempo disponível.

Antes de ensinar, registre em `Perguntas sobre {{TOPIC}}.md`, sob `## Diagnóstico inicial`, as perguntas usadas, uma síntese das respostas e a avaliação inicial. Use registros compactos; não transcreva toda a conversa.

## Condução

Alterne entre dois papéis, nesta ordem:

1. **Avaliador:** proponha uma pergunta, explicação ou exercício sem consulta e espere a tentativa do usuário.
2. **Professor:** classifique a tentativa como correta, parcial, incorreta ou sem base; explicite acertos, gaps e a origem provável do erro; ensine somente o necessário para corrigir ou ampliar o modelo.
3. **Avaliador:** teste a mudança com recuperação, explicação própria ou uma variação semelhante.

Faça uma pergunta ou exercício por vez. Não revele a resposta antes da tentativa. Se o usuário declarar não possuir base suficiente, apresente somente a base mínima e solicite recuperação logo depois.

Adapte a próxima pergunta à evidência observada. Priorize gaps e erros relevantes; não acumule perguntas predeterminadas quando a resposta alterar o caminho. Antes de avançar para outra parte do tópico, exija uma explicação ou aplicação sem pistas.

Quando pertinente ao tópico, avance gradualmente por teoria, exemplo mínimo, aplicação, testes, provocação de falhas, diagnóstico e trade-offs. Não force etapas técnicas que não façam sentido. Use analogias ou diagramas para tornar relações explícitas, nunca como substitutos da recuperação e da aplicação.

Registre em `## Perguntas adaptativas` somente as perguntas relevantes, uma síntese das tentativas, o feedback decisivo e o resultado da nova tentativa. Um erro relevante deve registrar o raciocínio incorreto e a correção verificada, não apenas `errado`.

## Encerramento e persistência

Encerre quando o objetivo couber na evidência obtida ou o tempo disponível terminar. Não declare domínio para concluir artificialmente a sessão.

Atualize `Perguntas sobre {{TOPIC}}.md`:

- `## Resultado`: evidências do que o usuário conseguiu explicar ou aplicar, indicando a assistência necessária;
- `## Gaps identificados`: gaps ainda abertos e erros que devem ser recuperados depois.

Atualize `{{TOPIC}}.md` sem apagar conteúdo válido:

- `## Conteúdo`: conhecimento confirmado ou corrigido na sessão;
- `## Gaps`: gaps relevantes ainda abertos;
- `## Erros`: erros relevantes, sua causa e o modelo corrigido;
- preserve integralmente `## Minhas anotações` e o bloco `USER-NOTES`.

Regras dos campos:

- defina `Data criação` somente ao criar o tópico;
- ao concluir estudo ou aprofundamento, defina `Data último estudo` como a data atual;
- não altere `Data última revisão`, reservada a uma futura Skill de revisão;
- após uma sessão com conhecimento novo ou gaps relevantes, defina `Data próxima revisão` como a data atual mais um dia (`D+1`); alterações secundárias não reiniciam a revisão;
- use somente `Não iniciado`, `Estudando`, `Praticando` ou `Consolidado` em `Status`;
- mantenha `Status` e `Nível` independentes: status representa a fase do tópico, nível representa domínio observado.

Classifique `Nível` somente por evidência observada:

- `0` — não compreendeu;
- `1` — reconhece;
- `2` — entende com ajuda;
- `3` — explica corretamente;
- `4` — aplica corretamente;
- `5` — analisa trade-offs, diagnostica problemas e lida com casos não óbvios.

Não aumente o nível por conteúdo apenas apresentado. Se o desempenho contradisser o nível existente, registre o gap e ajuste-o à evidência atual.

Ao terminar, informe sucintamente o objetivo coberto, o status, o nível resultante, os principais gaps, a próxima revisão e os arquivos atualizados.

## Limites

- Não execute uma revisão ou avaliação independente; apenas deixe dados úteis para futuras Skills `reviews` e `assess-topic`.
- Não altere templates, arquivos de `99_SYSTEM/METHOD`, `99_SYSTEM/STRATEGY` ou notas fora do tópico em estudo.
- Não trate releitura, resposta assistida ou conclusão de uma única sessão como consolidação.
