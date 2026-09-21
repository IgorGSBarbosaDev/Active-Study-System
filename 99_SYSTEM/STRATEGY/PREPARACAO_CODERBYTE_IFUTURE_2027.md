# Preparação Coderbyte — iFuture 2027 | Engenharia de Software

> Objetivo: preparar-se de forma focada para o teste técnico do iFood na Coderbyte.
>
> Período de preparação: **19/09/2026 a 22/09/2026**
> Teste oficial planejado: **23/09/2026 às 08:00**
>
> Prioridade: **resolver problemas, reconhecer padrões e justificar decisões**, não estudar conteúdo amplo de Engenharia de Software.

---

# 1. Estratégia da preparação

A preparação deve priorizar os tópicos com maior probabilidade de aparecer no teste:

1. **Matrizes + DFS/BFS**
2. **Arrays + Strings + HashMap/HashSet**
3. **SQL**
4. **Stack + Queue**
5. **Sorting + Searching**
6. **Big O e estruturas de dados**
7. **Web/Git/arquitetura/sistemas distribuídos em nível conceitual**

Evitar nesta semana:

- Dynamic Programming avançada;
- Dijkstra;
- Trie;
- Union Find;
- árvores balanceadas;
- Heap avançado;
- Kubernetes;
- Spring aprofundado;
- microsserviços aprofundados;
- System Design completo.

---

# 2. Regra de aprendizado ativo

Para cada tópico, seguir:

```text
Entender
↓
Explicar com as próprias palavras
↓
Reconhecer quando usar
↓
Implementar
↓
Resolver problema sem ajuda
↓
Analisar complexidade
↓
Identificar erros e edge cases
```

Um tópico só está suficientemente preparado para a prova quando você consegue:

- explicar o conceito;
- identificar quando ele deve ser usado;
- implementar o caso principal;
- resolver pelo menos 1 problema sem ajuda;
- dizer a complexidade aproximada;
- reconhecer erros comuns.

---

# 3. Arrays

## Entender

- índice;
- acesso por posição;
- iteração;
- atualização;
- tamanho fixo;
- diferença entre array e lista;
- custo de acesso;
- custo de busca;
- custo de inserção/remoção.

## Saber explicar

- Por que acessar `array[i]` é O(1)?
- Por que procurar um valor geralmente é O(n)?
- Quando ordenar um array pode ajudar?
- Quando usar array/lista em vez de HashMap?

## Praticar

- percorrer array;
- encontrar máximo/mínimo;
- somar valores;
- contar ocorrências;
- comparar elementos;
- remover duplicatas;
- ordenar;
- buscar elementos;
- usar dois ponteiros.

## Problemas

- Two Sum
- Contains Duplicate
- Find Intersection
- Maximum Subarray
- remover duplicatas
- encontrar maior/menor valor

## Critério de domínio

- [ ] Consigo percorrer e manipular arrays sem consultar sintaxe.
- [ ] Consigo reconhecer problemas de busca e contagem.
- [ ] Consigo usar `Arrays.sort`.
- [ ] Consigo explicar O(1), O(n) e O(n log n) nesses casos.
- [ ] Resolvi Two Sum sem ajuda.

---

# 4. Strings

## Entender

- string como sequência de caracteres;
- comparação;
- acesso por índice;
- substring;
- split;
- transformação;
- StringBuilder;
- frequência de caracteres.

## Saber explicar

- Quando usar `StringBuilder`?
- Como detectar palindrome?
- Como verificar anagrama?
- Quando usar HashMap/array de frequência?

## Praticar

- inverter string;
- palindrome;
- contar caracteres;
- primeira ocorrência;
- primeiro caractere não repetido;
- anagrama;
- parsing simples;
- transformação de texto.

## Problemas

- Palindrome
- Valid Anagram
- First Non-Repeating Character
- First Reverse
- Longest Word
- Run Length

## Critério de domínio

- [ ] Consigo implementar palindrome sem ajuda.
- [ ] Consigo inverter uma string.
- [ ] Consigo contar frequência de caracteres.
- [ ] Consigo resolver anagrama.
- [ ] Consigo identificar quando usar dois ponteiros.

---

# 5. HashMap e HashSet

## Entender

### HashMap

Armazena:

```text
chave → valor
```

Usar quando precisar relacionar um elemento a alguma informação.

Exemplos:

```text
nome → quantidade
número → posição
caractere → frequência
```

