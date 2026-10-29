# P10 — Repositório, ambientes, CI e integração mínima

> **Estado:** referência v1.0 aprovada em 29/10/2026 e adaptável por projeto. A ordem numérica é didática, não uma cascata.

## Objetivo e responsabilidades

Garantir mudanças revisáveis, ambiente reproduzível e verificação automatizada cedo.

**Responsável primário:** Engenharia e DevOps. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Definir repositório, README, CONTRIBUTING, organização de código, convenções de commits e proteção da branch principal.
2. Selecionar branch strategy simples, revisões por PR e autorização de merge compatível com o tamanho da equipe.
3. Adicionar linters, formatadores, análise estática e testes rápidos; fazer CI falhar quando verificações obrigatórias falham.
4. Configurar dev, homologação e produção na medida da necessidade, mantendo segregação de dados e segredos.
5. Usar tokens de menor privilégio, gerenciador de segredos e configurações por ambiente; nunca versionar senhas reais.
6. Implementar walking skeleton: cliente → serviço → persistência → teste → deploy controlado, ainda sem todas as funcionalidades.
7. Documentar como reproduzir, testar, observar, implantar e recuperar; revisar permissões do pipeline e dependências.

## Artefatos e evidências de saída

- Estrutura, políticas e PR template do repositório.
- Pipeline de CI com resultados observáveis.
- Ambiente controlado e integração mínima executável.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Outra pessoa consegue executar com instruções.
- Segredos não estão no repositório.
- Uma operação mínima atravessa as camadas e pode ser verificada.

## Falhas e cuidados

Docker, GitFlow e Sprint 0 não são requisitos universais.

**Trabalho paralelo permitido:** Pesquisa e UX; contratos evoluem sem depender de UI definitiva.

**Exemplo orientativo:** Página de teste chama API autenticada e grava registro sintético em homologação.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
