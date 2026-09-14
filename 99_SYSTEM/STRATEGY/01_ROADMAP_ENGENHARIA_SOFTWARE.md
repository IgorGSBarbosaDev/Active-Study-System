# Roadmap — Engenharia de Software

> Objetivo: evoluir de desenvolvedor backend com boa familiaridade com Java/Spring para engenheiro de software capaz de compreender fundamentos, projetar sistemas, implementar, testar, publicar, observar e justificar decisões técnicas.

---

# Como usar este roadmap

Não estudar todas as fases simultaneamente.

Para cada tópico:

1. estudar teoria;
2. implementar um exemplo mínimo;
3. aplicar em um projeto;
4. testar;
5. provocar falhas;
6. diagnosticar;
7. registrar trade-offs;
8. produzir uma evidência de aprendizado quando fizer sentido.

Critério de saída de uma fase:

> conseguir explicar e implementar os conceitos principais sem depender da IA para tomar as decisões centrais.

---

# Fase 1 — Fundamentos de Ciência da Computação

## Objetivo

Construir a base que permite entender o que acontece abaixo dos frameworks.

## 1.1 Complexidade e algoritmos

Estudar:

- custo de tempo;
- custo de memória;
- Big O;
- Big Ω e Big Θ em nível conceitual;
- análise de loops;
- recursão;
- busca linear;
- busca binária;
- principais algoritmos de ordenação;
- comparação entre algoritmos.

Dominar pelo menos:

- Bubble Sort — para entendimento;
- Selection Sort;
- Insertion Sort;
- Merge Sort;
- Quick Sort;
- busca binária.

### Saber responder

- Por que busca binária é O(log n)?
- Por que ela exige dados ordenados?
- Quando O(n) pode ser perfeitamente aceitável?
- Qual a diferença prática entre O(n), O(log n) e O(n²)?

---

## 1.2 Estruturas de dados

Estudar:

- arrays;
- linked lists;
- stacks;
- queues;
- hash tables;
- sets;
- trees;
- binary search trees;
- heaps;
- graphs.

Relacionar com Java:

- ArrayList;
- LinkedList;
- ArrayDeque;
- HashMap;
- HashSet;
- TreeMap;
- TreeSet;
- PriorityQueue.

### Prática

Implementar manualmente versões simples de:

- lista;
- stack;
- queue;
- hash table;
- binary search tree.

Depois comparar com as Collections do Java.

---

## 1.3 Memória e execução de programas

Estudar:

- bits e bytes;
- endereçamento;
- stack;
- heap;
- referências;
- alocação;
- garbage collection;
- call stack;
- stack frame;
- memory leak;
- garbage collector.

### Resultado esperado

Conseguir explicar o que acontece com memória durante uma chamada como:

```java
User user = new User("Igor");
service.save(user);
```

---

## 1.4 Sistemas Operacionais

Estudar:

- kernel;
- user space;
- processos;
- threads;
- context switching;
- scheduling;
- system calls;
- arquivos;
- file descriptors;
- memória virtual;
- paginação;
- concorrência;
- deadlock.

Não é necessário estudar implementação de kernel neste momento.

---

## 1.5 Redes

Estudar na seguinte ordem:

1. modelo cliente-servidor;
2. IP;
3. portas;
4. TCP;
5. UDP;
6. DNS;
7. HTTP;
8. HTTPS;
9. TLS;
10. sockets;
11. NAT;
12. firewall;
13. proxy;
14. reverse proxy;
15. load balancer;
16. VPN.

### Saber explicar

O caminho aproximado de:

```text
https://api.exemplo.com/users
```

até chegar a uma aplicação Spring Boot.

---

## Entregável da Fase 1

Criar um repositório:

`computer-science-foundations`

Com:

- implementações de estruturas de dados;
- algoritmos;
- pequenos experimentos;
- explicações curtas;
- diagramas.

### Evidência pública opcional

Post/vídeo:

> “O que acontece da URL até o Controller do Spring?”

---

# Fase 2 — Java Profundo e JVM

## Objetivo

Transformar Java de linguagem familiar em linguagem de especialização.