### HashSet

Armazena valores únicos.

Usar principalmente para:

- verificar rapidamente se algo já apareceu;
- remover duplicatas;
- controlar elementos visitados.

## Java

Dominar:

```java
HashMap<K, V>
HashSet<T>

map.put(key, value);
map.get(key);
map.getOrDefault(key, 0);
map.containsKey(key);

set.add(value);
set.contains(value);
```

## Saber explicar

- Por que HashMap costuma ter acesso médio O(1)?
- HashMap vs HashSet.
- Quando HashMap melhora uma solução O(n²) para O(n)?
- Por que Two Sum pode ser resolvido com HashMap?

## Problemas

- Two Sum
- Contains Duplicate
- Valid Anagram
- frequência de caracteres
- Find Intersection
- Group Totals

## Critério de domínio

- [ ] Sei decidir entre Map e Set.
- [ ] Sei usar `getOrDefault`.
- [ ] Resolvo problemas de frequência.
- [ ] Resolvo Two Sum com O(n).
- [ ] Consigo explicar por que HashMap melhora a solução.

---

# 6. Two Pointers

## Entender

Dois índices percorrem a estrutura simultaneamente.

Padrão comum:

```text
left → início
right → fim
```

## Reconhecer quando usar

- comparar início e fim;
- palindrome;
- arrays ordenados;
- procurar pares;
- reduzir necessidade de loops aninhados.

## Problemas

- Palindrome
- Two Sum em array ordenado
- remover duplicatas de array ordenado
- inverter array/string

## Critério de domínio

- [ ] Reconheço quando dois ponteiros fazem sentido.
- [ ] Consigo implementar palindrome usando `left` e `right`.
- [ ] Consigo explicar a complexidade.

---

# 7. Sliding Window

## Entender

Manter uma janela contínua dentro de uma sequência.

Exemplo:

```text
[a b c d e f]
 ↑   ↑
left right
```

## Saber reconhecer

Problemas envolvendo:

- substring;
- subarray;
- maior sequência;
- menor sequência;
- janela contínua.

## Praticar

- maior substring sem repetir;
- soma de janela;
- substring mínima em nível básico.

## Problemas

- Longest Substring Without Repeating Characters
- Min Window Substring — apenas se houver tempo

## Critério de domínio

- [ ] Entendo o conceito de janela.
- [ ] Consigo mover `left` e `right`.
- [ ] Sei diferenciar sliding window de two pointers simples.

---

# 8. Stack

## Entender

```text
LIFO
Last In, First Out
```

Operações:

```text
push
pop
peek
```

## Java

Preferir:

```java
Deque<Character> stack = new ArrayDeque<>();
```

## Quando usar

- parênteses;
- brackets;
- estruturas aninhadas;
- undo;
- parsing;
- DFS iterativa.

## Problemas

- Valid Parentheses
- Bracket Matcher

## Saber explicar

- Por que stack resolve validação de parênteses?
- Qual elemento sai primeiro?
- Stack vs Queue.

## Critério de domínio

- [ ] Sei implementar stack com `ArrayDeque`.
- [ ] Resolvo Valid Parentheses.
- [ ] Consigo reconhecer problemas LIFO.

---

# 9. Queue

## Entender

```text
FIFO
First In, First Out
```

Operações:

```text
offer
poll
peek
```

## Java

```java
Deque<Integer> queue = new ArrayDeque<>();
```

## Quando usar

- processamento em ordem;
- BFS;
- filas de tarefas;
- exploração por níveis.

## Saber explicar

- Por que BFS usa Queue?
- Queue vs Stack.
- O que significa FIFO?

## Critério de domínio

- [ ] Sei implementar uma Queue.
- [ ] Sei usar Queue em BFS.
- [ ] Consigo explicar FIFO.

---

# 10. Matrizes 2D

> **Prioridade muito alta para o teste.**

## Entender

Representação:

```text
matrix[row][col]
```

Percorrer:

```java
for (int row = 0; row < rows; row++) {
    for (int col = 0; col < cols; col++) {
        // ...
    }
}
```

## Dominar

- linhas;
- colunas;
- limites;
- vizinhos;
- coordenadas;
- matriz de visitados.

## Vizinhos

Normalmente:

```text
(row - 1, col) → cima
(row + 1, col) → baixo
(row, col - 1) → esquerda
(row, col + 1) → direita
```

