# Matrizes + DFS + BFS

Data criação: 2026-09-21
Data último estudo: 2026-09-21
Data última revisão:
Data próxima revisão: 2026-09-22
Status: Estudando
Nível: 2

## Conteúdo

- Em `matriz[linha][coluna]`, o primeiro índice representa a linha e o segundo a coluna.
- `matriz.length` representa a quantidade de linhas; `matriz[linha].length` representa a quantidade de colunas daquela linha.
- Uma matriz quadrada `n × n` tem percurso `O(n²)`; no caso geral com `L` linhas e `C` colunas, o percurso custa `O(L × C)`.
- Matrizes podem ser percorridas com dois loops aninhados.
- Em uma grade, cada célula pode ter vizinhos nas quatro direções: cima, baixo, esquerda e direita; diagonais não entram quando o problema define quatro direções.
- DFS (Depth-First Search) explora um caminho em profundidade antes de voltar. Pode ser implementada com recursão ou pilha.
- BFS (Breadth-First Search) explora por camadas e usa uma fila. Em grafos sem pesos, é adequada para encontrar o menor número de passos.
- `visited` registra células já processadas e evita repetição e recursão infinita.
- O padrão de contagem de ilhas percorre a grade, incrementa ao encontrar uma nova célula de terra e usa DFS/BFS para marcar toda a região conectada.

## Gaps

- Implementar autonomamente DFS e BFS em uma matriz.
- Completar e explicar a função `contarIlhas`.
- Explicar por que `total++` ocorre uma vez antes de explorar a região, e não em cada chamada do DFS.
- Consolidar a diferença entre matriz como representação e pilha/fila como estruturas de controle.
- Praticar limites, `visited`, quatro direções e análise de complexidade.

## Erros

- Interpretou `matriz.length` como quantidade total de células; correção: é a quantidade de linhas.
- Confundiu a linha 0 com a coluna 0 ao listar elementos.
- Incluiu `(2,2)` na mesma região de `(0,0)` por diagonal; correção: com quatro direções, diagonais não conectam células.
- Inicialmente associou DFS ao uso da matriz; correção: a matriz é o espaço percorrido, enquanto DFS usa recursão ou pilha.

## Minhas anotações

<!-- USER-NOTES:START -->

<!-- USER-NOTES:END -->
