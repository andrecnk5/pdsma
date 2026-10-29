# P03 — Viabilidade, restrições e riscos

> **Estado:** proposta v0.1, sujeita a revisão e adaptação. A posição numérica é didática: não representa fases isoladas.

## Objetivo e responsabilidades

Verificar valor, possibilidade de entrega, dependências, custos, obrigações e riscos antes de investimentos difíceis de reverter.

**Responsável primário:** Produto e Engenharia. A participação de usuários, UX, engenharia, dados, QA, segurança ou operações deve ser acionada conforme risco e dependência.

## Entradas e pré-condições

Consultar artefatos e decisões produzidos anteriormente que sejam necessários ao incremento em questão. Caso uma dependência esteja indefinida, documentar premissa, risco e responsável; provas de conceito não requerem que toda a experiência de uso já esteja aprovada.

## Passo a passo operacional

1. Levantar recursos humanos, custos iniciais e recorrentes, prazo imposto, requisitos contratuais e disponibilidade dos interessados.
2. Investigar dispositivos, conectividade, integrações, API externa, identidade, dados legados, hospedagem e governança de acesso.
3. Registrar riscos com probabilidade, impacto, responsável, mitigação e gatilho de reavaliação; separar riscos de pressupostos.
4. Para dúvidas técnicas de alto impacto, criar provas de conceito pequenas e descartáveis, sem confundi-las com software aprovado para produção.
5. Comparar alternativas usando critérios relevantes para o problema e documentar compromissos aceitos.
6. Submeter decisão de seguir, alterar o escopo, realizar pesquisa adicional ou encerrar a iniciativa.

## Artefatos e evidências de saída

- Registro de riscos priorizado, dependências e restrições.
- Avaliação proporcional de alternativas e viabilidade.
- Decisão explícita com data, responsável e condições.

O formato pode ser Markdown, issue, protótipo ou relatório, desde que contenha estado, versão, responsável, data e links para decisões e requisitos relacionados.

## Critérios verificáveis de conclusão

- Dependências que podem bloquear o módulo são conhecidas.
- Riscos graves têm dono e resposta proposta.
- Não se apresentou estimativa preliminar como prazo garantido.

## Falhas e cuidados

Ignorar custo operacional e risco de fornecedor; escolher stack apenas por preferência.

**Trabalho paralelo permitido:** Descoberta, protótipos exploratórios e pesquisa técnica.

**Exemplo orientativo:** Verificar se existe forma autorizada de integrar dados de um sistema escolar anterior.

## Controle e relações

A passagem para uma implementação, homologação ou publicação deve observar as dependências e o controle A–D aplicável. Consulte [fluxo e controles](../02-fluxo-e-controles.md), [papéis](../03-papeis.md) e [matriz de rastreabilidade](../05-rastreabilidade.md). Quando uma descoberta exigir revisão, atualize as evidências e não descarte automaticamente código válido.

[Voltar ao índice principal](../../README.md)