## Praticar

- percorrer matriz inteira;
- acessar vizinhos;
- verificar limites;
- marcar célula visitada;
- encontrar regiões conectadas.

## Saber explicar

- Como transformar uma matriz em um problema de grafo?
- O que representa cada célula?
- Quem são os vizinhos?
- Como impedir acesso fora dos limites?

## Critério de domínio

- [ ] Percorro matriz sem dificuldade.
- [ ] Sei verificar limites.
- [ ] Sei visitar quatro direções.
- [ ] Sei usar `boolean[][] visited`.
- [ ] Reconheço regiões conectadas.

---

# 11. DFS — Depth First Search

> **Prioridade máxima.**

## Entender

DFS explora profundamente um caminho antes de voltar.

Pode usar:

```text
recursão
ou
stack
```

## Template mental

```text
dfs(row, col)

se fora dos limites:
    retorna

se inválido:
    retorna

se já visitado:
    retorna

marca como visitado

visita cima
visita baixo
visita esquerda
visita direita
```

## Aplicações

- Flood Fill;
- Number of Islands;
- regiões conectadas;
- componentes de grafo;
- caminhos simples.

## Saber explicar

- O que é DFS?
- Por que recursão funciona para DFS?
- Como evitar loop infinito?
- Para que serve `visited`?
- Qual é a complexidade em uma matriz?

Em uma matriz:

```text
O(rows * cols)
```

quando cada célula é visitada no máximo uma vez.

## Problemas obrigatórios

1. Flood Fill — LeetCode 733
2. Number of Islands — LeetCode 200
3. Max Area of Island — LeetCode 695

## Critério de domínio

- [ ] Consigo escrever DFS de memória.
- [ ] Sei usar `visited`.
- [ ] Resolvo Flood Fill.
- [ ] Resolvo Number of Islands.
- [ ] Consigo explicar por que a solução é O(rows × cols).

---

# 12. BFS — Breadth First Search

## Entender

BFS explora:

```text
nível por nível
```

Usa:

```text
Queue
```

## Fluxo

```text
adiciona origem na Queue

enquanto Queue não vazia:
    remove elemento
    processa
    adiciona vizinhos válidos
```

## Aplicações

- matriz;
- grafos;
- menor caminho sem peso;
- busca por níveis;
- regiões conectadas.

## Saber explicar

- DFS vs BFS.
- Por que BFS usa Queue?
- Quando BFS encontra menor caminho?
- Qual a complexidade?

## Praticar

Resolver novamente:

- Flood Fill usando BFS;
- Number of Islands usando BFS.

## Critério de domínio

- [ ] Sei implementar BFS usando Queue.
- [ ] Sei explicar DFS vs BFS.
- [ ] Consigo resolver problema de matriz com BFS.

---

# 13. Grafos

## Entender somente o necessário

Conceitos:

- vertex/nó;
- edge/aresta;
- vizinhos;
- directed vs undirected;
- connected component;
- visited;
- DFS;
- BFS.

## Não estudar agora

- Dijkstra;
- Bellman-Ford;
- Floyd-Warshall;
- MST;
- Union Find avançado.

## Saber explicar

- O que é um grafo?
- Como uma matriz pode representar implicitamente um grafo?
- DFS vs BFS.
- O que é componente conectado?

## Critério de domínio

- [ ] Entendo nó e aresta.
- [ ] Entendo componente conectado.
- [ ] Sei percorrer usando DFS/BFS.

---

# 14. Recursão

## Entender

Uma função chama a si mesma.

Necessário:

```text
base case
recursive case
```

## Praticar

- factorial;
- DFS;
- soma simples;
- percorrer estrutura.

## Saber explicar

- O que impede recursão infinita?
- O que é base case?
- Relação entre recursão e call stack.

## Problemas

- Factorial
- DFS em matriz

## Critério de domínio

- [ ] Sei implementar factorial.
- [ ] Sei identificar base case.
- [ ] Consigo usar recursão em DFS.

---

# 15. Sorting

## Entender

Complexidade típica:

```text
O(n log n)
```

## Java

Dominar:

```java
Arrays.sort(array);
Collections.sort(list);
list.sort(comparator);
```

## Saber

Em nível conceitual:

- Bubble Sort;
- Insertion Sort;
- Merge Sort;
- Quick Sort.

Não gastar tempo implementando todos nesta semana.

## Saber explicar

