# P06 — Backlog, planejamento e método de trabalho

> **Estado:** referência v1.0 aprovada em 29/10/2026 e adaptável por projeto. A ordem numérica é didática, não uma cascata.

## Objetivo e responsabilidades

Organizar entregas em sequência de valor, respeitando riscos, capacidade real e feedback.

**Responsável primário:** Produto e facilitação da equipe. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Decompor capacidades em itens pequenos vinculados a requisitos e critérios de aceite, incluindo atividades de QA e operação.
2. Priorizar por valor, urgência, dependências, risco e potencial de aprendizagem; explicitar conflitos de prioridade.
3. Planejar fatias verticais completas em vez de pacotes isolados de telas, banco ou endpoints.
4. Estimar capacidade e incerteza com base na equipe e histórico disponível; não impor prazo genérico por complexidade abstrata.
5. Selecionar Scrum, Kanban ou combinação conforme necessidade; definir cadência, limites de WIP, revisões e como replanejar.
6. Combinar Definition of Done e preparação opcional de itens, sem criar 'Sprint 0' como suposto evento obrigatório do Scrum.
7. Comunicar ordem de execução e bloqueios; revisar backlog quando pesquisa, protótipo ou testes revelarem fatos novos.

## Artefatos e evidências de saída

- Backlog priorizado com dependências e responsáveis.
- Plano do primeiro incremento e rotina de inspeção.
- Definições de qualidade e critérios de início quando adotados.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Itens prioritários podem ser demonstrados e verificados.
- Dependências de alto risco são visíveis.
- Existe mecanismo explícito de mudança de prioridade.

## Falhas e cuidados

Evitar estimativa teatral, excesso de reuniões e trabalho em progresso ilimitado.

**Trabalho paralelo permitido:** Design, arquitetura inicial e preparação técnica.

**Exemplo orientativo:** Primeira fatia lista turmas autorizadas; segunda grava frequência; terceira corrige com auditoria.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
