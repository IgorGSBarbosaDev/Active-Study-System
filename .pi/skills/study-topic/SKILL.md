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

Faça um diagnóstico breve para localizar o ponto de partida, não para medir todo o domínio. Comece com uma solicitação ampla que permita ao usuário mostrar o que sabe. Faça somente as perguntas adicionais necessárias para resolver dúvidas que mudem o ensino, sem quantidade fixa. Encerre o diagnóstico assim que distinguir conhecimento demonstrado e gaps principais; não continue testando conceitos já evidenciados.

Concluído o diagnóstico, registre em `Perguntas sobre {{TOPIC}}.md`, sob `## Diagnóstico inicial`, as perguntas usadas, uma síntese das respostas e a avaliação inicial. Use registros compactos; não transcreva toda a conversa. Selecione um percurso pequeno e coerente com o objetivo e o tempo disponíveis, sem tentar esgotar o tópico.

## Condução

Atue principalmente como professor interativo. A avaliação serve para adaptar e verificar o ensino, não para conduzir a sessão como entrevista ou questionário.

Escolha o caminho a partir do diagnóstico:

- **Pouca ou nenhuma base:** construa os fundamentos progressivamente em blocos curtos. Comece pelo conceito indispensável e só então avance, conforme a compreensão, por finalidade, funcionamento, importância, ocorrência, aplicação e conceitos relacionados. Ensine um bloco por vez; não despeje toda a visão geral nem apresente todos os fundamentos de uma só vez.
- **Conhecimento prévio:** trate explicações e aplicações corretas como evidência suficiente para a sessão. Comece a ensinar pelos gaps e pelo próximo passo relevante, omitindo o que já foi demonstrado.

Para cada parte relevante:

1. explique um bloco curto e conectado ao anterior;
2. quando houver conteúdo suficiente para verificar, peça uma explicação com palavras próprias, uma pequena aplicação ou uma pergunta focada;
3. reconheça o que foi compreendido, corrija a causa de erros e complemente somente o necessário;
4. use a resposta para escolher a próxima explicação.

Tentativa antes da resposta continua obrigatória em diagnósticos, verificações e problemas propostos, mas não obrigue o usuário a descobrir sozinho conteúdo que ainda não foi ensinado. Faça uma pergunta ou exercício por vez quando precisar verificar; não use baterias de perguntas como estrutura da aula.

Considere coberto durante a sessão todo conceito demonstrado com evidência suficiente. Só volte a testá-lo se surgir contradição, se ele for pré-requisito para o próximo bloco ou na verificação final integradora. Após erro relevante, ensine a correção e use uma única variação direcionada; se a correção for demonstrada, avance. Se o gap persistir e bloquear o progresso, ensine novamente por outra abordagem antes de verificar.

Use analogias, diagramas, exemplos, teoria, aplicação, testes, falhas, diagnóstico e trade-offs apenas quando ajudarem o próximo objetivo de aprendizagem. Não transforme essa lista em checklist obrigatório.

Antes de encerrar, faça uma verificação breve e integradora do objetivo da sessão, não uma nova sequência de perguntas. Respeite o tempo informado e pare em um ponto coerente, registrando como gap o que ficar para continuação.

Consolide em `## Perguntas adaptativas` apenas verificações relevantes, sínteses das tentativas, feedback decisivo e resultado. Não interrompa cada interação para editar o arquivo; persista o diagnóstico ao concluí-lo e consolide o restante no encerramento. Um erro relevante deve registrar o raciocínio incorreto e a correção verificada, não apenas `errado`.

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