- Por que ordenar pode simplificar um problema?
- Qual custo geralmente deve ser considerado?
- Quando sorting + scan pode ser melhor que loops aninhados?

## Critério de domínio

- [ ] Sei ordenar arrays e listas.
- [ ] Sei usar Comparator básico.
- [ ] Sei que sorting geralmente custa O(n log n).
- [ ] Reconheço quando ordenar ajuda.

---

# 16. Binary Search

## Entender

Pré-requisito:

```text
dados ordenados
```

Complexidade:

```text
O(log n)
```

## Saber implementar

```text
left
right
mid
```

## Problema

- Binary Search — LeetCode 704

## Saber explicar

- Por que é O(log n)?
- Por que exige dados ordenados?
- Quando usar?

## Critério de domínio

- [ ] Implemento busca binária.
- [ ] Sei explicar O(log n).
- [ ] Sei identificar quando pode ser usada.

---

# 17. Big O

## Dominar

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
```

## Reconhecer

```text
acesso direto → O(1)

binary search → O(log n)

1 loop → O(n)

sorting → O(n log n)

2 loops aninhados → geralmente O(n²)
```

## Saber explicar

- tempo vs memória;
- melhor abordagem entre duas soluções;
- impacto de HashMap;
- impacto de sorting;
- DFS/BFS em matriz.

## Critério de domínio

- [ ] Identifico as complexidades acima.
- [ ] Sei analisar loops.
- [ ] Sei explicar Two Sum O(n²) vs O(n).
- [ ] Sei explicar DFS de matriz.

---

# 18. SQL

> **Prioridade alta.**

## Dominar

```sql
SELECT
FROM
WHERE
ORDER BY
ASC
DESC
LIMIT

INNER JOIN
LEFT JOIN

GROUP BY
HAVING

COUNT()
SUM()
AVG()
MAX()
MIN()

DISTINCT

IS NULL
IS NOT NULL

LIKE
IN

CASE WHEN
```

## Entender

- filtragem;
- ordenação;
- agregação;
- agrupamento;
- relacionamento entre tabelas;
- diferença entre WHERE e HAVING;
- INNER JOIN vs LEFT JOIN.

## Praticar

### Exercício 1

Buscar funcionários ativos.

### Exercício 2

Ordenar funcionários por salário.

### Exercício 3

Contar funcionários por departamento.

### Exercício 4

Retornar departamentos com mais de N funcionários.

### Exercício 5

JOIN entre funcionários e departamentos.

### Exercício 6

LEFT JOIN mostrando inclusive registros sem relacionamento.

### Exercício 7

GROUP BY + HAVING + ORDER BY.

### Exercício 8

CASE WHEN.

## Saber explicar

- WHERE vs HAVING.
- INNER JOIN vs LEFT JOIN.
- GROUP BY.
- agregações.
- NULL.

## Critério de domínio

- [ ] Escrevo SELECT/WHERE sem consultar.
- [ ] Faço JOIN.
- [ ] Faço GROUP BY.
- [ ] Uso HAVING corretamente.
- [ ] Consigo combinar GROUP BY + HAVING + ORDER BY.
- [ ] Resolvo pelo menos 5 queries sem ajuda.

---

# 19. HTTP e Engenharia Web

## Revisar

Métodos:

```text
GET
POST
PUT
PATCH
DELETE
```

Status:

```text
200
201
204
400
401
403
404
409
500
```

Conceitos:

- request;
- response;
- header;
- body;
- query parameter;
- path parameter;
- JSON;
- REST;
- idempotência;
- cliente-servidor.

## Saber explicar

- GET vs POST.
- PUT vs PATCH.
- 401 vs 403.
- path parameter vs query parameter.
- o que significa idempotência.

## Critério de domínio

- [ ] Reconheço métodos HTTP.
- [ ] Reconheço status codes principais.
- [ ] Sei interpretar request/response.
- [ ] Sei explicar REST em nível básico.

---

# 20. Git

## Revisar

```bash
git clone
git status
git add
git commit
git push
git pull
git fetch

git branch
git switch
git checkout

git merge
git rebase

git log
git diff

