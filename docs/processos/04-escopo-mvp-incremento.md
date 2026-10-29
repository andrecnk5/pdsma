# P04 — Escopo, MVP e primeiro incremento

> **Estado:** referência v1.0 aprovada em 29/10/2026 e adaptável por projeto. A ordem numérica é didática, não uma cascata.

## Objetivo e responsabilidades

Distinguir produto completo, MVP para testar hipótese e módulo ou incremento funcional que entregue uma capacidade real.

**Responsável primário:** Produto. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Construir mapa de capacidades e jornadas do produto sem exigir detalhamento de todos os módulos futuros.
2. Definir hipótese do MVP, usuário que obtém valor e evidência real capaz de confirmar ou refutar a hipótese.
3. Escolher primeiro incremento pela relação valor, risco, dependências e capacidade da equipe; preferir fatia de interface, regra e persistência.
4. Listar explicitamente inclusões, exclusões, funcionalidades transversais mínimas e limitações aceitas.
5. Identificar requisitos de autenticação, autorização, identidade, histórico e observabilidade imprescindíveis ao fluxo.
6. Descrever demonstração ponta a ponta e como se saberá que o recorte está funcional; rever caso dependa de recursos ainda inexistentes.

## Artefatos e evidências de saída

- Declaração de escopo e fora de escopo.
- Hipótese de MVP e métrica de aprendizagem.
- Mapa do primeiro incremento com dependências.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- O módulo gera comportamento demonstrável, e não só componentes técnicos.
- Riscos essenciais não foram removidos apenas para reduzir esforço.
- Produto e equipe concordam sobre limites do recorte.

## Falhas e cuidados

MVP não significa versão insegura; primeiro módulo não é automaticamente MVP.

**Trabalho paralelo permitido:** Refinamento inicial de regras e UX.

**Exemplo orientativo:** Registrar e consultar a frequência de uma turma antes de implantar relatórios gerais.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
