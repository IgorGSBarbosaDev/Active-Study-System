# Perguntas sobre Arrays + Strings

Data criação: 2026-09-19

## Diagnóstico inicial

- Pergunta: como encontrar o maior valor de um array?
- Síntese: reconhece a necessidade de percorrer e comparar com um maior armazenado, mas usou limites e operadores Java incorretos e inicialização que falha com negativos.
- Pergunta: como inverter uma string?
- Síntese: reconhece a necessidade de percorrer do final para o início, mas ainda não domina a criação/preenchimento da saída.
- Pergunta: como verificar palíndromo?
- Síntese: hipótese incorreta de que palíndromos precisam ter tamanho ímpar; ainda não apresentou o critério de comparação.
- Pergunta: como verificar anagrama?
- Síntese: não sabe ainda.
- Avaliação inicial: reconhece estruturas de repetição e comparação, nível 1. Principais gaps: sintaxe/índices, dois ponteiros, manipulação de strings, frequência e anagrama.

## Perguntas adaptativas

- Máximo/mínimo: após correção de inicialização, limites e operadores, compreendeu a passagem linear e identificou corretamente o menor valor entre negativos.
- Palíndromo: implementou corretamente dois ponteiros com assistência e reconheceu que strings de tamanho par também podem ser palíndromos.
- Reverse string: implementou corretamente o percurso reverso com `StringBuilder`.
- Frequência: corrigiu a criação do `HashMap`, `toCharArray()` e retorno após feedback.
- Anagrama: não conseguiu construir na primeira tentativa, mas compreendeu a comparação de frequências após a correção.
- Integração: corrigiu o escopo do contador e o retorno antecipado e implementou corretamente a contagem de palíndromos em um array.

## Resultado

Explicou corretamente o princípio de percorrer arrays, comparar valores, contar frequências e reconhecer anagramas. Implementou reverse string e a verificação integradora de palíndromos. A aplicação ainda depende de feedback para sintaxe Java e controle de fluxo em problemas novos, especialmente anagrama.

Status resultante: Praticando. Nível: 2 — entende e aplica com ajuda.

## Gaps identificados

- Reforçar aplicação autônoma de anagrama.
- Praticar escopo de variáveis, `return`, `break`, contadores e métodos Java.
- Resolver pelo menos um problema novo sem template e analisar tempo/espaço.

## Avaliações
