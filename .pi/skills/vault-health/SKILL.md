---
name: vault-health
description: Audita em modo somente leitura a integridade estrutural e o estado derivado do Active Study System. Não corrige arquivos sem pedido explícito separado.
---

# Vault Health

Execute uma auditoria determinística antes de interpretar problemas do Vault.

## Procedimento

1. Execute na raiz:

   ```powershell
   py -3 .pi\skills\vault-health\scripts\check_vault.py --root .
   ```

2. Classifique os achados por impacto:
   - erro: estado inválido, par obrigatório ausente, proteção de notas quebrada ou visão derivada divergente;
   - aviso: link canônico quebrado ou lista sem estado claro.
3. Explique a causa provável e a correção mínima, agrupando problemas repetidos.
4. Se não houver achados, informe que os invariantes cobertos foram verificados; não declare que todo o conteúdo pedagógico está correto.

## Limites

A auditoria é somente leitura. Não execute sincronização nem repare arquivos durante esta Skill, salvo se o usuário pedir explicitamente a correção depois de ver o relatório.

O script verifica pares de tópicos, datas, `Status`, `Nível`, marcadores `USER-NOTES`, links canônicos, listas sem resumo e divergência de `00_HOME.md`/`REVIEWS.md`. Ele não julga a qualidade conceitual das notas nem o domínio real do usuário.
