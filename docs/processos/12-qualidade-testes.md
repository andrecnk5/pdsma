# P12 — Qualidade e testes contínuos

> **Estado:** proposta v0.1, sujeita a revisão e adaptação. A posição numérica é didática: não representa fases isoladas.

## Objetivo e responsabilidades

Verificar comportamento e riscos continuamente, desde os requisitos e critérios de aceite.

**Responsável primário:** QA em conjunto com Engenharia. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Desenhar estratégia por criticidade, níveis de teste, massa sintética, ambientes e oráculos de resultado.
2. Preparar testes positivos, negativos, limites, estados e concorrência a partir das regras e cenários reais.
3. Distribuir unidade, integração/contrato, E2E e exploração manual conforme custo e risco; pirâmide de testes é heurística, não percentual obrigatório.
4. Automatizar regressões em PR e integração; separar testes instáveis e corrigir suas causas.
5. Revisar acessibilidade real, falhas de rede, segurança, migrações e resultados em dispositivos e navegadores relevantes.
6. Registrar defeito com reprodução, impacto, versão, evidência e reteste; diferenciar bug, mudança e melhoria.
7. Consolidar riscos residuais e coberturas de requisitos críticos antes da homologação.

## Artefatos e evidências de saída

- Plano e matriz de testes vinculados aos requisitos.
- Automação e registros de execução.
- Defeitos, regressão e parecer de qualidade.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Requisitos críticos possuem testes rastreáveis e executados.
- Cenários negativos de autorização e integridade foram verificados.
- Falhas bloqueantes possuem tratamento explícito.

## Falhas e cuidados

Cobertura de linhas e CI verde não comprovam qualidade total.

**Trabalho paralelo permitido:** Começa no refinamento e continua durante construção e publicação.

**Exemplo orientativo:** Rejeitar tentativa direta à API de editar frequência de turma não autorizada.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
