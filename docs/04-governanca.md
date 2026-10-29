# Governança documental e mudanças

## Fonte de verdade

Decisões e artefatos versionados são referências oficiais do projeto que os adotar. Issues, reuniões e conversas são fontes de contexto e devem ser vinculadas; não substituem registro de decisão quando a alteração afeta comportamento, dados, segurança ou escopo.

## Padrões GitHub propostos

- Branch principal estável; mudança por branch temática e Pull Request.
- PR pequeno, issue e decisão vinculadas, testes e impacto descritos.
- CODEOWNERS sugere mantenedor editorial; exigência de revisão depende de ruleset/branch protection realmente configurado.
- Workflow de documentação valida títulos e links locais; revisores avaliam coerência técnica e fontes.
- Preferir nomes minúsculos, hífens e Markdown UTF-8 com um H1 por documento.
- Nunca armazenar segredos ou dados reais de estudantes em issues, código ou exemplos.

## Tipos de mudança

**Editorial:** ortografia, navegação e formatação sem alterar comportamento ou interpretação.  
**Material:** altera sequência, controle, critério de aceite, papel, dado, API, risco, política ou obrigação.

Para mudança material: criar issue → justificar e identificar fontes → mapear impactos cruzados → registrar decisão competente → PR → CI e revisão → merge autorizado → CHANGELOG → comunicar quem usa a documentação.

## Rastreabilidade e estados

IDs de requisitos, decisões e testes permanecem estáveis. Estados possíveis: proposto, em revisão, aprovado, substituído, rejeitado. Não reescrever história: decisões substituídas devem apontar para sucessoras e manter sua justificativa.

## Métricas

Avaliar tempo entre descoberta e feedback, retrabalho por ambiguidade, falhas detectadas antes/depois da homologação e incidentes de release. Métricas de engenharia descrevem fluxo e qualidade, não desempenho individual isolado.

## Governança da própria v0.1

Esta versão foi proposta para revisão. A passagem para v1.0 exige decisão explícita do responsável, revisão dos controles A–D, papéis, fontes, política de alteração e licença. Um PR criado ou CI verde não constitui aprovação.

[Índice](../README.md)
