# Lista de exercícios — Arrays + Strings

Data criação: 2026-09-19
Data última atividade: 2026-09-19
Objetivo: praticar arrays, strings, dois ponteiros, frequência de caracteres e anagramas para o teste prático da iFuture/Coderbyte.
Quantidade: 12
Dificuldade: gradual — fácil a média, com desafio integrado
Fonte do conteúdo: `01_TOPICS/Arrays + Strings` e estratégia de preparação Coderbyte/iFuture.

## Instruções ao usuário

- Use Java.
- Inclua código em blocos e justifique decisões, complexidades e casos-limite.
- Respeite a política de consulta indicada em cada exercício.
- **Anotações permitidas:** pode consultar suas notas do tópico.
- **Exercícios anteriores permitidos:** pode consultar exercícios/códigos já resolvidos, mas explique o que reutilizou.
- **Sem consulta:** não consulte anotações, exercícios anteriores, documentação externa, busca ou IA.
- Não olhe soluções prontas. Se travar, registre a dificuldade e avance.
- Envie as respostas em lotes ou todas de uma vez. O feedback será registrado após cada lote solicitado.

## Exercícios

### 1. Maior e menor valor

**Consulta:** anotações permitidas; exercícios anteriores permitidos.

Implemente:

```java
int encontrarMaior(int[] valores)
int encontrarMenor(int[] valores)
```

Não ordene o array. As funções devem funcionar com valores negativos.

Teste com:

```text
{4, -2, 9, 1, -7}
```

Entregue também a complexidade de cada função.

### 2. Soma e contagem

**Consulta:** sem consulta.

Implemente:

```java
int somarPares(int[] valores)
int contarOcorrencias(int[] valores, int alvo)
```

Teste com:

```text
valores = {2, 5, 2, 8, 2, -4}
alvo = 2
```

Inclua um caso de teste com array vazio, se sua solução permitir essa entrada.

### 3. Inverter uma string

**Consulta:** anotações permitidas; exercícios anteriores não permitidos.

Implemente:

```java
String inverter(String texto)
```

Não use `StringBuilder.reverse()`.

Teste com:

```text
"Coderbyte"
"Java"
""
```

### 4. Verificar palíndromo

**Consulta:** sem consulta.

Implemente:

```java
boolean ehPalindromo(String texto)
```

Não crie uma segunda string invertida. Teste com:

```text
"radar" → true
"aa"    → true
"casa"  → false
""      → true
```

Explique a complexidade.

### 5. Contar palíndromos

**Consulta:** anotações permitidas; exercícios anteriores permitidos.

Implemente:

```java
int contarPalindromos(String[] palavras)
```

Teste com:

```text
{"radar", "casa", "aa", "java", "level"}
```

### 6. Frequência de caracteres

**Consulta:** anotações permitidas; exercícios anteriores não permitidos.

Implemente:

```java
Map<Character, Integer> contarCaracteres(String texto)
```

Teste com:

```text
"banana"
"abracadabra"
""
```

Explique como sua solução trata a primeira ocorrência de um caractere.

### 7. Primeiro caractere não repetido

**Consulta:** anotações permitidas; exercícios anteriores permitidos.

Implemente:

```java
Character primeiroNaoRepetido(String texto)
```

Retorne `null` se todos os caracteres forem repetidos ou se a string estiver vazia.

Teste com:

```text
"aabbcdd" → 'c'
"aabb"    → null
"swiss"   → 'w'
```

### 8. Verificar anagrama

**Consulta:** sem consulta.

Implemente:

```java
boolean saoAnagramas(String primeira, String segunda)
```

Não use ordenação. Teste com:

```text
"listen", "silent"  → true
"aab", "abb"        → false
"abc", "ab"         → false
"banana", "abnnaa"  → true
```

Explique como sua solução detecta um caractere ausente ou com frequência incorreta.

### 9. Contar anagramas de uma palavra

**Consulta:** anotações permitidas; exercícios anteriores permitidos.

