# Arrays + Strings

Data criação: 2026-09-19
Data último estudo: 2026-09-19
Data última revisão: 2026-09-20
Data próxima revisão: 2026-09-21
Status: Praticando
Nível: 2

## Conteúdo

- Arrays são percorridos com `for`, usando índices de `0` até `length - 1`.
- Máximo/mínimo podem ser encontrados em uma passagem, mantendo o melhor valor atual; tempo `O(n)` e espaço auxiliar `O(1)`.
- Para evitar falha com valores negativos, inicializa-se o melhor valor com `array[0]`.
- Strings podem ser invertidas percorrendo do último caractere ao primeiro com `StringBuilder`; tempo e espaço `O(n)`.
- Palíndromo pode ser verificado com dois ponteiros nas extremidades; tempo `O(n)` e espaço `O(1)`.
- Frequência de caracteres usa `HashMap<Character, Integer>` e `getOrDefault`.
- Anagrama exige mesmo tamanho e mesmas frequências; solução com um mapa em tempo `O(n)`.
- Foi aplicada a combinação de percurso de array com verificação de palíndromo para contar palavras palíndromas.

## Gaps

- Aplicar sintaxe e controle de fluxo sem assistência, especialmente escopo de variáveis, `return`, `break` e contadores.
- Reconhecer e implementar anagrama de forma autônoma em um novo problema.
- Praticar edge cases: strings vazias, valores negativos, caracteres repetidos e entrada nula.
- Declarar e justificar complexidade em soluções práticas.
- Distinguir array vazio de array contendo zero e ampliar a cobertura de testes.

## Erros

- Usou `array.length()` e `i <= array.length`; em arrays Java é `array.length` e o limite correto é `i < array.length`.
- Usou `maior == array[i]`; `==` compara, enquanto atribuição usa `=`.
- Inicializar `maior` com `0` falha quando todos os valores são negativos; preferir `array[0]` ou `Integer.MIN_VALUE`.
- Supôs que palíndromos precisam ter quantidade ímpar de letras; strings como `"aa"` também são palíndromos.
- Tentativa de `array2[].add(i)` mistura array fixo com lista e não define corretamente os elementos a copiar.
- Na contagem de palíndromos, reiniciou o contador por palavra e retornou antes de processar o array; modelo corrigido: contador fora do loop e retorno somente ao final.
- Na frequência/anagrama, precisou de assistência para sintaxe de `HashMap`, chamada `toCharArray()`, retorno do mapa e decremento das frequências.
- Usou concatenação de `String` dentro de um loop ao inverter texto; funciona, mas pode gerar `O(n²)`, enquanto `StringBuilder` permite `O(n)`.
- Nas primeiras cinco respostas da lista, deixou complexidades ou cobertura de testes incompletas; modelo a reforçar: toda solução deve informar tempo/espaço e verificar casos-limite relevantes.

## Minhas anotações

<!-- USER-NOTES:START -->

<!-- USER-NOTES:END -->