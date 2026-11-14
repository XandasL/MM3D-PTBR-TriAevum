# Registro técnico e estado dos testes

## Confirmado no jogo (testes locais do autor)
- O Custom RomFS folder aplicado isoladamente exibiu a mensagem de sucesso, mas o banqueiro permaneceu em inglês.
- O caminho `imports/mm3d-message-specs.json` fez o Forge preparar mensagens substituídas; falas do banqueiro apareceram em PT-BR.
- Acentos testados (como ç, ã e ê) apareceram corretamente.
- Os lotes eram parciais: algumas falas inteiras permaneceram em inglês.
- Uma versão anterior falhou em **Preparing assets** com `en: MM messages: overlapping dialogue/price owner`.
- O conflito conhecido foi identificado no ID **0477**; a versão atual exclui esse ID. O conjunto corrigido ainda exige teste integral em jogo.

## Verificado no código do Forge
- `forge-assets/src/mm3d_ui.rs` lê `imports/mm3d-message-specs.json` se existir; do contrário usa `titles/mm3d/dekui/setup/reviewed-dialogue.json`.
- A especificação deve conter exatamente `en`, `de`, `fr`, `es` e `it`.
- O preparador produz arquivos GMSG de camada preparada e recursos de fonte.
- `mm3d_messages.rs` aplica regras de diálogo e de preço; IDs duplicados entre as duas classes são rejeitados.
- Plano original de preços: `titles/mm3d/dekui/setup/price-plan.json`. O catálogo não deve tomar posse de seus IDs.

## Limitações atuais
- **28 entradas PT-BR**, não 28 conversas completas. O lote inclui banqueiro e algumas mensagens simples da Casa do Tesouro.
- Mensagens com valores variáveis ou comandos complexos ainda não foram portadas.
- Os controles de fluxo, as quebras de linha e as fontes precisam de teste em diferentes diálogos.
- O JSON pronto foi preparado sobre especificações oficiais em revisão conhecida. Não foi validado universalmente em todas as versões do Forge.
- Este repositório não contém nenhum `.gmsg` extraído da ROM.

## Fontes
- https://github.com/coccofresco/TriAevum/blob/main/tools/triaevum_forge/crates/forge-assets/src/mm3d_ui.rs
- https://github.com/coccofresco/TriAevum/blob/main/tools/triaevum_forge/crates/forge-assets/src/mm3d_messages.rs
- https://github.com/coccofresco/TriAevum/blob/main/titles/mm3d/dekui/setup/price-plan.json