Dado um array de palavras e uma palavra-alvo, implemente:

```java
int contarAnagramas(String[] palavras, String alvo)
```

Exemplo:

```text
palavras = {"listen", "silent", "hello", "enlist", "world"}
alvo = "listen"
resultado = 3
```

Informe a complexidade em função da quantidade e do tamanho das palavras.

### 10. Corrigir uma implementação

**Consulta:** sem consulta.

O código abaixo deve contar palíndromos, mas possui erros de escopo e controle de fluxo. Reescreva-o para funcionar e explique cada correção:

```java
int contarPalindromos(String[] palavras) {
    for (int i = 0; i < palavras.length; i++) {
        int contagem = 0;
        String texto = palavras[i];
        int esquerda = 0;
        int direita = texto.length() - 1;

        while (esquerda < direita) {
            if (texto.charAt(esquerda) != texto.charAt(direita)) {
                return 0;
            }
            esquerda++;
            direita--;
        }

        return contagem++;
    }

    return contagem;
}
```

### 11. Maior palavra palíndroma

**Consulta:** exercícios anteriores permitidos; anotações não permitidas.

Implemente:

```java
String maiorPalindromo(String[] palavras)
```

Retorne a maior palavra palíndroma. Em caso de empate, retorne a primeira. Defina o comportamento para array vazio.

Teste com:

```text
{"noon", "radar", "abc", "redivider"}
```

### 12. Simulado curto

**Consulta:** sem consulta. Tempo sugerido: 30 minutos.

Implemente:

```java
boolean contemDuplicata(int[] valores)
String primeiroMaiorQue(int[] valores, int limite)
```

Requisitos:

- `contemDuplicata` deve identificar se algum valor aparece mais de uma vez;
- `primeiroMaiorQue` deve retornar o primeiro valor maior que `limite`, convertido para `String`;
- retorne `null` se não houver valor maior;
- justifique a estrutura de dados escolhida e informe tempo e espaço.

## Tentativas

<!-- As respostas do usuário serão preservadas e associadas ao número do exercício. -->

### Exercício 1

```java
package exercicios.arraysstrings;

public class MaiorMenor {
    void main(){
        int[] arrays = {4, -2, 9, 1, -7};
        System.out.println(encontrarMaior(arrays));
        System.out.println(encontrarMenor(arrays));


    }
    int encontrarMaior(int [] valores){
        int valor = valores[0];
        for (int i = 1; i < valores.length; i++){
            if (valor < valores[i]){
                valor = valores[i];
            }
        }
        return valor;
    }

    int encontrarMenor(int [] valores){
        int valor = valores[0];
        for (int i = 1; i < valores.length; i++){
            if (valor > valores[i]){
                valor = valores[i];
            }
        }
        return valor;
    }
} // O(n) e O(1)
```

### Exercício 2

```java
package exercicios.arraysstrings;

public class Somacontagem {
    void main(){
        int[] valores = {2, 5, 2, 8, 2, -4};
        int[] arrayVazio = {0};
        System.out.println(somarPares(valores));
        System.out.println(somarPares(arrayVazio));
        System.out.println(contarOcorrencias(valores, 2));
        System.out.println(contarOcorrencias(arrayVazio, 2));
    }

    int somarPares(int[] valores){
        int soma = 0;
        for (int i = 0; i < valores.length; i++) {
            if (valores[i] % 2 == 0){
                soma+=valores[i];
            }
        }
        return soma;
    }

    int contarOcorrencias(int[] valores, int alvo){
        int ocorrencia = 0;
        for (int i = 0; i < valores.length; i++) {
            if (alvo == valores[i]) {
                ocorrencia++;
            }
        }
        return ocorrencia;
    }
}
```

### Exercício 3

```java
package exercicios.arraysstrings;

public class InverterString {
    void main(){
        System.out.println(inverter("texto"));
    }

    public String inverter(String txt){
        String stringInvertida = "";

        for (int i = txt.length() - 1; i >= 0; i--) {
            stringInvertida += txt.charAt(i);
        }
        return stringInvertida;
    }
}
```

