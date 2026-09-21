# Resumo - Matrizes + DFS + BFS

Data criação: 2026-09-21
Data última atualização: 2026-09-21
Tipo: Material de estudo
Escopo: representação e percurso de matrizes em Java; DFS, BFS, `visited` e contagem de regiões conectadas.

## Conceitos essenciais

### Matrizes em Java

Uma matriz usa dois índices:

```java
matriz[linha][coluna]
```

- Primeiro índice: linha.
- Segundo índice: coluna.
- `matriz.length`: quantidade de linhas.
- `matriz[linha].length`: quantidade de colunas daquela linha.

Criação:

```java
int[][] matriz = new int[3][3];
```

Acesso e alteração:

```java
matriz[1][2] = 10;
int valor = matriz[1][2];
```

Uma matriz Java também pode ter linhas de tamanhos diferentes:

```java
int[][] matriz = {
    {1, 2},
    {3, 4, 5}
};
```

### Percurso

```java
for (int linha = 0; linha < matriz.length; linha++) {
    for (int coluna = 0;
         coluna < matriz[linha].length;
         coluna++) {
        System.out.println(matriz[linha][coluna]);
    }
}
```

Para uma matriz com `L` linhas e `C` colunas, o custo é `O(L × C)`. Em uma matriz quadrada `n × n`, o custo é `O(n²)`.

### Vizinhos em uma grade

Quando o problema define quatro direções, os vizinhos são:

- cima;
- baixo;
- esquerda;
- direita.

Uma célula diagonal não é vizinha nesse modelo.

## Funcionamento e relações

### DFS — Depth-First Search

DFS explora um caminho em profundidade antes de voltar para tentar outro caminho.

Pode ser implementada com:

- recursão, usando implicitamente a pilha de chamadas;
- uma pilha explícita (`Stack` ou `Deque`).

Modelo recursivo para uma grade:

```java
void dfs(int[][] grid, boolean[][] visitado,
         int linha, int coluna) {
    if (linha < 0 || linha >= grid.length ||
        coluna < 0 || coluna >= grid[linha].length ||
        grid[linha][coluna] == 0 ||
        visitado[linha][coluna]) {
        return;
    }

    visitado[linha][coluna] = true;

    dfs(grid, visitado, linha - 1, coluna);
    dfs(grid, visitado, linha + 1, coluna);
    dfs(grid, visitado, linha, coluna - 1);
    dfs(grid, visitado, linha, coluna + 1);
}
```

A condição de parada verifica limites, água ou célula já visitada.

### BFS — Breadth-First Search

BFS explora a grade por camadas:

```text
distância 0 → início
distância 1 → vizinhos diretos
distância 2 → vizinhos dos vizinhos
```

Usa uma fila:

```java
Queue<int[]> fila = new ArrayDeque<>();
fila.add(new int[]{linhaInicial, colunaInicial});
visitado[linhaInicial][colunaInicial] = true;

while (!fila.isEmpty()) {
    int[] atual = fila.remove();
    // explorar os quatro vizinhos
}
```

A célula deve ser marcada ao entrar na fila para evitar inserções repetidas. Em grafos sem pesos, BFS é adequada para encontrar o menor número de passos.

### `visited`

`visited` registra células já processadas. Ele evita:

- repetir trabalho;
- visitar a mesma célula várias vezes;
- recursão infinita em regiões conectadas.

### Contagem de ilhas

O padrão é:

1. percorrer todas as células;
2. encontrar uma célula de terra (`1`) ainda não visitada;
3. incrementar o contador uma vez;
4. usar DFS ou BFS para marcar toda a região conectada;
5. continuar procurando outra região.

O `total++` ocorre uma vez por nova região, não em cada célula visitada.

## Exemplos e aplicações

Para a grade:

```text
1 1 0
0 1 0
0 0 1
```

Começando em `(0,0)` e usando quatro direções, a primeira região contém:

```text
(0,0), (0,1), (1,1)
```

`(2,2)` não pertence à região porque está apenas na diagonal.

Modelo de contagem de regiões:

```java
static int contarIlhas(int[][] grid) {
    if (grid == null || grid.length == 0) {
        return 0;
    }

    boolean[][] visitado =
            new boolean[grid.length][grid[0].length];
    int total = 0;

    for (int linha = 0; linha < grid.length; linha++) {
        for (int coluna = 0; coluna < grid[linha].length; coluna++) {
            if (grid[linha][coluna] == 1 &&
                !visitado[linha][coluna]) {
                total++;
                dfs(grid, visitado, linha, coluna);
            }
        }
    }

    return total;
}
```

O modelo foi estudado, mas ainda precisa ser implementado autonomamente.

## Erros e cuidados

- `matriz.length` não é a quantidade total de células; é a quantidade de linhas.
- Na expressão `matriz[linha][coluna]`, o primeiro índice é a linha.
- `matriz[0][0]`, `matriz[1][0]` e `matriz[2][0]` formam parte da coluna 0, não da linha 0.
- A matriz é a estrutura representada; DFS usa recursão/pilha e BFS usa fila.
- Diagonais não conectam células quando o problema define somente quatro direções.
- Sem `visited`, a busca pode repetir células ou entrar em recursão infinita.
- Em uma matriz geral, a complexidade é `O(L × C)`, não necessariamente `O(n²)`.

## Gaps e aprofundamento

- Implementar DFS em uma matriz sem consultar o modelo.
- Implementar BFS em uma matriz usando `Queue`.
- Completar autonomamente `contarIlhas`.
- Explicar por que `total++` ocorre antes do DFS.
- Praticar limites, `visited`, regiões conectadas e complexidade.
- Comparar na prática quando escolher DFS ou BFS.

## Checklist de recuperação

- O que representam os dois índices de `matriz[linha][coluna]`?
- Qual a diferença entre `matriz.length` e `matriz[linha].length`?
- Quando o percurso custa `O(L × C)` e quando pode ser escrito como `O(n²)`?
- Quais são os quatro vizinhos de uma célula?
- O que significa DFS e qual estrutura ela usa?
- O que significa BFS e qual estrutura ela usa?
- Por que `visited` é necessário?
- Por que BFS pode encontrar o menor caminho em um grafo sem pesos?
- Como contar regiões conectadas em uma matriz?
- Por que o contador de ilhas é incrementado apenas uma vez por região?

## Minhas anotações

<!-- USER-NOTES:START -->

<!-- USER-NOTES:END -->
