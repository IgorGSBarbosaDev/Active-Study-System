# Roadmap de Estudos - Engenharia de Software para Estágio/Júnior em Big Tech e Fintech

> Objetivo: chegar a processos seletivos de Mercado Livre, iFood, Nubank, Itaú e empresas similares com nível técnico percebido de **Software Engineer Júnior**, mesmo concorrendo a vagas de estágio.

## Como usar este guia

- **Stack principal:** Java 21+ e Spring Boot.
- **Regra central:** profundidade > quantidade de tecnologias.
- Não avance apenas porque "vi o conteúdo". Avance quando conseguir **explicar, implementar e justificar trade-offs**.
- Todo bloco estudado deve gerar alguma evidência prática: código, teste, benchmark, ADR, diagrama ou melhoria mensurável em projeto.
- Use **MarketRoute como projeto principal** para consolidar boa parte da trilha.
- Em paralelo, mantenha treino leve de algoritmos e entrevistas: **3 problemas por semana**.

> Este arquivo é um complemento orientado ao mercado, às práticas e às evidências de portfólio. A sequência canônica de dependências está em `01_ROADMAP_ENGENHARIA_SOFTWARE.md`; portanto, não trate este documento como um segundo calendário independente.

> Dependências importantes: Docker e CI/CD devem estar disponíveis antes de aprofundar Redis, Kafka e sistemas distribuídos; segurança começa com Spring/API e é aprofundada antes de cloud e sistemas distribuídos; sistemas operacionais e redes continuam sendo estudados junto dos fundamentos.

---

# Organização temática

## 0. Base de trabalho do engenheiro

### Estudar
- Git e GitHub
  - commit, branch, merge, rebase
  - pull request e code review
  - resolução de conflitos
- Linux/terminal
  - navegação, processos, portas, variáveis de ambiente
  - `curl`, `grep`, `ps`, `top`, `lsof`
- HTTP
  - métodos, status codes, headers
  - request/response
  - cookies, CORS e HTTPS em alto nível
- JSON e serialização

### Prática
- Trabalhar sempre via Git em projetos reais.
- Abrir PRs para as próprias features e revisar o diff antes do merge.
- Testar APIs também com `curl`, não somente Postman.

### Critério para avançar
Você consegue explicar o caminho de uma requisição HTTP e diagnosticar erros básicos de porta, status code, CORS e configuração.

---

## 1. Estruturas de Dados, Algoritmos e Big O

**Prioridade: máxima.**

### Estudar
- Arrays e ArrayList
- LinkedList
- HashMap e HashSet
- Stack
- Queue e Deque
- Heap / PriorityQueue
- Trees
- Graphs
- Recursão
- Binary Search
- BFS e DFS
- Sorting
- Two Pointers
- Sliding Window
- Hashing

### Complexidade
- O(1)
- O(log n)
- O(n)
- O(n log n)
- O(n^2)
- complexidade de espaço
- trade-off tempo x memória

### Prática
- Resolver aproximadamente **50-80 problemas bem escolhidos** ao longo da trilha.
- Implementar BFS, DFS, Dijkstra e estruturas basicas sem copiar.
- Para cada solução, responder:
  1. Qual estrutura de dados foi escolhida?
  2. Qual a complexidade?
  3. Existe alternativa melhor?
  4. Qual o trade-off?

### Aplicação no MarketRoute
- Representar mapa como grafo.
- Implementar Dijkstra e, depois, A*.
- Comparar custo e comportamento das duas abordagens.

### Critério para avançar
Você consegue olhar para um problema e discutir estrutura de dados, complexidade e alternativas sem depender de decorar uma solução.

---

## 2. Java em nível de Engenheiro Júnior

### Estudar
#### Linguagem e runtime
- Collections
- Generics
- Streams
- Optional
- Exceptions
- Records
- Imutabilidade
- `equals()` e `hashCode()`
- JVM
- Heap x Stack
- Garbage Collection

#### Concorrência
- Threads
- Executors
- CompletableFuture
- race conditions
- locks
- thread safety
- virtual threads

#### Qualidade de código
- Clean Code sem dogmatismo
- SOLID
- coesão e acoplamento
- composição x heranca

### Prática
- Implementar pequenas rotinas concorrentes.
- Comparar estruturas mutáveis e imutáveis.
- Investigar consumo de memória e threads com ferramentas da JVM.

### Perguntas que voce deve conseguir responder
- Por que `HashMap` tende a lookup O(1)?
- Quando Streams pioram legibilidade ou performance?
- O que acontece quando várias threads alteram o mesmo estado?
- Qual o custo de criar muitos objetos na JVM?

