# P11 — Implementação iterativa e revisão

> **Estado:** proposta v0.1, sujeita a revisão e adaptação. A posição numérica é didática: não representa fases isoladas.

## Objetivo e responsabilidades

Entregar pequenas capacidades completas, integradas e verificáveis, mantendo feedback de produto e qualidade.

**Responsável primário:** Engenharia. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Escolher item cujo fluxo, contrato e critérios de aceite estejam suficientemente compreendidos.
2. Limitar trabalho em progresso, vincular issue e requisito, quebrar em mudanças pequenas e descrever demonstração esperada.
3. Implementar regras, validações, persistência, controle de acesso no servidor e interface seguindo protótipos relevantes.
4. Incluir testes de sucesso, falha e autorização; tratar erros, concorrência e retrocompatibilidade necessários.
5. Executar CI, revisão de código e análise de risco; registrar mudanças de decisão ou regra descobertas no desenvolvimento.
6. Integrar em ambiente compartilhado e demonstrar a tarefa real; não declarar fatia pronta porque só o backend funciona.
7. Solicitar feedback cedo e atualizar backlog, testes e contratos antes do próximo incremento.

## Artefatos e evidências de saída

- PRs pequenos, ligados a issue/requisito.
- Código integrado e demonstrável.
- Evidência de CI, revisão e testes.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Critérios da fatia cobertos por evidências.
- Definition of Done aplicável cumprida.
- Nenhum bloqueador conhecido é ocultado como tarefa futura.

## Falhas e cuidados

Evitar construir banco inteiro e depois todas as telas sem integração incremental.

**Trabalho paralelo permitido:** QA, observabilidade e revisão de protótipo.

**Exemplo orientativo:** Lançamento de presença completo: seleção, gravação, mensagem e consulta posterior.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
