# P05 — Requisitos, regras e critérios de aceite

> **Estado:** referência v1.0 aprovada em 29/10/2026 e adaptável por projeto. A ordem numérica é didática, não uma cascata.

## Objetivo e responsabilidades

Traduzir necessidades em comportamento verificável, incluindo exceções, autorização e requisitos de qualidade.

**Responsável primário:** Análise de negócio e Produto. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Identificar e numerar RF, RN e RNF, preservando IDs estáveis, fonte, prioridade, versão e estado.
2. Detalhar cada cenário: ator, pré-condição, evento, resultado, persistência, alternativas e comportamento diante de falhas.
3. Definir regras de negócio invariantes, estados e transições, com atenção a quem pode criar, corrigir ou excluir vínculos.
4. Descrever autorização por recurso e ator; validar no servidor e definir trilha de auditoria onde necessária.
5. Especificar qualidade de maneira mensurável: acessibilidade-alvo, desempenho sob carga definida, recuperação, disponibilidade e privacidade conforme contexto.
6. Redigir critérios de aceite com exemplos de sucesso, proibição, limite e erro (Dado/Quando/Então quando útil).
7. Revisar inconsistências com UX, dados, engenharia e QA, registrando escolhas e questões pendentes.

## Artefatos e evidências de saída

- Catálogo de requisitos e regras com IDs e origem.
- Cenários de aceite, incluindo negativos.
- Matriz de atores/permissões e requisitos não funcionais verificáveis.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Cada requisito crítico tem método de verificação previsto.
- Estados e exceções foram discutidos com responsável competente.
- Não há termos vagos como 'rápido' sem contexto e critério.

## Falhas e cuidados

História de usuário não substitui análise de domínio; regra crítica não pode morar apenas na interface.

**Trabalho paralelo permitido:** UX exploratória, modelagem de domínio e backlog.

**Exemplo orientativo:** Corrigir frequência fechada exige motivo, autorização e preservação do valor anterior.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
