# Contexto Estratégico — Estudos de Engenharia de Software

> **Função deste arquivo:** registrar apenas o contexto que deve orientar decisões de estudo: situação atual, direção profissional, lacunas, sinais de mercado e prioridades estratégicas.
>
> Método de aprendizagem, comportamento do agente e sequência detalhada de estudos pertencem a outros arquivos.

**Última revisão:** setembro de 2026

---

## 1. Objetivo

Os estudos devem atender simultaneamente a dois objetivos:

1. desenvolver domínio sólido de Programação, Ciência da Computação e Engenharia de Software, da teoria à prática;
2. transformar esse domínio em vantagem profissional, aumentando a capacidade de disputar vagas melhores e demonstrar competência técnica.

O foco não é acumular tecnologias. É desenvolver capacidade de compreender problemas, implementar soluções, justificar decisões, diagnosticar falhas e trabalhar com sistemas reais.

---

## 2. Situação atual

### Formação e experiência

- Graduação em Engenharia de Software, com conclusão prevista para o final de 2027.
- Experiência profissional atual em estágio na Usiminas.
- Já possui experiência prática com desenvolvimento, automações, integrações e resolução de problemas em ambiente corporativo.

### Especialização atual

**Stack principal:** Backend Java + Spring.

Experiência já existente com:

- Java e ecossistema Spring;
- APIs REST e HTTP;
- JPA/Hibernate e persistência;
- SQL e bancos relacionais, principalmente PostgreSQL/MySQL;
- Collections, Streams, Exceptions e Generics;
- conceitos de arquitetura e Design Patterns.

**Stack complementar:** TypeScript/Node.js, principalmente para aplicações web, ferramentas e projetos full stack.

### Diagnóstico atual

O principal gargalo não é falta de contato com tecnologias, mas **profundidade técnica**.

Já existe familiaridade suficiente para construir aplicações, porém ainda é necessário aprofundar os fundamentos e entender melhor o comportamento das tecnologias abaixo das abstrações dos frameworks.

---

## 3. Principais lacunas

As lacunas mais relevantes para a evolução profissional atual são:

- fundamentos de Ciência da Computação;
- estruturas de dados, algoritmos e complexidade;
- memória, processos, threads e redes;
- Java/JVM e concorrência;
- funcionamento interno do Spring;
- SQL, transações, índices e comportamento do JPA/Hibernate;
- estratégia profissional de testes;
- Linux, containers, CI/CD e cloud;
- segurança de aplicações;
- arquitetura de software;
- Redis, mensageria e sistemas distribuídos;
- observabilidade, diagnóstico e performance.

Essas lacunas não possuem a mesma prioridade. A ordem detalhada deve ser definida pelo roadmap.

---

## 4. Direção profissional

O posicionamento desejado é:

> **Engenheiro de Software / Backend Java com fundamentos fortes, domínio do ecossistema Spring e capacidade de projetar, implementar, testar, publicar, observar e evoluir sistemas reais.**

A especialização principal deve continuar sendo **Java + Spring**.

TypeScript permanece como competência complementar, sem competir com a especialização principal.

O objetivo de médio prazo não é apenas conhecer uma stack, mas conseguir justificar decisões envolvendo:

- estruturas de dados e algoritmos;
- persistência e modelagem;
- arquitetura;
- concorrência;
- segurança;
- testes;
- infraestrutura;
- performance;
- sistemas distribuídos.

---

## 5. Contexto atual do mercado

Os dados públicos mais recentes disponíveis em larga escala reforçam a estratégia atual.

### Java e Spring continuam relevantes

O **State of Java 2025**, da JetBrains, apontou o Spring como principal framework web do ecossistema Java entre os respondentes, com aproximadamente **65% de uso**. Java também permanece fortemente presente em desenvolvimento de microsserviços.

**Implicação:** aprofundar Java/Spring continua sendo uma especialização defensável, principalmente para backend e sistemas empresariais.

### Infraestrutura deixou de ser diferencial opcional

Na **Stack Overflow Developer Survey 2025**, Docker atingiu aproximadamente **71% de uso** entre tecnologias de cloud/desenvolvimento de infraestrutura, com forte crescimento em relação ao ano anterior. AWS também permanece entre as principais plataformas utilizadas.

**Implicação:** saber apenas implementar uma API é insuficiente. Backend profissional exige capacidade de testar, containerizar, configurar e publicar aplicações.

### PostgreSQL permanece estratégico

A pesquisa do Stack Overflow de 2025 manteve PostgreSQL entre os bancos com maior interesse e preferência entre desenvolvedores.

**Implicação:** aprofundar SQL, índices, transações, concorrência e PostgreSQL gera mais valor agora do que acumular vários bancos diferentes superficialmente.

### TypeScript continua relevante como stack complementar

O GitHub Octoverse 2025 colocou TypeScript na primeira posição por número de contribuidores no GitHub naquele período.

**Implicação:** manter TypeScript como segunda stack é útil, mas não existe motivo estratégico para abandonar a especialização em Java.

