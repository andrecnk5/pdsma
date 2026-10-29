# P15 — Publicação, operação e recuperação

> **Estado:** referência v1.0 aprovada em 29/10/2026 e adaptável por projeto. A ordem numérica é didática, não uma cascata.

## Objetivo e responsabilidades

Entregar em destino autorizado com capacidade de identificar incidentes e recuperar serviço.

**Responsável primário:** Operações e responsável por release. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Definir destino: homologação, piloto restrito ou produção, público habilitado e autoridade para publicar.
2. Preencher checklist de release: build, commits, dados, configurações, HTTPS, permissões, testes, backups e migrações.
3. Preparar recuperação ou rollback realista; reverter aplicativo não desfaz alterações destrutivas de banco.
4. Realizar deploy controlado e smoke tests funcionais e de autorização após publicação.
5. Ativar logs saneados, métricas, rastreio e alertas proporcionais à criticidade; definir responsável de plantão e suporte.
6. Registrar incidente, impacto, decisão de correção/desativação, comunicação e versão remediada.
7. Documentar release e comparar comportamento pós-publicação aos critérios operacionais de aceitação.

## Artefatos e evidências de saída

- Registro de release e autorização de destino.
- Checklist, backup/recuperação e smoke test.
- Monitoramento, notas de versão e contatos responsáveis.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Existe autorização específica e trilha de implantação.
- A recuperação é plausível e testada de acordo com o risco.
- Telemetria e suporte cobrem situações críticas.

## Falhas e cuidados

Não publicar porque 'passou no teste'; não presumir rollback do esquema sem plano.

**Trabalho paralelo permitido:** Final da homologação e preparação do suporte.

**Exemplo orientativo:** Piloto com duas turmas, observando erro de salvamento, disponibilidade e suporte.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
