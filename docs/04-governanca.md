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

## Aprovação da base v1.0

A base metodológica inicial foi aprovada pelo responsável em 29/10/2026, conforme [DEC-001](decisoes/DEC-001-aprovacao-base-v1.0.md). Os processos e controles formam uma referência adaptável, não uma certificação. Alterações materiais posteriores exigem avaliação e decisão registrada.

**Pendências independentes:** a licença de redistribuição permanece não definida e regras de proteção da branch principal ainda requerem configuração. Um PR criado ou CI verde não constitui, isoladamente, aprovação humana.

[Índice](../README.md)