### Critério para avançar
Você domina Java alem de annotations/framework e consegue explicar comportamento de memória, collections e concorrência.

---

## 3. Spring Boot para produção

### Estudar
#### Web/API
- REST
- modelagem de recursos
- HTTP profundamente
- status codes corretos
- headers
- idempotência
- paginação
- versionamento
- OpenAPI/Swagger

#### Spring
- IoC e Dependency Injection
- lifecycle de beans
- Configuration
- Spring Data JPA
- Spring Security
- Bean Validation
- exception handling global
- transactions
- profiles e configuração externa

### Prática
Construa APIs com:

```text
Controller
   -> Application/Service
   -> Domain
   -> Repository
   -> PostgreSQL
```

Inclua desde o inicio:
- validação
- tratamento consistente de erros
- logs estruturados
- documentação da API
- testes

### Critério para avançar
Você consegue construir sozinho uma API real, segura, testada e organizada, sem depender de tutorial passo a passo.

---

## 4. Testes e qualidade de software

Não deixe testes para o final.

### Estudar
- piramide de testes
- JUnit 5
- Mockito
- testes unitários
- testes de integração
- Testcontainers
- WireMock
- fixtures/builders
- coverage como indicador, não como objetivo

### Prática
- Testar regra de negocio sem subir a aplicação inteira.
- Testar repositories com PostgreSQL real via Testcontainers.
- Testar integracoes externas com WireMock.
- Criar testes para bugs antes de corrigi-los quando possível.

### Critério para avançar
Você sabe escolher entre unitario, integração e end-to-end e consegue explicar por que cada teste existe.

---

## 5. PostgreSQL e fundamentos de banco de dados

### Estudar
- modelagem relacional
- PK e FK
- constraints
- joins
- indexes
- composite indexes
- `EXPLAIN` / `EXPLAIN ANALYZE`
- normalização
- transações
- ACID
- isolation levels
- locks
- deadlocks
- optimistic locking
- connection pool
- paginação
- problema N+1

### Prática
- Ver a SQL gerada pelo Hibernate.
- Criar uma consulta lenta, medir, adicionar indice e comparar.
- Simular concorrência e conflitos de atualizacao.
- Identificar N+1 em JPA e corrigir.

### Critério para avançar
Você não trata JPA como caixa preta e sabe diagnosticar queries lentas, índices ruins e problemas transacionais básicos.

---

## 6. Arquitetura de Software

### Ordem de estudo
1. Layered Architecture
2. Modular Monolith
3. Hexagonal / Ports and Adapters
4. Clean Architecture
5. DDD pragmatico
6. Microservices
7. Event-Driven Architecture

### Conceitos
- separação de responsabilidades
- high cohesion / low coupling
- dependency inversion
- boundaries
- Repository Pattern
- Strategy
- Factory
- Adapter
- Entity
- Value Object
- Aggregate
- Bounded Context

### Prática
- Estruturar o MarketRoute inicialmente como **monolito modular**.
- Criar ADRs (Architecture Decision Records) para decisões relevantes.
- Justificar por que não usar microsservicos cedo demais.

### Critério para avançar
Você consegue dizer: "considerei A e B, escolhi A por X, e aceitei Y como desvantagem".

---

## 7. Redis e caching

### Estudar
- key-value store
- cache-aside
- TTL
- cache invalidation
- eviction
- cache stampede em alto nível
- rate limiting
- locks distribuidos: conceito e riscos

### Prática
- Cachear uma consulta cara do MarketRoute.
- Medir latência antes/depois.
- Definir estrategia de invalidação.
- Implementar rate limiting simples.

### Critério para avançar
Você sabe explicar quando Redis ajuda, quando não ajuda e qual problema de consistência o cache introduz.

---

## 8. Kafka e mensageria

### Estudar
- producer
- consumer
- topic
- partition
- consumer group
- offset
- ordering
- retention
- retries
- DLQ
- at-least-once delivery
- idempotência
- eventual consistency
- Schema Registry em alto nível

### Prática
Criar um projeto de pagamentos ou pedidos:

```text
Order/Payment API
      -> PostgreSQL
      -> Outbox
      -> Kafka
      -> Consumer
      -> Notification/Fraud
```

### Depois
- Transactional Outbox
- Saga: conceito
- CQRS: conceito
- Event Sourcing: conceito

### Critério para avançar
Você consegue explicar por que mensageria existe, como duplicidade acontece e como tornar um consumidor idempotente.