## 2.1 Java Core

Revisar e aprofundar:

- tipos;
- objetos;
- imutabilidade;
- equals/hashCode;
- records;
- enums;
- exceptions;
- generics;
- collections;
- streams;
- Optional;
- lambdas;
- interfaces funcionais.

---

## 2.2 JVM

Estudar:

- compilação Java;
- bytecode;
- JVM;
- JIT;
- ClassLoader;
- heap;
- stacks por thread;
- metaspace;
- garbage collectors;
- referências strong/weak;
- profiling básico.

Fluxo:

```text
.java
  ↓
javac
  ↓
.class / bytecode
  ↓
JVM
  ↓
JIT
  ↓
código de máquina
```

---

## 2.3 Concorrência

Estudar:

- Thread;
- Runnable;
- Callable;
- ExecutorService;
- Future;
- CompletableFuture;
- synchronized;
- locks;
- volatile;
- atomics;
- ConcurrentHashMap;
- thread pools;
- race condition;
- deadlock;
- starvation;
- thread safety;
- Java Memory Model em nível aplicado.

### Projeto prático

Criar pequenos experimentos que provoquem:

- race condition;
- deadlock;
- problemas de visibilidade.

Depois corrigir cada um.

---

# Fase 3 — Web e Spring por dentro

## Objetivo

Parar de conhecer apenas as annotations e compreender o framework.

## 3.1 HTTP aprofundado

Estudar:

- métodos;
- status codes;
- headers;
- body;
- content negotiation;
- caching HTTP;
- idempotência;
- cookies;
- sessions;
- CORS;
- REST;
- paginação;
- versionamento de API.

---

## 3.2 Spring Core

Estudar:

- IoC;
- Dependency Injection;
- ApplicationContext;
- Beans;
- escopos;
- Bean lifecycle;
- Component Scan;
- proxies;
- AOP;
- configuration.

Entender o que realmente acontece com:

```java
@Service
@Transactional
@Cacheable
@Async
```

---

## 3.3 Spring MVC

Aprofundar:

- DispatcherServlet;
- filtros;
- interceptors;
- argument resolvers;
- exception handlers;
- validação;
- serialização/deserialização.

---

## 3.4 Spring Security

Aprofundar:

- Authentication;
- Authorization;
- SecurityFilterChain;
- PasswordEncoder;
- sessions;
- JWT;
- OAuth 2.0;
- OpenID Connect;
- method security.

---

# Fase 4 — Bancos de Dados e Persistência

## Objetivo

Sair do nível “sei SQL/JPA” para “sei projetar e diagnosticar persistência”.

## 4.1 SQL avançado

Estudar:

- joins;
- subqueries;
- CTE;
- window functions;
- aggregation;
- indexes;
- índices compostos;
- query planner;
- execution plan.

Usar:

```sql
EXPLAIN ANALYZE
```

---

## 4.2 Bancos relacionais

Estudar:

- ACID;
- transactions;
- isolation levels;
- locks;
- deadlocks;
- MVCC;
- B-Tree;
- constraints;
- normalização;
- denormalização;
- optimistic locking;
- pessimistic locking.

---

## 4.3 JPA/Hibernate profundo

Estudar:

- persistence context;
- entity lifecycle;
- dirty checking;
- lazy/eager loading;
- N+1;
- cascade;
- orphan removal;
- JPQL;
- native queries;
- batching;
- transactions.

---

## Projeto

Criar uma API com PostgreSQL e:

- consultas não triviais;
- índices;
- medição antes/depois;
- transações;
- concorrência;
- problemas N+1 intencionais e correção.

---

# Fase 5 — Testes e Qualidade

## Objetivo

Ser capaz de modificar software com confiança.

Estudar:

- JUnit;
- assertions;
- Mockito;
- mocks;
- stubs;
- spies;
- unit tests;
- integration tests;
- API tests;
- repository tests;
- E2E;
- test pyramid;
- fixtures;
- coverage;
- mutation testing em nível introdutório.

## Spring

Dominar:

- `@SpringBootTest`;
- `@WebMvcTest`;
- `@DataJpaTest`;
- MockMvc;
- Testcontainers.

