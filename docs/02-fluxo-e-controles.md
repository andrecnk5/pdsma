# Fluxo de trabalho, dependências e critérios de passagem

## Mapa conceitual

    Necessidade → Descoberta / AS-IS / Viabilidade
                 ↓
       Incremento / Requisitos / Backlog
                 ↓
      UX e protótipos ↔ Domínio / Arquitetura / API
                 ↘          ↙
              CI / integração mínima
                       ↓
              Fatias verticais
                       ↓
         Testes e proteção contínuos
                       ↓
         Homologação e aceite
                       ↓
       Release no destino autorizado
                       ↓
             Uso e aprendizagem
                       ↺

## Paralelismo responsável

A equipe pode preparar CI e repositório enquanto usuários testam protótipos, pesquisar tecnologias antes de fechar o visual e escrever testes durante o refinamento. O que **não** convém consolidar prematuramente: telas definitivas sem fluxo esclarecido; contratos de domínio que dependem de regras não validadas; divulgação em produção sem aceite e plano operacional.

## Controle A — Problema e escopo

**Responsável:** Produto. **Momento:** antes do investimento substancial na solução.
- [ ] Problema, usuários e hipóteses identificados com evidência e limitações.
- [ ] Valor esperado, alternativas, restrições e primeiro corte definidos.
- [ ] Decisão registrada: continuar, pesquisar mais, ajustar ou interromper.

## Controle B — Prontidão funcional e UX

**Responsável:** Produto com UX/Análise/QA. **Momento:** antes da implementação definitiva dos fluxos correspondentes.
- [ ] Regras, permissões, erros e critérios de aceite estão compreendidos.
- [ ] Wireframes/protótipos necessários foram apreciados ou testados proporcionalmente ao risco.
- [ ] Divergências materiais possuem dono, tratamento e decisão.

## Controle C — Prontidão técnica

**Responsável:** Engenharia. **Momento:** antes de comprometer contratos e implementação da fatia.
- [ ] Domínio, dados, API, autorização e arquitetura mínimos definidos.
- [ ] Riscos técnicos e ADRs relevantes registrados.
- [ ] CI e estratégia de teste do incremento são executáveis.

## Controle D — Aceite e disponibilização

**Responsáveis:** Produto para negócio e alçada operacional para release. **Momento:** antes de disponibilizar ao público do destino.
- [ ] Build integrado e critérios de qualidade atendidos.
- [ ] UAT e riscos residuais documentados; bloqueadores não ignorados.
- [ ] Destino, versão, backup/recuperação, observabilidade e responsáveis autorizados.

## Registro de controle

Registrar: código A/B/C/D, incremento e versão, evidências, decisão (aprovado, condicionado ou não aprovado), pendências, responsável, data, validade e gatilho de reavaliação. Os controles não exigem reuniões isoladas nem devem bloquear pesquisa técnica descartável.

**Em caso de falha:** preserve o código válido; identifique lacuna e corrija com rastreabilidade. Nenhum controle deve ser tratado como consentimento tácito.

[Papéis](03-papeis.md) · [Rastreabilidade](05-rastreabilidade.md) · [Índice](../README.md)