---

## 9. Sistemas Distribuídos

### Estudar
#### Falhas e resiliência
- timeout
- retry
- exponential backoff
- circuit breaker
- cascading failure
- bulkhead em alto nível

#### Consistência
- consistência forte x eventual
- idempotência
- deduplicação
- distributed transactions: problema
- CAP theorem sem decorar slogan

#### Escala
- horizontal x vertical scaling
- stateless services
- load balancing
- sharding: conceito
- replicas: conceito

### Prática
- Simular dependencia fora do ar.
- Implementar timeout e retry controlado.
- Testar processamento duplicado.
- Documentar como o sistema reage a falhas.

### Critério para avançar
Você raciocina sobre falhas como parte normal do sistema, não como excecao improvável.

---

## 10. Docker e ambientes reproduzíveis

### Estudar
- images
- containers
- Dockerfile
- layers
- multi-stage build
- volumes
- networks
- environment variables
- health checks
- Docker Compose

### Prática
Seu projeto deve subir com algo proximo de:

```bash
docker compose up
```

Incluindo aplicação, PostgreSQL, Redis e Kafka quando necessário.

### Critério para avançar
Qualquer pessoa consegue clonar o repositorio e executar o sistema seguindo poucas instrucoes.

---

## 11. AWS para Software Engineer

Não tente aprender toda a AWS.

### Prioridade alta
- IAM
- EC2
- S3
- RDS
- DynamoDB
- ElastiCache
- SQS
- SNS
- Lambda
- ECS
- CloudWatch

### Depois
- VPC
- Load Balancer
- Auto Scaling
- EKS: conceito

### Prática
- Fazer deploy de ao menos um projeto real.
- Configurar banco gerenciado.
- Externalizar secrets/configuracoes.
- Consultar logs e métricas do ambiente.

### Critério para avançar
Você consegue colocar um backend em produção e explicar os principais componentes usados.

---

## 12. CI/CD e engenharia de entrega

### Estudar
- Continuous Integration
- Continuous Delivery/Deployment
- GitHub Actions
- build automatizado
- testes no pipeline
- análise estática
- build de imagem Docker
- secrets de CI
- rollback
- trunk-based development
- feature branches
- canary e blue/green em alto nível

### Pipeline alvo

```text
push / pull request
      -> build
      -> unit tests
      -> integration tests
      -> static analysis
      -> Docker image
      -> deploy
```

### Critério para avançar
Uma alteracao não depende de voce executar manualmente cada etapa para validar e entregar o sistema.

---

## 13. Observabilidade e diagnóstico de produção

### Estudar
#### Os tres pilares
- Logs
- Metrics
- Traces

#### Ferramentas
- structured logging
- correlation/trace ID
- OpenTelemetry
- Prometheus
- Grafana

#### Metricas
- throughput
- latency
- error rate
- CPU
- memória
- p50, p95, p99

### Prática
- Criar dashboard do projeto.
- Instrumentar uma requisição ponta a ponta.
- Executar teste de carga.
- Encontrar e corrigir ao menos um gargalo real.

### Pergunta-chave
> "Minha API ficou lenta. Como eu descobriria a causa?"

### Critério para avançar
Você sabe usar evidências de produção para diagnosticar problemas, não apenas ler stack trace.

---

## 14. Kubernetes basico

Aprenda o suficiente para trabalhar como desenvolvedor, não como administrador de cluster.

### Estudar
- Pod
- Deployment
- Service
- ConfigMap
- Secret
- Ingress
- replicas
- readiness/liveness probe
- horizontal scaling

### Prática
- Subir sua aplicação em cluster local (kind/minikube) uma vez.
- Entender manifests sem tentar decorar YAML.

### Critério para avançar
Você entende como uma aplicação containerizada e executada, exposta e escalada dentro do Kubernetes.

---

## 15. Segurança para Backend

### Estudar
- Authentication x Authorization
- Spring Security
- JWT
- OAuth2/OIDC
- password hashing
- HTTPS
- CORS
- CSRF
- SQL Injection
- XSS: conceito
- secrets management
- rate limiting
- OWASP Top 10

### Prática
- Implementar autenticação/autorização corretamente.
- Remover secrets do repositorio.
- Testar acesso por papeis/permissoes.

### Critério para avançar
Você conhece os erros de seguranca mais comuns de APIs e evita solucoes caseiras para autenticação e criptografia.

---

## 16. System Design para Júnior