## Projeto

Subir PostgreSQL real em container durante testes.

Depois adicionar Redis real com Testcontainers em uma fase futura.

---

# Fase 6 — Design de Software

## Objetivo

Aprender a organizar código para mudança.

## 6.1 Princípios

Estudar:

- SOLID;
- DRY;
- KISS;
- YAGNI;
- Separation of Concerns;
- high cohesion;
- low coupling;
- composition over inheritance;
- dependency inversion.

---

## 6.2 Design Patterns

Estudar primeiro:

1. Strategy;
2. Factory Method;
3. Builder;
4. Adapter;
5. Facade;
6. Observer;
7. Decorator;
8. Command;
9. Template Method;
10. Singleton.

Para cada padrão:

- problema;
- estrutura;
- exemplo;
- trade-offs;
- quando não usar.

Não decorar padrões.

---

## 6.3 Refactoring

Estudar:

- code smells;
- extract method;
- extract class;
- replace conditional with polymorphism;
- dependency inversion;
- refactoring seguro com testes.

---

# Fase 7 — Arquitetura de Software

## Objetivo

Compreender diferentes formas de estruturar sistemas e seus custos.

Ordem:

1. Layered Architecture;
2. MVC / MVP / MVVM — entendendo que são padrões ligados principalmente à apresentação;
3. monólito tradicional;
4. Modular Monolith;
5. Hexagonal Architecture;
6. Onion Architecture;
7. Clean Architecture;
8. DDD;
9. Event-Driven Architecture;
10. Microservices.

## Prioridade

Construir um **Monólito Modular** antes de construir microsserviços.

### Estudar também

- módulos;
- boundaries;
- coupling;
- cohesion;
- dependency rules;
- ports and adapters;
- bounded contexts;
- aggregates;
- domain services;
- application services.

---

# Fase 8 — Linux, Docker e CI/CD

## Objetivo

Conseguir executar e publicar software sem depender da IDE.

## Linux

Estudar:

- filesystem;
- permissions;
- users;
- processes;
- environment variables;
- ports;
- SSH;
- curl;
- grep;
- pipes;
- logs;
- systemd em nível básico.

---

## Docker

Dominar:

- images;
- containers;
- Dockerfile;
- layers;
- volumes;
- networks;
- environment variables;
- Docker Compose;
- multi-stage build.

Projeto mínimo:

```text
Spring Boot
PostgreSQL
Redis
```

subindo com:

```bash
docker compose up
```

---

## CI/CD

Começar por GitHub Actions:

```text
push
 ↓
build
 ↓
tests
 ↓
package
 ↓
docker image
 ↓
deploy
```

---

# Fase 9 — Redis e NoSQL

## Objetivo

Aprender bancos não relacionais a partir dos problemas que resolvem.

## 9.1 Redis

Estudar:

- key-value;
- TTL;
- eviction;
- cache-aside;
- write-through;
- write-behind em nível conceitual;
- cache invalidation;
- session storage;
- rate limiting;
- distributed locks;
- pub/sub;
- persistence;
- failure scenarios.

### Prática

Implementar cache-aside em uma API Spring.

Depois provocar:

- stale cache;
- Redis indisponível;
- cache stampede;
- expiração simultânea.

---

## 9.2 NoSQL

Primeiro entender as categorias:

- document;
- key-value;
- wide-column;
- graph.

Depois estudar MongoDB:

- documents;
- collections;
- embedding;
- references;
- indexes;
- aggregation;
- consistência;
- modelagem orientada a acesso.

### Pergunta central

> Por que eu escolheria MongoDB em vez de PostgreSQL para este problema?

Se não houver resposta concreta, PostgreSQL pode continuar sendo a melhor escolha.

---

# Fase 10 — Segurança de Aplicações

## Objetivo

Entender segurança além das configurações do Spring Security.

Estudar:

- authentication;
- authorization;
- password hashing;
- salts;
- sessions;
- cookies;
- JWT;
- OAuth 2.0;
- OpenID Connect;
- TLS;
- CORS;
- CSRF;
- XSS;
- SQL Injection;
- SSRF;
- secrets;
- rate limiting;
- least privilege.

