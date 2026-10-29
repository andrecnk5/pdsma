# P16 — Feedback e evolução

> **Estado:** referência v1.0 aprovada em 29/10/2026 e adaptável por projeto. A ordem numérica é didática, não uma cascata.

## Objetivo e responsabilidades

Analisar resultados reais, aprender com problemas e decidir o próximo incremento por evidências.

**Responsável primário:** Produto. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Medir resultado previsto na descoberta, comparando à situação anterior e explicitando limitações.
2. Coletar feedback de usuários, suporte e observações de tarefas com cuidado à privacidade e representatividade.
3. Separar falha de UX, defeito técnico, demanda nova, adaptação de processo e hipótese de valor refutada.
4. Revisar riscos, arquitetura, testes, débito técnico e operação à luz das evidências.
5. Realizar retrospectiva da colaboração e escolher melhorias de processo pequenas, com responsáveis e indicadores.
6. Repriorizar backlog e decidir desenvolver, ajustar, pesquisar ou interromper, registrando justificativa.
7. Manter ligação entre a versão publicada, o resultado observado e a decisão sobre o próximo incremento.

## Artefatos e evidências de saída

- Relato de aprendizagem e indicadores.
- Backlog revisado e decisões.
- Plano de melhoria e acompanhamento.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Resultados e limitações das evidências estão diferenciados.
- O próximo incremento tem prioridade justificável.
- Incidentes e problemas recorrentes têm donos.

## Falhas e cuidados

Não confundir mais funcionalidades com mais valor; não ranquear pessoas por métricas de fluxo.

**Trabalho paralelo permitido:** Operação e descoberta subsequente.

**Exemplo orientativo:** Comparar retrabalho e tempo de lançamento após o piloto, corrigindo o fluxo se o benefício não aparecer.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
