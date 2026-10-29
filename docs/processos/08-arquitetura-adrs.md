# P08 — Arquitetura evolutiva e ADRs

> **Estado:** referência v1.0 aprovada em 29/10/2026 e adaptável por projeto. A ordem numérica é didática, não uma cascata.

## Objetivo e responsabilidades

Tomar decisões técnicas justificadas e proporcionais ao risco, sem projetar todos os módulos futuros.

**Responsável primário:** Engenharia/Arquitetura. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Reunir cenários de qualidade e suas consequências: segurança, rastreabilidade, desempenho, manutenção e disponibilidade.
2. Escolher organização técnica proporcional à equipe; monolito modular pode ser adequado, mas não é obrigação.
3. Descrever contexto, fronteiras, componentes e integrações; usar C4 quando facilitar comunicação.
4. Registrar decisões importantes em ADR: contexto, alternativas, decisão, consequências e circunstâncias de revisão.
5. Confrontar arquitetura com fluxos e exceções de UX e requisitos; ajustar contratos antes de cristalizá-los.
6. Identificar autenticação, autorização, transações, migrações, falhas, logs e riscos de concorrência.
7. Investigar pontos desconhecidos com spike curto e descartável; separar hipótese arquitetural de decisão validada.

## Artefatos e evidências de saída

- Diagramas suficientes e cenários de qualidade.
- ADRs com decisões relevantes.
- Plano de riscos e contratos a detalhar.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Decisões de alto impacto possuem justificativa recuperável.
- Atributos críticos estão protegidos por estratégia técnica e verificação.
- Nenhuma dependência funcional importante ficou invisível.

## Falhas e cuidados

Evitar arquitetura teatral e microserviços sem justificativa operacional.

**Trabalho paralelo permitido:** UX, esquema de dados, APIs e CI.

**Exemplo orientativo:** Preservar autoria e histórico de correção de frequência como invariantes do domínio.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
