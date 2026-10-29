# Contribuição e revisão

## Fluxo

1. Abra issue com problema, fonte, impacto e proposta verificável.
2. Crie branch temática, por exemplo docs/revisao-ux.
3. Edite Markdown com um H1, seções H2/H3, vocabulário consistente, links relativos e sem dados sensíveis reais.
4. Para mudança material, identifique impacto em requisitos, UX, arquitetura, QA, dados, segurança e controles.
5. Execute: python scripts/validar_documentacao.py
6. Abra PR com issue/decisão, escopo, riscos, critérios de aceite e evidência.
7. Aguarde revisão humana autorizada; CI verde não equivale a aprovação.
8. Atualize CHANGELOG quando o processo ou suas políticas mudarem.

## Regras editoriais

Diferencie afirmações normativas de recomendações contextualizadas. Não prescreva prazo, ferramenta ou método como universal. Cite fonte oficial, versão e status. Preserve IDs estáveis e histórico de decisões. Exemplos sensíveis devem usar dados sintéticos.

## Estados e versões

Proposto → Em revisão → Aprovado / Rejeitado → Substituído. A versão v0.x é experimental; passar para v1.0 depende de decisão explícita do responsável. Considere CODEOWNERS e ruleset somente quando configurados com permissões reais.

[Índice](README.md)