Estudar o OWASP Top 10 atual.

---

# Fase 11 — Mensageria e Sistemas Distribuídos

## Objetivo

Aprender os problemas que aparecem quando o sistema deixa de ser uma única aplicação.

Começar por conceitos:

- synchronous vs asynchronous communication;
- message queues;
- events;
- producers;
- consumers;
- retries;
- idempotency;
- ordering;
- delivery guarantees;
- eventual consistency.

Depois ferramentas:

1. RabbitMQ;
2. Kafka.

Não é obrigatório dominar as duas igualmente.

---

## Conceitos distribuídos

Estudar:

- CAP theorem;
- consistency;
- availability;
- partitions;
- eventual consistency;
- retries;
- exponential backoff;
- timeout;
- circuit breaker;
- bulkhead;
- distributed locks;
- distributed transactions;
- Saga;
- Transactional Outbox.

---

# Fase 12 — Microsserviços

## Pré-requisito

Só iniciar depois de compreender minimamente:

- Docker;
- redes;
- mensageria;
- transações;
- observabilidade;
- consistência;
- retries;
- segurança;
- CI/CD.

Estudar:

- service boundaries;
- database per service;
- API Gateway;
- service discovery em nível conceitual;
- synchronous communication;
- asynchronous communication;
- resilience;
- distributed tracing;
- configuration;
- secrets.

## Projeto

Extrair conscientemente partes de um monólito modular para serviços separados.

Não começar criando 10 serviços vazios.

---

# Fase 13 — Observabilidade e Performance

## Objetivo

Aprender a responder:

> “O sistema está lento ou falhando. Onde está o problema?”

Estudar os três pilares:

- logs;
- metrics;
- traces.

Ferramentas/conceitos:

- structured logging;
- correlation ID;
- Micrometer;
- Prometheus;
- Grafana;
- OpenTelemetry;
- distributed tracing.

## Performance

Estudar:

- profiling;
- CPU;
- memória;
- GC;
- queries;
- latency;
- throughput;
- load testing;
- bottlenecks.

Ferramentas possíveis:

- JFR;
- VisualVM;
- JMeter ou k6.

---

# Fase 14 — Cloud

## Objetivo

Entender como aplicações modernas são hospedadas e operadas.

Como foco inicial, escolher uma cloud. AWS é uma boa candidata.

Aprender primeiro os conceitos e serviços equivalentes a:

- compute;
- virtual machines;
- object storage;
- managed databases;
- networking;
- IAM;
- load balancers;
- containers;
- monitoring;
- secrets.

Não tentar decorar dezenas de serviços.

---

# Fase 15 — System Design

## Objetivo

Integrar todo o conhecimento anterior para projetar sistemas.

Estudar:

- requisitos funcionais;
- requisitos não funcionais;
- capacity estimation;
- latency;
- throughput;
- availability;
- caching;
- load balancing;
- databases;
- replication;
- partitioning;
- queues;
- CDN;
- consistency;
- failure scenarios.

Exercícios:

- URL shortener;
- chat;
- e-commerce;
- sistema de pagamentos;
- notificações;
- armazenamento de arquivos.

---

# Fase 16 — Engenharia de Software

Esta fase ocorre em paralelo às demais, mas deve ganhar profundidade progressivamente.

Estudar:

## Requisitos

- requisitos funcionais;
- requisitos não funcionais;
- user stories;
- use cases;
- critérios de aceite.

## Modelagem e documentação

- UML;
- C4 Model;
- ADR;
- documentação de APIs;
- arquitetura.

## Processo de desenvolvimento

- Git;
- code review;
- branching strategies;
- semantic versioning;
- release management;
- technical debt;
- refactoring;
- manutenção.

## Trabalho profissional

- debugging;
- incident analysis;
- root cause analysis;
- comunicação técnica;
- estimativas;
- trade-offs;
- priorização.

---

# Trilha de Mercado — Executar em paralelo

Conhecimento sem evidência é difícil de avaliar externamente.

## GitHub

Manter poucos projetos fortes.

Cada projeto relevante deve possuir:

