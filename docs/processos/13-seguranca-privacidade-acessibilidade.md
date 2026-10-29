# P13 — Segurança, privacidade e acessibilidade

> **Estado:** proposta v0.1, sujeita a revisão e adaptação. A posição numérica é didática: não representa fases isoladas.

## Objetivo e responsabilidades

Incorporar proteção e inclusão transversalmente, tratando obrigações legais de modo contextual.

**Responsável primário:** Segurança e privacidade com UX/Engenharia. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Inventariar dados, finalidades, papéis, acesso, retenção e descarte; aplicar minimização e avaliar LGPD quando pertinente.
2. Modelar ameaças de autenticação, autorização por recurso, manipulação de identificadores, vazamento e alterações históricas.
3. Selecionar controles verificáveis com NIST SSDF e OWASP ASVS como referências, de acordo com os riscos.
4. Definir níveis-alvo de acessibilidade (ex.: WCAG 2.2 AA), tarefas com teclado, foco, rótulos, contraste e mensagens de erro.
5. Aplicar controles em servidor, banco, API, frontend, pipeline e operação; gerenciar segredos e dependências.
6. Testar combinações de automação e validação manual, inclusive tecnologias assistivas e abuso de API.
7. Registrar riscos residuais e aceitação por autoridade legítima; preparar resposta a incidentes e recuperação.

## Artefatos e evidências de saída

- Matriz de dados e autorização, ameaças e controles.
- Critérios de acessibilidade e testes.
- Parecer de riscos e plano de resposta proporcional.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Segurança não depende somente de interface.
- Critérios de risco alto possuem evidências de teste.
- Não se declara conformidade sem avaliação efetiva e abrangente.

## Falhas e cuidados

Login não prova conformidade legal; scanner não substitui validação; protótipo não substitui WCAG na aplicação.

**Trabalho paralelo permitido:** Todas as demais atividades.

**Exemplo orientativo:** Impedir por regra de servidor que um professor visualize frequência de turma sem atuação legítima.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
