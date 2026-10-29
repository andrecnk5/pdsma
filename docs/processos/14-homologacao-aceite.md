# P14 — Homologação, UAT e aceite

> **Estado:** referência v1.0 aprovada em 29/10/2026 e adaptável por projeto. A ordem numérica é didática, não uma cascata.

## Objetivo e responsabilidades

Separar qualidade técnica de aceitação funcional, com versão e evidências observáveis.

**Responsável primário:** Produto e usuários-chave. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Definir responsáveis, participantes, build, ambiente representativo, massa de dados apropriada e roteiro vinculado aos critérios.
2. Executar tarefas do TO-BE com cenário normal, exceções e permissões, observando sucesso, dificuldades e erros.
3. Registrar resultado por teste com responsável, data, versão, evidência e diferença entre esperado e observado.
4. Classificar problemas como bloqueador, defeito não bloqueante ou melhoria futura; corrigir com regressão proporcional.
5. Avaliar limitações de amostra, dispositivos, conectividade e acessibilidade na validade dos resultados.
6. Registrar decisão formal: aceito, condicionado com critérios claros ou rejeitado; preservar pendências rastreáveis.
7. Não tratar UAT ou aceite funcional como autorização automática para produção.

## Artefatos e evidências de saída

- Plano e relatório UAT vinculados a requisitos.
- Defeitos e decisões de tratamento.
- Aceite com versão, responsável, data e condição.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Todos os critérios críticos foram exercitados ou justificadamente bloqueados.
- Riscos e pendências são visíveis ao decisor.
- O aceite identifica exatamente qual versão foi analisada.

## Falhas e cuidados

Demonstração por desenvolvedor não substitui tarefa executada por usuário.

**Trabalho paralelo permitido:** Planejamento de release e observabilidade.

**Exemplo orientativo:** Professor confirma registro e a coordenação confere trilha de correção pós-fechamento.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
