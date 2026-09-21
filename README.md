# 🐰 DUNYA

Jogo desenvolvido em **Python** com a biblioteca **Pygame**, para a disciplina de Programação.

DUNYA é um "diário de bordo" em forma de jogo: uma coelhinha que precisa se defender de ondas de flores, em um cenário noturno tomado por montanhas roxas e um céu estrelado. A estética segue uma paleta em tons de rosa, roxo e verde, com visual em pixel art — inspirada em clássicos do estilo *Space Invaders*, mas com uma identidade mais fofa e colorida.

## 🎮 Sobre o jogo

O jogador se move apenas na horizontal e atira para cima, precisando eliminar todas as flores antes que elas alcancem a base. O jogo tem elementos próprios que fogem do clássico:

- 🍫 **Blocos de chocolate** — servem de escudo e vão perdendo pedaços conforme são atingidos;
- 🍬 **Candy** — doce-bônus que atravessa a tela de vez em quando, valendo pontos extras;
- 🌸 **Flores** — os inimigos, organizados em uma grade que avança pela tela.

O jogo tem **3 fases** com dificuldade crescente:

| Fase | Linhas x Colunas | Velocidade das flores | Intervalo de tiro inimigo |
|---|---|---|---|
| 1 — Fácil | 3 x 9 | 1.0 | a cada 100 quadros |
| 2 — Média | 4 x 10 | 1.6 | a cada 75 quadros |
| 3 — Difícil | 5 x 11 | 2.3 | a cada 50 quadros |

A tela do jogo tem **1000 x 650 pixels**.

## 🕹️ Como jogar

- **Setas esquerda/direita (← →)** — move a coelhinha pela horizontal;
- **Barra de espaço** — atira;
- Elimine todas as flores da fase para avançar, sem deixar sua vida chegar a zero.

> Ajuste os controles acima caso o mapeamento de teclas no código seja diferente.

## 🧩 Estrutura do código

O código é organizado em classes, cada uma cuidando de uma parte do jogo:

- **Jogador** — controla o movimento da coelhinha, suas vidas e o tempo de invencibilidade após levar dano;
- **Flor** — representa cada inimigo da grade, com posição e tamanho próprios;
- **Tiro** — cuida dos projéteis, tanto os da coelhinha (estrelinhas amarelas) quanto os das flores (retângulos vermelhos);
- **Chocolate** — os blocos de escudo, que vão perdendo pedaços conforme são atingidos;
- **Candy** — o doce-bônus que atravessa a tela valendo pontos extras.

O jogo roda em um *game loop* principal: a cada quadro, lê o teclado, atualiza a posição de todos os elementos, verifica colisões e redesenha a tela. Uma máquina de estados simples controla as telas de menu, jogo, game over e vitória.

Os sprites são desenhados em **pixel art via matriz de texto**: `0` é espaço vazio, `1` é a cor principal e `2` marca uma cor secundária. Cada célula diferente de zero vira um retângulo colorido na tela.

## ▶️ Como rodar

```bash
# instale o Pygame
pip install pygame

# rode o jogo
python main.py
```

> Ajuste `main.py` para o nome real do arquivo principal do projeto.

## 📋 Requisitos

- Python 3.x
- Pygame

## 📖 Diário de bordo

O processo completo de criação — do desenho no papel até o código, incluindo os erros encontrados durante a programação e como foram corrigidos — está documentado em [`DUNYA_Diario_de_Bordo.pdf`](./DUNYA_Diario_de_Bordo.pdf).

## 👩‍💻 Autoras

- Wanessa Santos
- Emilly Cardoso

---

*Trabalho da disciplina de Programação.*