### IA aumenta a importância dos fundamentos

Ferramentas de IA já fazem parte do fluxo de desenvolvimento, mas pesquisas recentes também mostram baixa confiança dos desenvolvedores em respostas geradas automaticamente.

**Implicação:** geração de código tende a ficar mais barata. A vantagem profissional passa cada vez mais por saber revisar, validar, diagnosticar, projetar e justificar soluções.

### Limite desses sinais

Esses dados são majoritariamente globais e não representam diretamente o mercado brasileiro.

Para decisões específicas de carreira, tecnologias ou vagas, devem ser combinados com amostras periódicas das vagas reais que o usuário pretende disputar.

---

## 6. Sinais práticos de empregabilidade para desenvolvedores juniores

Além dos dados gerais de mercado, o relato analisado no vídeo do Galego mostra alguns fatores que diferenciaram desenvolvedores juniores que conseguiram entrar no mercado.

Os pontos mais relevantes foram:

- **experiência prévia**, mesmo em início de carreira, como evidência de já ter lidado com problemas reais;
- **projetos de portfólio**, usados para demonstrar capacidade prática em vez de apenas listar tecnologias;
- **curiosidade e disposição para aprender**, mostrando interesse em entender além do necessário para concluir uma tarefa;
- **entendimento aprofundado dos conceitos utilizados nos próprios projetos**;
- capacidade de explicar **por que uma decisão técnica foi tomada**, e não apenas como implementar;
- capacidade de explicar as consequências de uma alternativa diferente — por exemplo, por que uma fila foi utilizada e o que mudaria se outra estrutura fosse escolhida;
- capacidade de relatar **problemas técnicos reais encontrados**, como foram investigados e como foram resolvidos.

O sinal mais importante para este plano é que um júnior não precisa necessariamente conhecer uma quantidade enorme de tecnologias. É mais valioso conseguir discutir com profundidade aquilo que afirma conhecer.

### Implicação para os estudos

Os estudos e projetos devem desenvolver capacidade de responder, sobre aquilo que foi implementado:

- qual problema estava sendo resolvido;
- por que aquela solução foi escolhida;
- quais alternativas existiam;
- quais trade-offs estavam envolvidos;
- o que poderia dar errado;
- quais problemas apareceram durante a implementação;
- como esses problemas foram diagnosticados e resolvidos.

Projetos de portfólio devem servir como **evidência de raciocínio técnico**, e não apenas como demonstração de stack.

Esse princípio reforça a estratégia de priorizar **profundidade, projetos reais e capacidade de explicar decisões técnicas** em vez de estudar tecnologias superficialmente apenas para adicioná-las ao currículo.

**Fonte qualitativa:** vídeo analisado do Galego — https://www.youtube.com/watch?v=-xhdkDlPBwk

---

## 7. Prioridades estratégicas

No momento, a estratégia deve privilegiar:

1. **profundidade antes de amplitude** — dominar conceitos importantes em vez de acumular tecnologias;
2. **fundamentos antes de abstrações avançadas** — entender os problemas antes de estudar ferramentas que os escondem;
3. **Java/Spring como especialização principal**;
4. **banco de dados, testes e infraestrutura como competências obrigatórias de backend**;
5. **arquitetura e sistemas distribuídos somente após consolidar os fundamentos necessários**;
6. **aplicação prática** — conhecimento relevante deve aparecer em projetos, decisões técnicas ou resolução de problemas;
7. **capacidade de explicar decisões** — saber dizer por que uma solução foi escolhida, quais alternativas existiam e quais consequências ela possui.

---

## 8. Uso estratégico da experiência profissional

A experiência profissional atual deve ser aproveitada principalmente para desenvolver competências transferíveis:

- entendimento de problemas reais;
- levantamento e análise de requisitos;
- comunicação com pessoas técnicas e não técnicas;
- automação e integração de sistemas;
- confiabilidade;
- documentação;
- debugging;
- entrega de valor.

Experiências corporativas podem inspirar estudos e projetos próprios, mas informações internas, dados, código proprietário ou arquitetura não autorizada não devem ser publicados.

---

## 9. Critério para novas tecnologias

Uma nova tecnologia merece prioridade quando pelo menos uma destas condições for relevante:

- resolve um problema que ainda não se sabe resolver adequadamente;
- aparece com frequência nas vagas-alvo;
- ensina um conceito importante e transferível;
- será aplicada em um projeto real;
- é requisito para avançar em um tópico estratégico posterior.

Evitar estudar tecnologias apenas para aumentar a lista do currículo.

---

## 10. Diretriz final

A pergunta principal para orientar os estudos não deve ser:

> “Quantas tecnologias eu conheço?”

Mas:

> **“Quais problemas importantes de engenharia de software eu consigo compreender, resolver, testar, explicar e operar?”**

---

## Referências de mercado

- JetBrains — State of Java 2025: https://lp.jetbrains.com/the-state-of-java-2025/
- Stack Overflow Developer Survey 2025: https://survey.stackoverflow.co/2025/
- GitHub Octoverse 2025: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
