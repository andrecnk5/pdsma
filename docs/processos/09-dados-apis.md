# P09 — Dados, APIs e integrações

> **Estado:** proposta v0.1, sujeita a revisão e adaptação. A posição numérica é didática: não representa fases isoladas.

## Objetivo e responsabilidades

Estabelecer contratos e integridade a partir de fluxos e regras, preservando a história e protegendo dados.

**Responsável primário:** Engenharia e Dados. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Definir glossário e distinções de domínio, como Pessoa, Identidade, Matrícula, Vínculo temporal, Turma e Registro.
2. Modelar entidades, cardinalidades, restrições, estados e eventos; confirmar que o esquema responde aos cenários reais.
3. Proteger invariantes críticas na camada de aplicação e, quando pertinente, no PostgreSQL ou banco escolhido, incluindo transações e chaves.
4. Descrever API com métodos, entradas, saídas, autorização, erros, idempotência e contratos OpenAPI quando aplicável.
5. Cobrir mudanças concorrentes, duplicidade de requisições, falhas de integração e estratégias seguras de migração/versionamento.
6. Prever auditoria, minimização, retenção, descarte e não exposição de identificadores em logs ou respostas indevidas.
7. Criar testes negativos de alteração indevida de vínculos e testes positivos da criação legítima de novos vínculos.

## Artefatos e evidências de saída

- Modelo conceitual e lógico, dicionário e invariantes.
- Contrato da API e matriz de permissões.
- Migrações e testes de integridade e compatibilidade.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Não é possível transferir histórico apenas mudando cadastro sem ato válido.
- Os erros e limites da API são conhecidos.
- Mudanças de contrato têm avaliação de impacto e compatibilidade.

## Falhas e cuidados

Não depender só de validação do frontend nem apagar histórico com atualização silenciosa.

**Trabalho paralelo permitido:** UX de estados, arquitetura e walking skeleton.

**Exemplo orientativo:** Troca de identidade relacionada à matrícula não deve reatribuir registros de frequência anteriores.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
