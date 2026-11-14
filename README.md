# Majora's Mask 3D — Tradução PT-BR (Moonfall Curse / TriAevum)

> **Em desenvolvimento — base experimental.** Não é uma tradução completa, nem há lançamento público estável.

Projeto de tradução para português brasileiro de *The Legend of Zelda: Majora's Mask 3D*, voltado ao port nativo **Moonfall Curse**, da família TriAevum. O teste realizado até agora utiliza a **ROM europeia (EUR)**, com o jogo configurado para inglês.

## Estado verificado

- O Forge reconheceu `imports/mm3d-message-specs.json`, aplicou alterações e exibiu falas do banqueiro de Clock Town em português.
- Os acentos testados apareceram corretamente com a fonte HD.
- Há **28 entradas PT-BR no catálogo experimental**. Isso não corresponde a 28 conversas completas; várias falas continuam em inglês.
- O teste é **parcial em jogo**: parte das falas do banqueiro foi observada em PT-BR. O conjunto inteiro ainda requer revisão e testes.
- A mensagem **0477** foi removida das substituições porque o Forge reserva esse ID para o sistema de preços (`overlapping dialogue/price owner`).

## Instalação experimental

1. Instale e configure o Moonfall Curse Forge normalmente com sua própria ROM EUR compatível.
2. Com o jogo fechado, localize a **pasta de dados do Forge** (não assuma que é a pasta do executável).
3. Crie `imports` nessa pasta, caso necessário.
4. Copie `distribuicao/mm3d-message-specs.json` para `imports/mm3d-message-specs.json`. **Faça backup** se esse arquivo já existir.
5. Desative **Custom RomFS folder** durante o teste (a camada preparada de mensagens pode ter prioridade sobre o overlay).
6. Clique em **Apply changes** no Forge e inicie o jogo com idioma inglês.

Para reverter, restaure o JSON anterior (ou remova o JSON experimental se não existia), clique em **Apply changes** e reinicie o jogo.

**Não copie ROMs, arquivos `.gmsg` originais ou dados protegidos para este repositório.**

## Organização

- `catalogo/ptbr.json` — **fonte editável** das 28 entradas preliminares.
- `distribuicao/mm3d-message-specs.json` — JSON pronto para o Forge, com as regras originais dos cinco idiomas mais o catálogo PT-BR no idioma inglês.
- `ferramentas/gerar_specs.py` — recria o arquivo de distribuição a partir do catálogo e das especificações oficiais.
- `referencias/price-plan.json` — lista de IDs reservados pelos ajustes de preços do Forge (somente dados de configuração).
- `docs/ESTADO.md` — detalhes técnicos e limitações.

A geração normalmente busca uma versão **fixada** das especificações oficiais para evitar mudanças silenciosas:

```powershell
py .\ferramentas\gerar_specs.py
```

Para trabalhar com uma versão local das especificações, use `--base caminho.json`. Verifique primeiro a compatibilidade com sua versão do Forge. O gerador interrompe o processo diante de conflitos de IDs de preços ou de regras já existentes.

## Limitações e próximos passos

Ainda é necessário ampliar a cobertura, revisar o contexto dos diálogos, preservar variáveis de nome/quantidade e comandos especiais, validar o orçamento de texto e verificar compatibilidade a cada atualização do port. Mensagens gerenciadas pelo sistema de preços exigem uma integração própria, não uma segunda edição independente do mesmo ID.

## Créditos e direitos

- Projeto de tradução PT-BR: [XandasL](https://github.com/XandasL).
- Port e mecanismo Forge: [coccofresco/TriAevum](https://github.com/coccofresco/TriAevum).
- As especificações-base e o plano de preços em `distribuicao` e `referencias` foram derivados do projeto TriAevum, cujo código-fonte indica **GPL-3.0-or-later**. Consulte o repositório upstream para as licenças e créditos originais.
- *The Legend of Zelda* e *Majora's Mask 3D* pertencem aos respectivos titulares. Este repositório não distribui o jogo nem seus arquivos originais.

O pacote é **experimental**, sem garantia de compatibilidade com atualizações futuras.
