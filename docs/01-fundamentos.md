# Fundamentos do processo

## Princípios

1. **Entender antes de implementar:** definir necessidade e resultado antes de escolher solução.
2. **Validação proporcional:** testar hipóteses com usuários e evidências relevantes, sem presumir certeza universal.
3. **Entrega vertical:** criar funcionalidade que atravesse interação, regra de negócio, API e persistência quando aplicável.
4. **Arquitetura evolutiva:** antecipar decisões de alto risco e adiar detalhes reversíveis.
5. **Qualidade incorporada:** testes, segurança, privacidade, acessibilidade e integridade desde a definição dos requisitos.
6. **Decisões rastreáveis:** manter quem decidiu, por quê, com quais evidências e quando revisar.
7. **Publicação responsável:** não confundir código pronto, aceite funcional e autorização de produção.
8. **Feedback:** corrigir planejamento diante da realidade, sem ocultar impactos.

## Conceitos diferentes

**Produto:** solução ampla. **MVP:** menor experimento funcional suficiente para testar hipótese de valor. **Módulo:** conjunto de capacidades relacionadas. **Incremento:** software integrado e utilizável que atende aos critérios de qualidade acordados. Um módulo pode ser entregue sem constituir MVP completo.

**Prova de conceito:** verifica viabilidade de hipótese técnica e pode ser descartada. **Walking skeleton:** integração executável mínima de camadas necessárias que demonstra o caminho técnico, não todo o valor funcional.

**Homologação/UAT:** valida aceitação do negócio com usuários. **QA:** produz evidências de qualidade e identifica defeitos. **Release:** disponibilização em destino autorizado com controles operacionais.

## Compatibilidade ágil

Scrum possui eventos, papéis e compromissos próprios; 'Sprint 0' não é evento prescrito. Kanban pode privilegiar fluxo e limite de WIP. O PDSMA descreve dependências profissionais independentes de cerimônias específicas. Sprints de duas semanas, TDD, Docker, GitFlow, C4 e monolito modular são opções a justificar.

[Fluxo e controles](02-fluxo-e-controles.md) · [Índice](../README.md)
