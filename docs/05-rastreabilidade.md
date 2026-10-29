# Matriz de rastreabilidade ponta a ponta

Acompanhe **necessidade → requisito → regra → UX → arquitetura/API → issue/PR → teste → homologação → release**. O vínculo é mais importante que a ferramenta. Pode ser uma tabela Markdown, uma issue com links ou ferramenta especializada, desde que a evidência seja recuperável.

| Necessidade | Requisito | Regra | Fluxo | Decisão/contrato | PR | Teste | UAT | Release |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lançar presença | RF-001 | RN-001 | UX-001 | API-FREQ | Exemplo | TC-001 | UAT-001 | REL-001 |
| Preservar histórico | RF-002 | RN-004 | UX-003 | ADR-0001 | Exemplo | TC-004 | UAT-002 | REL-001 |

**Valores ilustrativos — não são issues ou releases existentes.**

## Regras de integridade documental

1. RF/RN crítico sem teste é lacuna, não cobertura.
2. Mudança de regra deve revisar impacto em UX, API, dados e testes.
3. Todo PR material explica quais necessidades e decisões altera.
4. Teste registra versão, resultado e evidência; cobertura percentual não substitui verificação.
5. Homologação identifica cenário, responsável e versão; release identifica commit/tag e ambiente.
6. Auditoria pode exigir muitos-para-muitos entre regras, casos e evidências; não forçar 1:1.
7. Não declarar implementação, aprovação ou disponibilização a partir da mera existência de um registro.

## Verificação antes do aceite

- [ ] Requisitos críticos possuem testes negativos e positivos relevantes.
- [ ] Sem divergência material não decidida entre protótipo e fluxo implementado.
- [ ] Integridade histórica e autorização cobertas até o armazenamento.
- [ ] Riscos residuais e decisões de liberação identificados.

[Índice](../README.md)