git reset
git revert
```

## Saber explicar

- pull vs fetch;
- merge vs rebase;
- reset vs revert;
- commit;
- branch;
- conflito.

## Critério de domínio

- [ ] Sei explicar comandos principais.
- [ ] Sei diferenciar merge/rebase.
- [ ] Sei diferenciar reset/revert.
- [ ] Sei diferenciar pull/fetch.

---

# 21. Sistemas distribuídos e arquitetura

> Estudar somente em nível conceitual para múltipla escolha.

## Revisar

- monólito;
- microsserviços;
- escalabilidade vertical;
- escalabilidade horizontal;
- load balancer;
- cache;
- mensageria;
- comunicação síncrona;
- comunicação assíncrona;
- stateless;
- disponibilidade;
- consistência;
- timeout;
- retry;
- circuit breaker.

## Saber explicar

- horizontal vs vertical scaling;
- sync vs async;
- para que serve cache;
- para que serve load balancer;
- por que usar fila;
- timeout e retry;
- monólito vs microsserviços em nível básico.

## Critério de domínio

- [ ] Reconheço todos os conceitos acima.
- [ ] Consigo responder perguntas conceituais curtas.
- [ ] Não preciso implementar esses conceitos para esta prova.

---

# 22. Lista principal de problemas

## Obrigatórios

- [ ] Palindrome
- [ ] Two Sum
- [ ] Valid Anagram
- [ ] Contains Duplicate
- [ ] Find Intersection
- [ ] Valid Parentheses
- [ ] Binary Search
- [ ] Maximum Subarray
- [ ] Flood Fill
- [ ] Number of Islands
- [ ] Max Area of Island
- [ ] Moving Median

## Se sobrar tempo

- [ ] Bracket Matcher
- [ ] Group Totals
- [ ] Run Length
- [ ] First Non-Repeating Character
- [ ] Longest Substring Without Repeating Characters
- [ ] Min Window Substring

---

# 23. Padrões que precisam virar automáticos

```text
Preciso saber se já vi um elemento?
→ HashSet

Preciso relacionar elemento → informação?
→ HashMap

Preciso contar frequência?
→ HashMap

Preciso comparar início e fim?
→ Two Pointers

Preciso analisar uma sequência contínua?
→ Sliding Window

Tenho parênteses/aninhamento?
→ Stack

Preciso processar em ordem?
→ Queue

Tenho células conectadas numa matriz?
→ DFS ou BFS

Preciso encontrar regiões/grupos?
→ DFS ou BFS

Tenho dados ordenados e preciso buscar?
→ Binary Search

Preciso reorganizar os dados antes de processar?
→ Sorting

Preciso explorar profundamente?
→ DFS

Preciso explorar por níveis?
→ BFS
```

---

# 24. Cronograma

# Sábado — 19/09

## Objetivo

Construir a base dos problemas mais frequentes e se familiarizar com a Coderbyte.

## Fazer

### 1. Avaliação de aquecimento

Usar para entender:

- [ ] editor;
- [ ] linguagem;
- [ ] execução;
- [ ] test cases;
- [ ] submit;
- [ ] busca interna;
- [ ] formato da plataforma.

### 2. Arrays + Strings

Estudar e praticar:

- [ ] percorrer array;
- [ ] máximo/mínimo;
- [ ] palindrome;
- [ ] reverse string;
- [ ] anagrama;
- [ ] frequência.

Problemas:

- [ ] Palindrome
- [ ] Valid Anagram
- [ ] Find Intersection

### 3. HashMap + HashSet

- [ ] frequência;
- [ ] duplicatas;
- [ ] busca rápida.

Problemas:

- [ ] Two Sum
- [ ] Contains Duplicate

### 4. Stack + Queue

- [ ] LIFO;
- [ ] FIFO;
- [ ] ArrayDeque.

Problemas:

- [ ] Valid Parentheses
- [ ] Bracket Matcher

---

# Domingo — 20/09

## Objetivo

Dominar matriz + DFS/BFS.

### 1. Matrizes

- [ ] linhas;
- [ ] colunas;
- [ ] loops;
- [ ] limites;
- [ ] vizinhos;
- [ ] visited.

### 2. DFS

- [ ] template recursivo;
- [ ] base cases;
- [ ] visited;
- [ ] quatro direções.

Problemas:

- [ ] Flood Fill
- [ ] Number of Islands
- [ ] Max Area of Island

### 3. BFS

- [ ] Queue;
- [ ] processamento por níveis;
- [ ] visited.

Refazer:

- [ ] Flood Fill com BFS
- [ ] Number of Islands com BFS

### 4. SQL inicial

Praticar:

- [ ] SELECT/WHERE
- [ ] ORDER BY
- [ ] GROUP BY
- [ ] JOIN
- [ ] HAVING

---

# Segunda — 21/09

## Objetivo

Consolidar DSA e SQL.

### Coding

Resolver sem ajuda:

- [ ] Two Sum
- [ ] Valid Parentheses
- [ ] Binary Search
- [ ] Number of Islands
- [ ] Flood Fill
- [ ] Maximum Subarray

### SQL

Fazer 5–8 exercícios envolvendo:

- [ ] JOIN
- [ ] GROUP BY
- [ ] HAVING
- [ ] ORDER BY
- [ ] agregações
- [ ] NULL

### Teoria

Revisar:

- [ ] Big O
- [ ] Array
- [ ] HashMap
- [ ] HashSet
- [ ] Stack
- [ ] Queue
- [ ] Graph
- [ ] DFS
- [ ] BFS
- [ ] Binary Search
- [ ] Sorting

---

# Terça — 22/09

## Objetivo

Simular a prova e corrigir lacunas.

### Simulado

Tempo sugerido:

```text
2 horas
```

Sem:

- ChatGPT;
- Google externo;
- Copilot;
- IDE externa;
- segunda tela;
- documentação externa.

Estrutura:

```text
1 questão SQL
+
1 problema coding Medium
+
20–30 questões técnicas/conceituais
```

Escolher um problema:

- Number of Islands;
- Flood Fill;
- Max Area of Island;
- Moving Median;
- Bracket Matcher.

### Pós-simulado

Registrar:

```text
Onde travei?