### Estudar
- levantamento de requisitos
- estimativas simples
- API design
- modelagem de dados
- cache
- filas
- banco relacional x NoSQL
- load balancer
- escalabilidade
- disponibilidade
- consistência
- observabilidade
- principais pontos de falha

### Problemas para práticar
- URL Shortener
- Notification System
- Payment System
- Ticketing System
- File Upload Service
- Product Catalog

### Critério para avançar
Você consegue desenhar uma solução simples, explicar os componentes e discutir gargalos/trade-offs sem transformar tudo em microsservicos.

---

## 17. Desenvolvimento assistido por IA

Use como multiplicador, não como substituto dos fundamentos.

### Estudar
- AI-assisted coding
- contexto para agentes/LLMs
- MCP: conceito e uso
- prompts/instrucoes de engenharia
- revisão de código gerado
- testes para saídas geradas
- risco de vazamento de secrets e dados

### Prática
- Usar IA para acelerar boilerplate, testes e investigacao.
- Revisar cada mudanca crítica.
- Ser capaz de implementar e explicar o código sem depender da IA.

### Critério para avançar
A IA aumenta sua velocidade, mas voce continua responsável pela arquitetura, corretude e seguranca.

---

# Projetos do portfólio

## Projeto principal - MarketRoute

### Objetivo
Demonstrar algoritmos, backend, banco de dados, arquitetura, performance e produto em um problema menos comum que CRUD.

### Stack alvo
- Java 21
- Spring Boot
- PostgreSQL
- Redis
- React + TypeScript
- Docker
- GitHub Actions
- AWS
- OpenTelemetry
- Prometheus/Grafana

### Evidencias técnicas desejadas
- grafo do supermercado
- Dijkstra/A*
- testes de persistencia e integração
- cache medido
- CI/CD
- deploy real
- observabilidade
- ADRs
- benchmark antes/depois de otimizações

---

## Projeto 2 - Payments Platform

### Demonstrar
- Kafka
- Transactional Outbox
- idempotency keys
- retry
- DLQ
- consistência eventual
- PostgreSQL
- Redis
- tracing distribuido
- Testcontainers

---

## Projeto 3 - High Scale Notification Platform

### Demonstrar
- processamento assíncrono
- workers
- Kafka/SQS
- Redis rate limiting
- retry com backoff
- DLQ
- métricas
- p95/p99
- testes de carga
- escalabilidade horizontal

> Se o tempo for limitado, prefira **2 projetos excelentes** a 5 projetos medianos.

---

# Trilha paralela para entrevistas

## Algoritmos
- 3 problemas por semana.
- Prioridade: Array, HashMap, Stack/Queue, Trees, Graphs, BFS/DFS, Binary Search e Heap.

## Behavioral
Prepare histórias reais no formato STAR sobre:
- conflito ou discordancia técnica
- bug difícil
- melhoria de processo
- entrega com prazo
- aprendizado rápido
- erro cometido
- decisão com trade-off
- colaboracao com area de negocio

## Ingles
- documentação sempre que possível em inglês
- explicar um projeto em inglês por 5-10 minutos
- práticar perguntas técnicas comuns

---

# Ordem resumida para seguir sem pensar

```text
0. Git + Linux + HTTP
1. Estruturas de Dados + Big O
2. Java avançado
3. Spring Boot profissional
4. Testes
5. PostgreSQL
6. Arquitetura
7. Docker + CI/CD
8. Segurança
9. Redis
10. Kafka
11. Sistemas Distribuídos
12. Observabilidade
13. AWS
14. Kubernetes basico
15. System Design
16. AI-assisted Engineering
```

Em paralelo durante toda a trilha:

```text
Projetos reais + GitHub + algoritmos + inglês + comunicação técnica
```

---

# O que NAO priorizar agora

- Clojure antes de ter fundamentos fortes
- Rust sem necessidade concreta
- Go profundo antes de consolidar Java
- Kubernetes avançado
- Terraform avançado
- certificações AWS como objetivo principal
- dezenas de Design Patterns decorados
- frontend avançado se o foco e backend
- varios bancos NoSQL superficialmente
- microservices antes de dominar um monolito bem estruturado

---

# Regra final de dominio

Para qualquer tecnologia escrita no seu currículo, voce deve conseguir responder:

1. **Por que usei?**
2. **Como funciona?**
3. **Qual alternativa eu considerei?**
4. **Qual trade-off aceitei?**
5. **Como provei que funcionou?**

Se não consegue responder essas cinco perguntas, a tecnologia ainda não esta pronta para virar destaque no currículo.
