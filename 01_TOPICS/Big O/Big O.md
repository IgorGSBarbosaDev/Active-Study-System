# Big O

Data criação: 2026-09-15
Data último estudo: 2026-09-15
Data última revisão: 2026-09-20
Data próxima revisão: 2026-09-21
Status: Praticando
Nível: 3

## Conteúdo

- Big O é uma notação assintótica que descreve como o custo de um algoritmo cresce conforme o tamanho da entrada `n` aumenta; não é uma medição exata de tempo nem depende diretamente de hardware.
- Constantes são ignoradas: `2n` é `O(n)`. Laços sequenciais somam (`n + n = O(n)`); laços aninhados multiplicam (`n × n = O(n²)`).
- Classes trabalhadas: acesso direto `O(1)`, busca linear `O(n)`, busca binária `O(log n)` e laços aninhados `O(n²)`.
- Busca linear: melhor caso `O(1)`, pior e caso médio `O(n)`; se nada for especificado, normalmente se comunica o pior caso.
- Busca binária divide o espaço de busca pela metade e exige dados ordenados. A versão iterativa analisada usa tempo `O(log n)` e espaço auxiliar `O(1)`.
- Tempo mede operações; espaço auxiliar mede memória nova alocada. Alterar o array existente pode usar `O(1)`, enquanto criar uma estrutura proporcional a `n` usa `O(n)`.

## Gaps

- Consolidar análise de espaço auxiliar em códigos mais variados.
- Entender com autonomia a relação entre recursão, pilha de chamadas e espaço `O(log n)`.
- Estudar e aplicar `O(n log n)`, `O(2ⁿ)` e análise de algoritmos de ordenação.

## Erros

- Inicialmente tratou `O(1)` como busca por um valor específico; modelo corrigido: `O(1)` significa custo independente de `n`, como acesso por índice.
- Classificou o melhor caso da busca linear como `O(n)`; modelo corrigido: melhor caso `O(1)`, pior caso `O(n)`.
- Confundiu percorrer uma lista com alocar memória proporcional a ela; modelo corrigido: tempo pode ser `O(n)` com espaço auxiliar `O(1)` quando a operação ocorre no próprio array.
- Classificou como `O(1)` o espaço de uma função que cria um novo array; modelo corrigido: a nova estrutura com `n` posições gera espaço auxiliar `O(n)`.
- Ao explicar busca binária recursiva, atribuiu `O(log n)` à dependência da versão iterativa; modelo corrigido: cada chamada fica na pilha e a profundidade é `O(log n)`.
- Contou 4 frames para 16 elementos; considerando a chamada inicial, a sequência `16 → 8 → 4 → 2 → 1` pode ter 5 frames, embora a classe assintótica continue `O(log n)`.

## Minhas anotações

<!-- USER-NOTES:START -->

<!-- USER-NOTES:END -->
