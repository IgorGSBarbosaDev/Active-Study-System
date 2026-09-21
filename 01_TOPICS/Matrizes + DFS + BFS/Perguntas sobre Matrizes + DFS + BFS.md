# Perguntas sobre Matrizes + DFS + BFS

Data criação: 2026-09-21

## Diagnóstico inicial

- Entende que o acesso a uma matriz usa linha e depois coluna e reconhece `int[3][3]` como uma matriz quadrada 3×3.
- Reconhece que uma matriz quadrada pode ser percorrida com dois loops aninhados, mas ainda precisa relacionar `O(n²)` ao caso quadrado e `O(linhas × colunas)` ao caso geral.
- Ainda não conhece DFS nem BFS; associou DFS genericamente a uma busca profunda em uma lista/array.
- Precisa diferenciar declaração, criação e acesso (`int[][] matriz`, `new int[3][3]`, `matriz[linha][coluna]`) e entender que arrays bidimensionais Java podem ter linhas de tamanhos diferentes.

## Perguntas adaptativas

- Explicou corretamente que o acesso usa linha e depois coluna, mas precisou corrigir a diferença entre declaração/criação/acesso.
- Confundiu `matriz.length` com a quantidade total de células e confundiu linha com coluna; corrigiu após exemplos concretos.
- Explicou corretamente que `visited` identifica células já processadas.
- Identificou as três células da primeira região, mas incluiu uma diagonal; foi corrigido sobre conectividade em quatro direções.
- Identificou corretamente fila para BFS e pilha para DFS sem recursão.
- Não conseguiu iniciar autonomamente a implementação de `contarIlhas`; recebeu o padrão completo com DFS e a análise de complexidade.

## Resultado

- Base demonstrada com ajuda: indexação, dimensões, percurso de matriz e conectividade por quatro direções.
- Reconhece DFS como busca em profundidade com recursão/pilha e BFS como busca em largura com fila.
- Ainda não demonstrou implementação autônoma nem explicou a razão de incrementar o contador apenas uma vez por região.
- Sessão encerrada após a apresentação da solução de `contarIlhas`; retomar pela pergunta sobre `total++` antes do DFS.

## Gaps identificados

- Implementação autônoma de DFS/BFS em matriz.
- Rastreamento de `visited` e limites da grade.
- Contagem de componentes/regiões conectadas.
- Diferença prática entre DFS e BFS e escolha do algoritmo.

## Avaliações
