# Método de aprendizagem

Este arquivo contém as regras pedagógicas e o modelo de estado compartilhados pelas Skills. Procedimentos e persistência específicos pertencem a cada Skill.

## Modelo de aprendizagem

Aprender é construir um modelo interno estável, conectado e utilizável. Recuperar conhecimento, formular uma hipótese, testar, aplicar e corrigir o raciocínio fortalece esse modelo mais do que releitura passiva.

A atenção é limitada. Cada sessão deve ter um tópico e um objetivo claros. Pausas e sono adequado fazem parte da consolidação; repetição intensiva e ferramentas não os substituem.

## Ciclo ativo

1. recuperar o que já se sabe sem consulta;
2. formular uma explicação, previsão ou solução;
3. comparar a tentativa com o conhecimento correto;
4. localizar acertos, gaps e a causa dos erros;
5. corrigir o modelo, não apenas a resposta;
6. verificar a correção com no máximo uma variação focada;
7. explicar ou aplicar sem consulta.

O feedback vem depois da tentativa quando já existe base para tentar. Quando não existe, ensine apenas o suporte necessário e verifique a recuperação logo depois. Analogias, diagramas, exemplos, código, testes e falhas são recursos opcionais, usados somente quando ajudam o objetivo atual.

Ensino progressivo divide o assunto em partes conectadas; não reduz cada parte a uma definição. Dê profundidade suficiente para o objetivo da sessão: construa como e por que o conceito funciona, onde é útil e como aplicá-lo ou reconhecê-lo em problemas. Use um exemplo acompanhado passo a passo, erros frequentes ou uma comparação quando isso esclarecer o mecanismo ou a escolha. Ajuste a profundidade à base demonstrada, sem exigir que o aluno descubra sozinho o que ainda não foi ensinado.

Considere coberto o conceito demonstrado. Retome-o apenas por contradição, dependência ou verificação integradora. Corrija a causa do erro e não prolongue a sessão para buscar exaustividade.

## Estudar, praticar, revisar e avaliar

- **Estudar:** constrói ou amplia o modelo com diagnóstico curto, ensino progressivo, recuperação e aplicação.
- **Praticar:** amplia aplicação e raciocínio; feedback pode ocorrer por item ou lote depois da tentativa.
- **Revisar:** recupera conteúdo estudado, prioriza gaps e introduz somente a correção necessária.
- **Avaliar:** mede desempenho autônomo; não oferece pistas, correções ou ensino durante a tentativa.

Os modos podem usar perguntas semelhantes, mas produzem evidências diferentes. Acerto assistido, releitura e conteúdo apresentado não demonstram domínio autônomo.

## Estado de aprendizagem

`Status` representa a fase do tópico:

- **Não iniciado:** existe registro, mas nenhuma sessão foi concluída;
- **Estudando:** o modelo ainda depende de ensino ou pistas;
- **Praticando:** os conceitos principais podem ser explicados, mas aplicação, diagnóstico ou decisões ainda exigem feedback;
- **Consolidado:** há evidência autônoma em datas diferentes de explicação, aplicação e análise relevante.

`Nível` representa a melhor evidência atual observada:

- **0:** não compreendeu;
- **1:** reconhece;
- **2:** entende com ajuda;
- **3:** explica corretamente;
- **4:** aplica corretamente;
- **5:** analisa trade-offs, diagnostica problemas e lida com casos não óbvios.

Mantenha `Status` e `Nível` independentes. Não aumente o nível por conteúdo apresentado nem marque `Consolidado` por uma única sessão. Evidência posterior incompatível exige registrar o gap e reclassificar o estado.

## Revisão espaçada

A sequência padrão é `D+1 → D+3 → D+7 → D+14 → D+30`.

Uma recuperação correta, explicada e autônoma avança um intervalo. Em `D+30`, novo sucesso mantém o intervalo máximo. Gap relevante reinicia em `D+1`; evidência insuficiente sem gap relevante repete o estágio. Imprecisão secundária é corrigida sem reiniciar a sequência.

O intervalo mede retenção; não substitui prática, aplicação nem descanso. As Skills de revisão e avaliação definem como tratar revisão antecipada e evidência longitudinal.
