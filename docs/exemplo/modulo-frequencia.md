# Exemplo fictício integrado — Módulo de frequência

> Situação pedagógica fictícia: não descreve requisitos aprovados de uma escola real nem autoriza acesso a registros de estudantes.

## Descoberta e hipótese

Problema hipotético: frequência registrada mais de uma vez causa retrabalho e divergência. A equipe entrevista professores e assistência, observa AS-IS, desenha TO-BE e mede a frequência de correções. A hipótese do produto é diminuir tempo de lançamento sem perder integridade histórica.

## Escopo do primeiro incremento

Incluído: listar turmas autorizadas, selecionar data, lançar presenças, salvar, consultar e corrigir conforme permissão. Excluído: boletim, análises anuais, mensagens a famílias e migração histórica integral.

## Requisitos demonstrativos

| ID | Comportamento | Evidência |
| --- | --- | --- |
| RF-001 | Professor lista apenas turmas autorizadas | TC-001 |
| RF-002 | Grava presença sem duplicação | TC-002 |
| RF-003 | Consulta histórico com data e autoria | TC-003 |
| RN-001 | Mudança de identidade não transfere histórico da matrícula | TC-004 |
| RN-002 | Correção pós-fechamento exige motivo, autorização e versão anterior | TC-005 |
| RNF-001 | Fluxo por teclado com foco e mensagens | TC-006 |

## Fluxos UX

Principal: autenticar → escolher turma e data → marcar → revisar → salvar → confirmar → consultar. Alternativos: sem turma, conectividade perdida, dados conflitantes, sem permissão e correção após fechamento. Prototipar os estados necessários e testar tarefas com representantes.

## Dados e arquitetura

Entidades conceituais: Pessoa, Identidade, Matrícula, VínculoTurma com validade temporal, Aula, Frequência, EventoCorreção, AtorAutorizado. O modelo exato depende da descoberta. API valida permissão por recurso e regras no servidor; banco usa chaves, restrições e transações pertinentes. Troca de chave de vínculo não pode silenciosamente reatribuir histórico.

## Construção por fatias

1. Walking skeleton: interface de teste → API autenticada → banco sintético → CI e homologação.
2. Fatia 1: listar turma autorizada, com estados vazio e proibido.
3. Fatia 2: registrar e consultar, cobrindo duplicidade e erro de rede.
4. Fatia 3: fechamento e correção auditável, com testes negativos e positivos.
5. Homologação: professor executa tarefas, responsável verifica histórico, QA consolida evidências.
6. Piloto autorizado: logs e indicadores, suporte e comparação da hipótese à linha de base.

## Critérios para considerar pronto

O cenário completo funciona, dados são preservados, permissões e exceções foram verificadas, DoD foi atendida, UAT é rastreável e existe decisão específica para qualquer publicação.

[Índice](../../README.md) · [Rastreabilidade](../05-rastreabilidade.md)