### Exercício 4

```java
package exercicios.arraysstrings;

public class VerifPalindromo {
    void main(){

        System.out.println(ehPalindromo("casa"));
    }

    boolean ehPalindromo(String txt){
        int esquerda = 0;
        int direita = txt.length() -1;

        while(esquerda < direita){
            if (txt.charAt(esquerda) != txt.charAt(direita)){
                return false;
            }
            esquerda++;
            direita--;
        }
        return true;

    }
}
```

### Exercício 5

```java
package exercicios.arraysstrings;

public class ContadorPalindromo {
    void main(){
        String[] palavras = {"radar", "casa", "aa", "java", "level"};
        System.out.println(contarPalindromos(palavras));
    }

    public int contarPalindromos(String[] palavras){
        int contador = 0;
        for (int i = 0; i < palavras.length; i++) {
            String palavra = palavras[i];
            int direita = palavra.length() - 1;
            int esquerda = 0;
            boolean palindromo = true;

            while(esquerda < direita){
                if (palavra.charAt(esquerda) != palavra.charAt(direita)){
                    palindromo = false;
                    break;
                }
                esquerda++;
                direita--;
            }
            if (palindromo){
                contador++;
            }
        }
        return contador;
    }
}
```

## Feedback

### Exercício 1 — Correta

- Evidência: `encontrarMaior` e `encontrarMenor` inicializam com `valores[0]` e percorrem os demais elementos comparando corretamente.
- A solução funciona com valores negativos e usa uma passagem por função.
- Complexidade informada corretamente: `O(n)` tempo e `O(1)` espaço auxiliar.
- Observação: pressupõe array não vazio, o que não foi definido como caso obrigatório.

### Exercício 2 — Parcial

- Evidência: as duas funções implementam corretamente a soma dos pares e a contagem de ocorrências.
- `arrayVazio = {0}` não é vazio; é um array com um elemento zero. A implementação, entretanto, funcionaria para `{}`.
- Faltou registrar a complexidade: tempo `O(n)` e espaço auxiliar `O(1)` para cada função.
- Próximo foco: diferenciar um caso de entrada vazio de um caso contendo zero.

### Exercício 3 — Parcial

- Evidência: a função percorre do último índice ao primeiro e produz a string invertida corretamente.
- O uso de `stringInvertida += ...` dentro do loop funciona, mas pode gerar custo de tempo `O(n²)` por causa da imutabilidade de `String`.
- Para uma solução linear, use `StringBuilder`; tempo `O(n)` e espaço `O(n)`.
- Faltou testar a string vazia e declarar a complexidade.

### Exercício 4 — Parcial

- Evidência: a lógica de dois ponteiros está correta; retorna `false` ao encontrar diferença e `true` quando todas as comparações passam.
- A implementação também trata corretamente string vazia e strings de tamanho par.
- Faltaram os demais testes solicitados e a declaração da complexidade: `O(n)` tempo e `O(1)` espaço auxiliar.

### Exercício 5 — Parcial

- Evidência: o contador está fora do loop, a flag é reiniciada para cada palavra e a contagem só aumenta quando a palavra é palíndroma.
- Para o caso fornecido, o resultado esperado é `3` (`radar`, `aa`, `level`).
- Faltou declarar a complexidade: `O(T)` tempo, em que `T` é o total de caracteres das palavras, e `O(1)` espaço auxiliar.
- Não há erro conceitual na implementação apresentada.

### Resumo do lote

- Corretas: 1
- Parciais: 4
- Incorretas: 0
- Não respondidas: 0

O raciocínio central dos cinco exercícios está correto. As principais melhorias são análise de complexidade, cobertura de testes e escolha de `StringBuilder` para evitar custo quadrático.

## Resumo

Lista aberta. 5 de 12 exercícios respondidos e corrigidos; próximos itens: exercícios 6 a 12.

## Minhas anotações

<!-- USER-NOTES:START -->

<!-- USER-NOTES:END -->
