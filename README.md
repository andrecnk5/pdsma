# PDSMA — Processos de Desenvolvimento de Software e Metodologias Ágeis

> **Proposta documental v0.1 · 29/10/2026 · Em revisão.** Nenhuma aprovação metodológica definitiva é presumida.

Guia operacional em português para aplicações web de complexidade intermediária, desde a concepção da ideia até o **primeiro incremento funcional e validado**. Integra descoberta de produto, engenharia de requisitos, UX/UI, arquitetura evolutiva, desenvolvimento por fatias verticais, qualidade, segurança, DevOps e evolução baseada em evidências.

## Navegação recomendada

1. [Como usar](docs/00-como-usar.md) e [fundamentos](docs/01-fundamentos.md).
2. [Fluxo, dependências e controles A–D](docs/02-fluxo-e-controles.md).
3. [Papéis e responsabilidades](docs/03-papeis.md).
4. [Governança e mudanças](docs/04-governanca.md).
5. [Matriz de rastreabilidade](docs/05-rastreabilidade.md) e [DoR / DoD](docs/06-ready-done.md).
6. [Exemplo aplicado: frequência escolar](docs/exemplo/modulo-frequencia.md).
7. [Referências oficiais](docs/referencias.md).

## Processos do ciclo

| Ordem | Processo | Resultado |
| --- | --- | --- |
| 01 | [Concepção e descoberta](docs/processos/01-concepcao-descoberta.md) | Visão do produto com problema, público, hipótese e métrica de resultado. |
| 02 | [Mapeamento AS-IS e TO-BE](docs/processos/02-processos-as-is-to-be.md) | Diagrama ou roteiro AS-IS e TO-BE versionado. |
| 03 | [Viabilidade, restrições e riscos](docs/processos/03-viabilidade-riscos.md) | Registro de riscos priorizado, dependências e restrições. |
| 04 | [Escopo, MVP e primeiro incremento](docs/processos/04-escopo-mvp-incremento.md) | Declaração de escopo e fora de escopo. |
| 05 | [Requisitos, regras e critérios de aceite](docs/processos/05-requisitos-regras.md) | Catálogo de requisitos e regras com IDs e origem. |
| 06 | [Backlog, planejamento e método de trabalho](docs/processos/06-backlog-planejamento.md) | Backlog priorizado com dependências e responsáveis. |
| 07 | [UX, jornadas e prototipação validada](docs/processos/07-ux-prototipacao.md) | Jornadas, fluxos e wireframes versionados. |
| 08 | [Arquitetura evolutiva e ADRs](docs/processos/08-arquitetura-adrs.md) | Diagramas suficientes e cenários de qualidade. |
| 09 | [Dados, APIs e integrações](docs/processos/09-dados-apis.md) | Modelo conceitual e lógico, dicionário e invariantes. |
| 10 | [Repositório, ambientes, CI e integração mínima](docs/processos/10-repositorio-ci.md) | Estrutura, políticas e PR template do repositório. |
| 11 | [Implementação iterativa e revisão](docs/processos/11-implementacao-iterativa.md) | PRs pequenos, ligados a issue/requisito. |
| 12 | [Qualidade e testes contínuos](docs/processos/12-qualidade-testes.md) | Plano e matriz de testes vinculados aos requisitos. |
| 13 | [Segurança, privacidade e acessibilidade](docs/processos/13-seguranca-privacidade-acessibilidade.md) | Matriz de dados e autorização, ameaças e controles. |
| 14 | [Homologação, UAT e aceite](docs/processos/14-homologacao-aceite.md) | Plano e relatório UAT vinculados a requisitos. |
| 15 | [Publicação, operação e recuperação](docs/processos/15-publicacao-operacao.md) | Registro de release e autorização de destino. |
| 16 | [Feedback e evolução](docs/processos/16-feedback-evolucao.md) | Relato de aprendizagem e indicadores. |

**Atenção:** esta lista apresenta uma ordem lógica de dependências, **não** um modelo em cascata. UX e arquitetura se influenciam; requisitos, segurança, testes e riscos evoluem ao longo de toda a construção. O primeiro módulo funcional não equivale necessariamente ao MVP.

## Modelos para aplicar em projetos reais

[Visão do produto](docs/modelos/visao.md) · [Requisito](docs/modelos/requisito.md) · [História de usuário](docs/modelos/historia.md) · [Validação de UX](docs/modelos/ux.md) · [ADR](docs/modelos/adr.md) · [Decisão](docs/modelos/decisao.md) · [Plano de testes](docs/modelos/testes.md) · [Release](docs/modelos/release.md).

## Governança documental do GitHub

- Documentação como código em Markdown, com links relativos, IDs e registro de mudanças.
- Contribuições por branch/PR, revisão e evidências ligadas a issues e decisões.
- Verificação automatizada de estrutura e links locais por [script Python](scripts/validar_documentacao.py) e [GitHub Actions](.github/workflows/docs.yml); não confundir CI com revisão técnica humana.
- [CONTRIBUTING](CONTRIBUTING.md) · [CHANGELOG](CHANGELOG.md) · templates de PR/issues e CODEOWNERS.
- **Licença de redistribuição ainda não escolhida**; não presumir autorização pública pelo fato de existir repositório.

As recomendações do PDSMA são políticas **propostas**, adaptáveis ao porte e ao risco; não equivalem a certificação Scrum, WCAG, OWASP, ISO ou LGPD.
