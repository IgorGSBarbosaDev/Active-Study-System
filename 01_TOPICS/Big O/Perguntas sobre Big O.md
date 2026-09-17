# Perguntas sobre Big O

Data criação: 2026-09-15

## Diagnóstico inicial

- Objetivo: compreender Big O o suficiente para explicar a outras pessoas, preparar-se para entrevistas e melhorar habilidades de programação.
- Motivo e tempo: faz parte do roadmap pessoal; sessão de aproximadamente 1 hora.
- Síntese da base: reconhece a ideia de crescimento do custo conforme a entrada cresce e cita O(1), O(n), O(n²), O(2ⁿ) e O(log n), associando O(n) à varredura, O(1) à busca direta e O(log n) à divisão pela metade.
- Avaliação inicial: reconhece as principais classes e a intuição geral, mas ainda confunde custo constante com encontrar qualquer valor, trata Big O principalmente como tempo e precisa distinguir notação assintótica, pior caso, espaço e condições de aplicação.

## Perguntas adaptativas

- Pergunta: classificar acesso por índice, busca linear e busca binária na lista `[8, 3, 10, 1, 6]`, incluindo a condição da busca binária.
- Tentativa: classificou acesso por índice como `O(1)`, varredura do início ao fim como `O(n)` e afirmou corretamente que busca binária exige dados ordenados.
- Feedback: correta. Refinamento: busca linear é `O(n)` no pior caso (e `O(1)` no melhor); busca binária não funciona corretamente sem ordenação porque precisa decidir qual metade descartar.

- Pergunta: explicar por que `log₂(16)` representa as etapas da busca binária.
- Tentativa: explicou que os 16 elementos são reduzidos para 8, mas não completou a sequência nem determinou o número de etapas.
- Feedback: parcial. A sequência é `16 → 8 → 4 → 2 → 1`: quatro divisões, portanto `log₂(16) = 4`. O logaritmo responde quantas vezes podemos dividir `n` por 2 até chegar a 1.

- Pergunta: determinar as etapas de uma busca binária com 32 elementos.
- Tentativa: apresentou corretamente `32 → 16 → 8 → 4 → 2 → 1` e concluiu cinco divisões.
- Resultado: correta; `log₂(32) = 5`.

- Pergunta: classificar o algoritmo que percorre uma lista uma vez e imprime cada elemento.
- Tentativa: classificou como `O(n)` porque o laço visita e imprime todos os elementos.
- Feedback: correta. O trabalho cresce proporcionalmente à quantidade de elementos; neste caso, também há espaço auxiliar `O(1)` além da saída produzida.

- Pergunta: classificar dois laços aninhados que percorrem a mesma lista.
- Tentativa: classificou como `O(n²)` porque, para cada elemento de `x`, o laço de `y` percorre `n` elementos, resultando em `n × n` operações.
- Resultado: correta; o raciocínio identifica corretamente a multiplicação causada pelo aninhamento.

- Pergunta: classificar dois laços sequenciais que percorrem a lista.
- Tentativa: respondeu `O(n)`, pois os laços são independentes e cada um percorre a lista uma vez.
- Feedback: correta. O custo é `n + n = 2n`; Big O ignora a constante 2, resultando em `O(n)`. Laços sequenciais somam; laços aninhados multiplicam.

- Pergunta: distinguir melhor e pior caso da busca linear.
- Tentativa: identificou corretamente que o melhor caso ocorre no início e o pior no final, mas classificou ambos genericamente como `O(n)`.
- Feedback: parcial. Melhor caso é `O(1)`, pois uma comparação basta quando o item está na primeira posição. Pior caso é `O(n)`, quando está no fim ou ausente. Em entrevistas, se nada for especificado, costuma-se informar o pior caso; o caso médio também é `O(n)`.

- Pergunta: classificar tempo e espaço ao copiar uma lista para outra.
- Tentativa: explicou corretamente que cada elemento é copiado e que uma segunda lista ocupa memória, mas não nomeou as classes.
- Feedback: sem base específica, com boa intuição. Tempo é `O(n)`, pois há uma operação por elemento. Espaço auxiliar é `O(n)`, pois a nova lista cresce com `n`. Mesmo que a memória total seja aproximadamente `2n`, Big O simplifica para `O(n)`; não se diz `2 × O(n)` como classe assintótica.

- Pergunta: classificar tempo e espaço de uma função que dobra os valores no próprio array.
- Tentativa: classificou corretamente o tempo como `O(n)`, mas afirmou que o espaço seria `O(n)` por percorrer a lista.
- Feedback: parcial. Percorrer dados não implica alocar memória proporcional. Como a alteração ocorre no próprio array e só usamos o índice `i`, o espaço auxiliar é `O(1)`. O erro foi confundir quantidade de elementos visitados (tempo) com memória nova alocada (espaço).
- Preferência registrada: usar exemplos em Java nas próximas perguntas.

- Pergunta: classificar a função Java que cria um novo array e copia valores dobrados.
- Tentativa: respondeu tempo `O(n)` e espaço `O(1)`.
- Feedback: tempo correto. Espaço incorreto: `resultado` possui `n` posições e é uma alocação nova, então o espaço auxiliar é `O(n)`. A distinção essencial é: modificar o array recebido pode usar `O(1)` espaço; criar um array de saída usa `O(n)`.

- Pergunta: analisar busca binária iterativa em Java.
- Tentativa: classificou tempo como `O(log n)` e espaço como `O(1)`, mas não identificou a condição do array.
- Feedback: parcialmente correta. Tempo `O(log n)` e espaço auxiliar `O(1)` estão corretos. O array precisa estar ordenado em ordem crescente, pois as comparações `valores[meio] < alvo` e `> alvo` determinam qual metade pode ser descartada. Sem ordenação, essa decisão pode eliminar a metade que contém o alvo.

## Resultado

- Explicou corretamente que Big O descreve o crescimento do custo conforme `n` aumenta, sem ser uma medição exata de tempo.
- Classificou e justificou corretamente acesso por índice (`O(1)`), busca linear (`O(n)` no pior caso), busca binária (`O(log n)`), laços aninhados (`O(n²)`) e laços sequenciais (`O(n)`).
- Aplicou corretamente tempo e espaço em exemplos Java após feedback: alteração no próprio array usa espaço auxiliar `O(1)`; criação de novo array usa `O(n)`.
- Explicou corretamente por que a busca binária exige ordenação e por que divide o espaço de busca sucessivamente pela metade.
- Precisou de assistência para distinguir melhor caso (`O(1)`) de pior caso (`O(n)`) na busca linear e para separar memória alocada de elementos apenas percorridos.

## Gaps identificados

- Recuperar sem pistas a diferença entre melhor, médio e pior caso.
- Consolidar análise de espaço auxiliar em códigos com estruturas existentes versus novas alocações.
- Praticar classes menos exploradas, especialmente `O(n log n)`, `O(2ⁿ)` e análise de algoritmos de ordenação.
