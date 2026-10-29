# Como utilizar o PDSMA

## Quem utiliza

Responsável de produto, analistas, designers, engenheiros, profissionais de dados, qualidade, segurança e operação. Papéis podem ser acumulados em equipes pequenas, mas a alçada de decisão deve permanecer explícita.

## Níveis de aplicação

| Nível | Aplicação | Evidências esperadas |
| --- | --- | --- |
| Enxuto | Projeto pequeno e riscos modestos | Visão, requisitos, fluxo, teste, aceite e release |
| Intermediário | Aplicação web com contas, persistência e integração | Processos P01–P16 e controles proporcionais |
| Reforçado | Dados sensíveis ou fluxos de alta criticidade | Ameaças, contratos formais, auditoria e testes especializados |

O objetivo é **evidência suficiente**, não documentos por obrigação. Registro curto em issue pode substituir documento extenso se mantiver decisão, contexto, versão e responsáveis.

## Roteiro de adoção

1. Defina problema, processo atual/futuro e viabilidade (P01–P03).
2. Escolha primeiro incremento e explicite requisitos e prioridades (P04–P06).
3. Desenvolva jornadas/protótipos e arquitetura/dados de modo coordenado (P07–P09).
4. Estruture CI e integração mínima, desenvolva em fatias com testes contínuos (P10–P13).
5. Homologue, publique somente no ambiente autorizado e meça resultados (P14–P16).

## Condições para adaptação

Ao dispensar algum artefato recomendado, registre risco e justificativa. Não dispense requisitos essenciais de segurança, integridade ou normas legais aplicáveis sob justificativa de agilidade. A aprovação do fluxo de um módulo não congela a arquitetura do produto inteiro.

## Convenções

IDs: RF-001, RN-001, RNF-001, US-001, UX-001, ADR-0001, DEC-001, RSK-001, TC-001, REL-001. Estados: proposto, em revisão, aprovado, substituído, rejeitado. O responsável pelo projeto determina a alçada de aprovação e registra a decisão.

[Índice](../README.md)
