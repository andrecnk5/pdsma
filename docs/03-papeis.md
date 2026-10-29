# Papéis, decisões e responsabilidades

| Papel | Responsabilidade principal | Interface com |
| --- | --- | --- |
| Produto | Problema, valor, escopo, prioridade, aceite funcional | Usuários, UX, engenharia |
| Análise de negócio | AS-IS/TO-BE, regras, requisitos, rastreabilidade | Produto, operações |
| UX | Jornadas, protótipos, pesquisa e interação acessível | Usuários, produto, engenharia |
| Engenharia | Arquitetura, contratos, código, integridade e revisão | UX, dados, QA |
| Dados | Modelo, histórico, migração, retenção e consistência | Engenharia, privacidade |
| QA | Estratégia, evidências de testes, regressões e riscos | Todos os responsáveis |
| Segurança e privacidade | Ameaças, controles, tratamento de dados, riscos | Engenharia, produto, jurídico |
| DevOps/Operações | Ambientes, CI/CD, deploy, logs, recuperação e suporte | Engenharia, segurança |
| Usuários representantes | Evidência de uso e avaliação de tarefas reais | UX, produto |
| Autoridade de release | Decisão de exposição no ambiente e risco operacional | Produto, QA, operações |

Uma pessoa pode assumir vários papéis, mas não deve poder encobrir um conflito de interesses em decisão crítica. Mantenha revisão independente de segurança e dados quando risco exigir.

## Autoridade e conflito

- Produto prioriza valor, mas não elimina obrigações legais ou proteção essencial.
- UX apresenta evidências e recomenda fluxos; aprovação funcional é documentada por Produto.
- Engenharia determina soluções técnicas justificadas e revisa impacto das decisões de UX.
- QA pode reportar risco sem ter autoridade para aceitar exposição desse risco.
- Homologação pode ser aceita sem autorizar produção; publicação precisa de autoridade específica.
- Discordâncias relevantes entram em [registro de decisão](modelos/decisao.md), com alternativas, pareceres e consequências.

[Controles](02-fluxo-e-controles.md) · [Índice](../README.md)
