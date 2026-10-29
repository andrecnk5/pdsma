# P07 — UX, jornadas e prototipação validada

> **Estado:** referência v1.0 aprovada em 29/10/2026 e adaptável por projeto. A ordem numérica é didática, não uma cascata.

## Objetivo e responsabilidades

Reduzir risco de construir a interação errada antes de comprometer implementação de telas definitivas.

**Responsável primário:** UX e Produto. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Identificar tarefas reais, contexto, entradas, saídas e usuários representativos; criar mapa de jornada do recorte.
2. Desenhar fluxos do cenário principal e também erros, ausência de dados, falta de permissão, espera e conexão interrompida.
3. Construir wireframes de baixa fidelidade para validar informação, ordem, vocabulário e comportamento antes da estética.
4. Evoluir para protótipo navegável apenas onde a interação requer exploração; documentar estados responsivos e acessibilidade.
5. Planejar observação de usuários por tarefas, amostra, contexto, critério de êxito e registro de limitações; não declarar representatividade estatística por regra de 3–5 participantes.
6. Analisar achados, corrigir impedimentos, registrar divergências e submeter fluxos relevantes à apreciação do responsável.
7. Negociar com engenharia impactos em domínio/API; UX não deve ficar rigidamente depois de arquitetura nem exigir ausência total de código exploratório.

## Artefatos e evidências de saída

- Jornadas, fluxos e wireframes versionados.
- Protótipos suficientes para o incremento e seus estados.
- Relatório de avaliação, ajustes e decisão do responsável.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Fluxos principais e erros importantes estão representados.
- Tarefas relevantes foram avaliadas com usuários ou revisão justificada.
- Pendências materiais não são tratadas como aprovação tácita.

## Falhas e cuidados

Protótipo aprovado não prova sistema acessível, seguro ou tecnicamente íntegro.

**Trabalho paralelo permitido:** Spikes de arquitetura, CI, risco e modelagem exploratória.

**Exemplo orientativo:** Testar seleção de turma, salvar presença, corrigir erro e recuperação após falha de conexão.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