Foi:
- sintaxe?
- reconhecimento de padrão?
- estrutura de dados?
- algoritmo?
- edge case?
- Big O?
- SQL?
- teoria?
```

Corrigir somente essas lacunas.

### Noite

- [ ] revisão leve;
- [ ] nenhuma técnica nova;
- [ ] revisar templates;
- [ ] dormir adequadamente.

---

# Quarta — 23/09

## Antes da prova

Fazer apenas:

- [ ] 1 problema Easy;
- [ ] revisar HashMap;
- [ ] revisar DFS;
- [ ] revisar BFS;
- [ ] revisar SQL;
- [ ] revisar Big O;
- [ ] conferir computador/internet;
- [ ] fechar extensões e programas desnecessários.

Não estudar conteúdo novo.

---

# 25. Checklist final

## Coding

- [ ] Arrays
- [ ] Strings
- [ ] HashMap
- [ ] HashSet
- [ ] Two Pointers
- [ ] Stack
- [ ] Queue
- [ ] Matrix
- [ ] DFS
- [ ] BFS
- [ ] Sorting
- [ ] Binary Search
- [ ] Recursion
- [ ] Big O

## SQL

- [ ] SELECT
- [ ] WHERE
- [ ] ORDER BY
- [ ] JOIN
- [ ] GROUP BY
- [ ] HAVING
- [ ] Aggregations
- [ ] NULL

## Teoria

- [ ] estruturas de dados;
- [ ] algoritmos;
- [ ] HTTP;
- [ ] Git;
- [ ] arquitetura básica;
- [ ] sistemas distribuídos básicos.

---

# 26. Critério de prontidão para quarta-feira

Antes da prova, devo conseguir responder **sim** para:

- [ ] Resolvo Two Sum sem ajuda.
- [ ] Resolvo Valid Parentheses sem ajuda.
- [ ] Implemento Binary Search.
- [ ] Percorro uma matriz 2D corretamente.
- [ ] Implemento DFS em matriz.
- [ ] Implemento BFS em matriz.
- [ ] Resolvo Flood Fill.
- [ ] Entendo Number of Islands.
- [ ] Sei usar HashMap e HashSet.
- [ ] Sei analisar Big O dos casos principais.
- [ ] Consigo escrever JOIN.
- [ ] Consigo escrever GROUP BY + HAVING.
- [ ] Sei diferenciar Stack e Queue.
- [ ] Sei explicar DFS vs BFS.
- [ ] Sei reconhecer os padrões principais sem precisar ver a solução.

---

# Regra final

Nesta preparação, o objetivo não é:

> resolver o maior número possível de LeetCodes.

O objetivo é:

> **reconhecer rapidamente o padrão do problema, escolher a estrutura de dados correta e implementar uma solução funcional dentro do tempo da avaliação.**