- README profissional;
- objetivo;
- arquitetura;
- stack;
- como executar;
- testes;
- decisões técnicas;
- screenshots/diagramas quando relevantes;
- deploy quando viável.

---

## Conteúdo

Transformar estudos importantes em conteúdo.

Formatos:

- post curto;
- artigo;
- vídeo de 2–5 minutos;
- vídeo técnico maior;
- demo de projeto.

### Conteúdo recomendado

Priorizar:

- explicações de algo que implementou;
- comparações;
- debugging real;
- arquitetura;
- performance;
- testes;
- decisões técnicas.

Evitar posts genéricos do tipo:

> “Hoje aprendi Redis.”

Preferir:

> “Implementei cache-aside com Redis e encontrei três problemas de consistência.”

---

## LinkedIn

Usar para:

- projetos;
- aprendizados relevantes;
- experiências técnicas;
- artigos;
- vídeos;
- networking;
- interação técnica.

Não transformar o perfil em diário de cada aula assistida.

---

## Portfólio

Objetivo mínimo até a conclusão da graduação:

### Projeto 1 — Backend profissional

- Spring Boot;
- PostgreSQL;
- Redis;
- testes;
- Docker;
- CI/CD;
- segurança;
- observabilidade;
- deploy.

### Projeto 2 — Monólito Modular

- domínio mais complexo;
- módulos;
- arquitetura;
- ADRs;
- testes;
- mensageria opcional.

### Projeto 3 — Sistemas Distribuídos

- 2–4 serviços;
- mensageria;
- consistência;
- resilience;
- tracing;
- containers;
- deploy.

Projetos menores podem existir, mas esses devem servir como projetos âncora.

---

# Ordem resumida

```text
1. Fundamentos de Ciência da Computação
        ↓
2. Java profundo + JVM + concorrência
        ↓
3. HTTP + Spring por dentro
        ↓
4. SQL + PostgreSQL + JPA/Hibernate profundo
        ↓
5. Testes
        ↓
6. Design de Software
        ↓
7. Arquitetura
        ↓
8. Linux + Docker + CI/CD
        ↓
9. Redis + NoSQL
        ↓
10. Segurança
        ↓
11. Mensageria + Sistemas Distribuídos
        ↓
12. Microsserviços
        ↓
13. Observabilidade + Performance
        ↓
14. Cloud
        ↓
15. System Design
```

`Engenharia de Software`, `Git`, comunicação técnica, projetos e posicionamento de mercado ocorrem em paralelo.

---

# Prioridade imediata

A primeira etapa é exatamente a que foi identificada:

## Fundamentos de Ciência da Computação

Ordem interna recomendada:

```text
Complexidade
    ↓
Estruturas de Dados
    ↓
Algoritmos
    ↓
Memória
    ↓
Sistemas Operacionais
    ↓
Processos e Threads
    ↓
Redes
    ↓
TCP / UDP
    ↓
DNS
    ↓
HTTP / HTTPS / TLS
```

Não é necessário dominar toda Ciência da Computação antes de voltar ao Java.

Quando essa base inicial estiver razoavelmente clara, seguir para Java/JVM e continuar aprofundando fundamentos em paralelo.

---

# Método de acompanhamento

Para cada tópico, registrar:

```md
## Tópico

Status: Não iniciado | Estudando | Praticando | Consolidado

### Conceito

### Como funciona

### Implementação

### Trade-offs

### Quando usar

### Quando não usar

### Falhas comuns

### Exercício

### Projeto onde apliquei

### Evidência pública

### Perguntas que ainda não sei responder
```

---

# Uso da Alura

Quando existir formação ou curso adequado, usar a Alura como uma das fontes estruturadas de estudo.

Ela não deve ser a única fonte.

Combinar:

1. curso/aula para estrutura;
2. documentação oficial;
3. implementação própria;
4. projeto;
5. revisão e aprofundamento.

---

# Regra final do roadmap

Não otimizar para:

> “quantas tecnologias eu conheço?”

Otimizar para:

> “quantos problemas importantes eu consigo compreender, resolver, testar, explicar e operar?”
