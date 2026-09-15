---
name: reviews
description: Consulta a agenda de revisões ou conduz uma revisão espaçada de tópicos já estudados no Active Study System. Não use para ensinar um tópico novo nem para realizar uma avaliação formal de domínio.
---

# Reviews

Consulte ou conduza revisões de conteúdos já estudados. Use `99_SYSTEM/LEARNING_METHOD.md` como autoridade pedagógica; aplique suas regras sem reproduzir suas explicações.

## Preparação

1. Leia `99_SYSTEM/LEARNING_METHOD.md`, `99_SYSTEM/TEMPLATES/topic.md`, `02_REVIEWS/REVIEWS.md` e `02_REVIEWS/REVIEW_LOG.md`.
2. Localize os arquivos principais dos tópicos em `01_TOPICS` e leia seus campos de data. Use datas ISO `YYYY-MM-DD` e a data local atual.
3. Para localizar um tópico solicitado, normalize o nome apenas durante a pesquisa: compare sem distinguir maiúsculas, acentos ou pontuação e procure títulos, nomes de pastas, aliases e links no Vault. Reutilize uma correspondência inequívoca; diante de candidatas plausíveis, peça que o usuário escolha. Nunca crie um tópico nesta Skill.
4. Quando houver uma sessão, leia o arquivo principal e `Perguntas sobre {{TOPIC}}.md`, se existir, considerando conteúdo central, gaps, erros, datas, status, nível e evidências anteriores. Preserve todo conteúdo válido. Texto entre `<!-- USER-NOTES:START -->` e `<!-- USER-NOTES:END -->` é propriedade do usuário e nunca pode ser substituído, movido, normalizado ou reorganizado.

## Agenda

Em toda invocação, reconstrua `02_REVIEWS/REVIEWS.md` a partir de `Data próxima revisão` nos tópicos:

- **Atrasadas:** data anterior à data atual;
- **Hoje:** data igual à data atual;
- **Próximas:** data posterior à data atual.

Ordene cada grupo por data e, em caso de empate, pelo nome do tópico. Liste todas as próximas revisões, sem horizonte artificial. Use uma linha compacta por tópico no formato `- [[caminho/do/tópico|Tópico]] — YYYY-MM-DD` e `- Nenhuma.` quando o grupo estiver vazio. Campos vazios não entram na agenda. Datas não vazias e inválidas ficam fora da classificação, não são corrigidas automaticamente e devem ser informadas ao usuário.

Se o pedido for somente uma consulta, apresente os tópicos e datas solicitados e encerre. Não faça perguntas de recuperação, não altere tópicos e não registre a consulta em `REVIEW_LOG.md`. A sincronização do painel continua sendo realizada.

## Sessão de revisão

Uma solicitação explícita pode iniciar a revisão de um tópico já estudado mesmo sem data programada ou antes da data prevista. Não converta a sessão em aula completa.

1. Defina um foco curto a partir dos gaps e erros relevantes ainda registrados.
2. Escolha o menor conjunto de recuperações capaz de verificar esses pontos e os conceitos centrais necessários. Priorize qualidade da evidência, não quantidade de perguntas.
3. Peça uma recuperação, explicação ou aplicação sem consulta e espere a tentativa. Faça uma solicitação por vez.
4. Se a tentativa revelar erro ou gap, explicite a causa, ensine somente a correção necessária e faça uma única variação curta para verificar a mudança.
5. Considere encerrado todo ponto demonstrado com autonomia. Não repita perguntas equivalentes, salvo se surgir contradição relevante.
6. Encerre quando os pontos prioritários tiverem evidência suficiente ou quando os gaps restantes estiverem claramente localizados.

Não use uma revisão para medir formalmente todo o domínio. Se o usuário pedir uma avaliação, use `assess-topic`; se precisar aprender ou aprofundar conteúdo novo, use `study-topic`.

## Agendamento

A sequência de intervalos é a definida em `LEARNING_METHOD.md`. Determine o estágio atual nesta ordem:

1. transição mais recente do tópico em `REVIEW_LOG.md`;
2. diferença entre `Data próxima revisão` e `Data última revisão`;
3. na primeira revisão, diferença entre `Data próxima revisão` e `Data último estudo`.

Ao concluir uma revisão na data prevista ou depois dela:

- recuperação correta, explicada e autônoma avança um estágio;
- gap relevante reinicia em `D+1`;
- evidência insuficiente para avançar, mas sem gap relevante, repete o estágio atual;
- sucesso em `D+30` mantém `D+30`.

Calcule a nova data a partir da data real da sessão. Se o estágio não puder ser inferido com segurança, use `D+1` e registre que o estágio anterior era indeterminado.

Em uma revisão antecipada, atualize a evidência e `Data última revisão`, mas não avance o estágio nem adie a `Data próxima revisão` existente. Se surgir gap relevante, substitua-a por data atual mais um dia. Quando uma revisão antecipada não tiver data programada ou estágio conhecido, aplique o fallback `D+1`.

## Persistência

Atualize o arquivo principal do tópico sem apagar conteúdo válido:

- defina `Data última revisão` como a data da sessão;
- defina `Data próxima revisão` conforme o agendamento;
- mantenha em `## Gaps` os gaps relevantes ainda abertos;
- registre em `## Erros` apenas erros relevantes, sua causa e a correção verificada;
- não altere `Data criação` nem `Data último estudo`;
- não altere `## Conteúdo` ou o arquivo `Perguntas sobre {{TOPIC}}.md` durante a revisão.

Acrescente a `02_REVIEWS/REVIEW_LOG.md` uma entrada compacta, sem transcrever a conversa:

```markdown
## YYYY-MM-DD — [[caminho/do/tópico|Tópico]]

- Resultado: síntese da recuperação e do grau de autonomia.
- Evidências: o que foi explicado ou aplicado sem assistência.
- Assistência: nenhuma ou suporte necessário.
- Gaps e erros: pontos relevantes ainda abertos ou corrigidos.
- Intervalo: estágio anterior → estágio resultante; próxima revisão YYYY-MM-DD.
```

Use somente `Não iniciado`, `Estudando`, `Praticando` ou `Consolidado` em `Status`. Mantenha `Status` e `Nível` independentes. Só os altere quando a sessão produzir evidência suficiente e rebaixe-os quando a evidência atual contradisser o registro.

Classifique `Nível` pela evidência observada:

- `0` — não compreendeu;
- `1` — reconhece;
- `2` — entende com ajuda;
- `3` — explica corretamente;
- `4` — aplica corretamente;
- `5` — analisa trade-offs, diagnostica problemas e lida com casos não óbvios.

Não marque `Consolidado` por uma única sessão. Exija também evidência autônoma compatível em outra data.

Ao terminar, informe sucintamente o resultado, gaps restantes, status, nível, transição do intervalo, próxima revisão e arquivos atualizados.

## Limites

- Não crie tópicos, não conduza estudo novo e não faça avaliação formal.
- Não altere templates, `LEARNING_METHOD.md`, arquivos de `99_SYSTEM/METHOD`, `99_SYSTEM/STRATEGY` ou notas fora dos arquivos previstos.
- Não trate releitura, acerto assistido ou quantidade de respostas como retenção autônoma.
