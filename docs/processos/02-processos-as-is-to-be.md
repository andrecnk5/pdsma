# P02 — Mapeamento AS-IS e TO-BE

> **Estado:** referência v1.0 aprovada em 29/10/2026 e adaptável por projeto. A ordem numérica é didática, não uma cascata.

## Objetivo e responsabilidades

Mapear o trabalho real (AS-IS) e formular um fluxo futuro (TO-BE), incluindo exceções, atores e transferências de responsabilidade.

**Responsável primário:** Análise de negócio e Produto. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Definir evento inicial e final, unidades envolvidas, entradas, saídas e documentos ou sistemas utilizados.
2. Observar o AS-IS com atores, decisões, campos, prazos, pontos de retrabalho e diferenças entre norma e prática.
3. Identificar falhas, espera, dados duplicados, responsabilidade pouco clara e controles que existem por razões legais ou operacionais.
4. Propor TO-BE simplificado, indicando fonte de verdade, quem registra, quem consulta, quem corrige e como auditoria ocorre.
5. Mapear situações não ideais: conexão indisponível, registro duplicado, correção tardia, ausência de permissão e integração fora do ar.
6. Validar o fluxo com operadores, responsáveis e consumidores das informações; atualizar regras e riscos decorrentes.

## Artefatos e evidências de saída

- Diagrama ou roteiro AS-IS e TO-BE versionado.
- Matriz de atores, responsabilidades, eventos, regras e exceções.
- Lista de ganhos esperados e mudanças organizacionais.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Os executores confirmaram a representação ou suas divergências foram registradas.
- Exceções críticas e transferências de responsabilidade estão contempladas.
- Mudanças de processo que exigem autorização possuem decisor.

## Falhas e cuidados

Não digitalizar cegamente cada formulário nem eliminar controle sem avaliar sua finalidade.

**Trabalho paralelo permitido:** Pesquisa de usuários, regras e riscos.

**Exemplo orientativo:** Definir que professor registra e assistência acompanha, enquanto correções depois do fechamento possuem fluxo auditável.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
