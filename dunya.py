import pygame
import random
import sys

pygame.init()

LARGURA = 1000
ALTURA = 650
FPS = 60
TAMANHO_PIXEL = 6

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("DUNYA")
relogio = pygame.time.Clock()

# posições fixas das estrelinhas no céu (geradas uma vez só, senão fica piscando)
ESTRELAS = [(random.randint(0, LARGURA), random.randint(15, 280)) for _ in range(45)]

BRANCO = (255, 255, 255)
PRETO = (15, 12, 40)
ROSA = (255, 80, 150)
ROSA_CLARO = (255, 150, 200)
VERDE = (80, 210, 90)
VERDE_ESCURO = (40, 120, 60)
MARROM = (120, 55, 30)
MARROM_CLARO = (180, 90, 45)
AMARELO = (255, 210, 70)
ROXO = (90, 55, 170)
ROXO_CLARO = (140, 90, 220)
AZUL = (80, 210, 255)
VERMELHO = (255, 60, 80)
LARANJA = (255, 150, 40)
CINZA = (100, 100, 120)

FONTE = pygame.font.SysFont("arial", 28, bold=True)
FONTE_GRANDE = pygame.font.SysFont("arial", 55, bold=True)
FONTE_PEQUENA = pygame.font.SysFont("arial", 20, bold=True)

# sprites em pixel art (matriz de 0 e 1, "2" é uma cor extra)
# coelhinho visto de costas: orelhinhas juntas, corpo redondo e rabinho fofo embaixo
BUNNY = [
    "001101100",
    "001101100",
    "001101100",
    "011111110",
    "111111111",
    "111111111",
    "111111111",
    "011111110",
    "001111100",
    "011001100",
    "000222000"
]

FLOWER = [
    "0011100",
    "0111110",
    "1101011",
    "1111111",
    "0111110",
    "0011100",
    "0011100",
    "0111110",
    "0101010"
]

HEART = [
    "01100110",
    "11111111",
    "11111111",
    "01111110",
    "00111100",
    "00011000"
]

# erro - bala feia
CANDY = [
    "00011000",
    "00111110",
    "01111111",
    "11111111",
    "01111111",
    "00111110",
    "00011000"
]

STAR = [
    "00100",
    "01110",
    "11111",
    "01110",
    "00100"
]

SUN = [
    "000111000",
    "001111100",
    "011111110",
    "111111111",
    "111111111",
    "011111110",
    "001111100",
    "000111000"
]


def desenhar_sprite(sprite, x, y, tamanho, cores, escala=1):
    for linha, valores in enumerate(sprite):
        for coluna, valor in enumerate(valores):
            if valor != "0":
                cor = cores.get(valor, BRANCO)
                pygame.draw.rect(tela, cor, (x + coluna * tamanho * escala, y + linha * tamanho * escala, tamanho * escala, tamanho * escala))


def desenhar_fundo(fase):
    if fase == 1:
        fundo = (30, 25, 80)
        montanha = ROXO
    elif fase == 2:
        fundo = (20, 20, 65)
        montanha = (65, 50, 130)
    else:
        fundo = (10, 10, 35)
        montanha = (45, 35, 90)

    tela.fill(fundo)

    for ex, ey in ESTRELAS:
        pygame.draw.rect(tela, BRANCO, (ex, ey, 3, 3))

    # era pra ser uma bala rosa, não um sol :)
    desenhar_sprite(CANDY, 55, 55, 8, {"1": ROSA})

    pygame.draw.polygon(tela, montanha, [
        (0, 320), (100, 220), (190, 310), (300, 180), (410, 310),
        (520, 210), (650, 320), (760, 190), (900, 310), (1000, 230),
        (1000, 400), (0, 400)
    ])

    pygame.draw.rect(tela, VERDE_ESCURO, (0, 575, LARGURA, 75))
    pygame.draw.rect(tela, VERDE, (0, 575, LARGURA, 12))

    for x in range(0, LARGURA, 35):
        pygame.draw.rect(tela, VERDE, (x, 560, 8, 20))

    pygame.draw.rect(tela, MARROM, (0, 590, LARGURA, 60))

    for x in range(0, LARGURA, 40):
        pygame.draw.rect(tela, MARROM_CLARO, (x + 5, 605, 12, 8))


class Jogador:
    def __init__(self):
        self.largura = len(BUNNY[0]) * TAMANHO_PIXEL
        self.altura = len(BUNNY) * TAMANHO_PIXEL
        self.x = LARGURA // 2 - self.largura // 2
        self.y = 500
        self.velocidade = 6
        self.vidas = 3
        self.tempo_dano = 0

    def desenhar(self):
        desenhar_sprite(BUNNY, self.x, self.y, TAMANHO_PIXEL, {"1": BRANCO, "2": ROSA_CLARO})

    def atualizar(self, teclas):
        # só anda pros lados, igual no space invaders original (sem subir/descer)
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.x -= self.velocidade
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.x += self.velocidade

        self.x = max(10, min(LARGURA - self.largura - 10, self.x))

        if self.tempo_dano > 0:
            self.tempo_dano -= 1

    def receber_dano(self):
        if self.tempo_dano <= 0:
            self.vidas -= 1
            self.tempo_dano = 90


class Flor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = len(FLOWER[0]) * TAMANHO_PIXEL
        self.altura = len(FLOWER) * TAMANHO_PIXEL

    def desenhar(self):
        desenhar_sprite(FLOWER, self.x, self.y, TAMANHO_PIXEL, {"1": ROSA})
        pygame.draw.rect(tela, AMARELO, (self.x + 2 * TAMANHO_PIXEL, self.y + 3 * TAMANHO_PIXEL, 3 * TAMANHO_PIXEL, 3 * TAMANHO_PIXEL))
        pygame.draw.rect(tela, VERDE, (self.x + 3 * TAMANHO_PIXEL, self.y + 6 * TAMANHO_PIXEL, 2 * TAMANHO_PIXEL, 3 * TAMANHO_PIXEL))


class Tiro:
    def __init__(self, x, y, inimigo=False):
        self.x = x
        self.y = y
        self.inimigo = inimigo
        self.velocidade = 5 if inimigo else 10
        self.ativo = True

    def atualizar(self):
        self.y += self.velocidade if self.inimigo else -self.velocidade
        if self.y < -30 or self.y > ALTURA:
            self.ativo = False

    def desenhar(self):
        if self.inimigo:
            pygame.draw.rect(tela, VERMELHO, (self.x, self.y, 6, 20))
            return

        # brilhinho amarelo (estrelinha de 4 pontas) pro tiro do coelhinho
        cx = self.x + 3
        cy = self.y + 10
        pontos = [
            (cx, cy - 10),
            (cx + 3, cy - 3),
            (cx + 10, cy),
            (cx + 3, cy + 3),
            (cx, cy + 10),
            (cx - 3, cy + 3),
            (cx - 10, cy),
            (cx - 3, cy - 3),
        ]
        pygame.draw.polygon(tela, AMARELO, pontos)


class Chocolate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 110
        self.altura = 65
        self.vida = 8

    def desenhar(self):
        tamanho = 15
        for linha in range(4):
            for coluna in range(7):
                if self.vida <= 0:
                    return
                if (linha + coluna) % 7 < self.vida:
                    pygame.draw.rect(tela, MARROM, (self.x + coluna * tamanho, self.y + linha * tamanho, tamanho - 2, tamanho - 2))
                    pygame.draw.rect(tela, MARROM_CLARO, (self.x + coluna * tamanho + 2, self.y + linha * tamanho + 2, tamanho - 7, 4))

    def receber_dano(self):
        self.vida -= 1


CORES_CANDY = [ROSA_CLARO, AMARELO, AZUL, VERDE, ROXO_CLARO, LARANJA]


class Candy:
    def __init__(self):
        self.x = -80
        self.y = random.randint(80, 230)
        self.velocidade = 5
        self.ativo = True
        self.cor = random.choice(CORES_CANDY)  # cor sorteada a cada vez que ela nasce

    def atualizar(self):
        self.x += self.velocidade
        if self.x > LARGURA + 80:
            self.ativo = False

    def desenhar(self):
        desenhar_sprite(CANDY, self.x, self.y, 5, {"1": self.cor})


def criar_flores(fase):
    flores = []

    if fase == 1:
        linhas, colunas, dx, dy = 3, 9, 80, 65
    elif fase == 2:
        linhas, colunas, dx, dy = 4, 10, 75, 60
    else:
        linhas, colunas, dx, dy = 5, 11, 70, 55

    largura_total = (colunas - 1) * dx
    inicio_x = (LARGURA - largura_total) // 2
    inicio_y = 90  # mais pra cima, pra dar mais tempo antes delas chegarem embaixo

    for linha in range(linhas):
        for coluna in range(colunas):
            flores.append(Flor(inicio_x + coluna * dx, inicio_y + linha * dy))

    return flores


def desenhar_coracoes(vidas):
    for i in range(3):
        x = LARGURA - 50 - i * 42
        cor = ROSA if i < vidas else CINZA
        desenhar_sprite(HEART, x, 20, 4, {"1": cor})


def desenhar_interface(pontos, vidas, fase):
    texto = FONTE.render(f"Pontos: {pontos:05d}", True, BRANCO)
    tela.blit(texto, (25, 20))

    nome_fase = ["FÁCIL", "MÉDIA", "DIFÍCIL"][fase - 1]
    texto_fase = FONTE_PEQUENA.render(f"FASE {fase} - {nome_fase}", True, BRANCO)
    tela.blit(texto_fase, (25, 55))

    desenhar_coracoes(vidas)


def desenhar_menu():
    tela.fill(PRETO)
    desenhar_sprite(SUN, 80, 70, 8, {"1": AMARELO})

    titulo = FONTE_GRANDE.render("DUNYA", True, ROSA)
    subtitulo = FONTE.render("DIÁRIO DE BORDO", True, BRANCO)
    iniciar = FONTE.render("ENTER - INICIAR", True, AZUL)
    controles = FONTE_PEQUENA.render("WASD / SETAS = MOVIMENTO    ESPAÇO = ATIRAR", True, BRANCO)

    tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 180))
    tela.blit(subtitulo, (LARGURA // 2 - subtitulo.get_width() // 2, 245))
    tela.blit(iniciar, (LARGURA // 2 - iniciar.get_width() // 2, 360))
    tela.blit(controles, (LARGURA // 2 - controles.get_width() // 2, 430))

    pygame.display.flip()


def desenhar_game_over(pontos):
    tela.fill(PRETO)

    texto = FONTE_GRANDE.render("GAME OVER", True, VERMELHO)
    pontuacao = FONTE.render(f"Pontuação: {pontos}", True, BRANCO)
    reiniciar = FONTE.render("ENTER - JOGAR NOVAMENTE", True, AZUL)

    tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, 200))
    tela.blit(pontuacao, (LARGURA // 2 - pontuacao.get_width() // 2, 280))
    tela.blit(reiniciar, (LARGURA // 2 - reiniciar.get_width() // 2, 360))

    pygame.display.flip()


def desenhar_vitoria(pontos):
    tela.fill(PRETO)

    texto = FONTE_GRANDE.render("VOCÊ VENCEU!", True, ROSA)
    pontuacao = FONTE.render(f"Pontuação final: {pontos}", True, BRANCO)
    continuar = FONTE.render("ENTER - JOGAR NOVAMENTE", True, AZUL)

    tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, 200))
    tela.blit(pontuacao, (LARGURA // 2 - pontuacao.get_width() // 2, 280))
    tela.blit(continuar, (LARGURA // 2 - continuar.get_width() // 2, 360))

    pygame.display.flip()


def iniciar_fase(fase):
    jogador = Jogador()
    flores = criar_flores(fase)
    chocolates = [Chocolate(130, 455), Chocolate(360, 455), Chocolate(590, 455), Chocolate(820, 455)]

    tiros = []
    tiros_inimigos = []
    candy = None

    if fase == 1:
        velocidade_flores, intervalo_tiro = 1.0, 100
    elif fase == 2:
        velocidade_flores, intervalo_tiro = 1.6, 75
    else:
        velocidade_flores, intervalo_tiro = 2.3, 50

    direcao = 1
    pontos = 0
    contador = 0
    candy_timer = random.randint(500, 800)
    jogando = True

    while jogando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return "menu", pontos
                if evento.key == pygame.K_SPACE:
                    tiros.append(Tiro(jogador.x + jogador.largura // 2, jogador.y, False))

        teclas = pygame.key.get_pressed()
        jogador.atualizar(teclas)
        contador += 1

        # inimigos atiram de tempos em tempos
        if contador % intervalo_tiro == 0 and flores:
            flor = random.choice(flores)
            tiros_inimigos.append(Tiro(flor.x + flor.largura // 2, flor.y + flor.altura, True))

        for tiro in tiros:
            tiro.atualizar()
        for tiro in tiros_inimigos:
            tiro.atualizar()

        tiros = [t for t in tiros if t.ativo]
        tiros_inimigos = [t for t in tiros_inimigos if t.ativo]

        # movimento das flores (tipo space invaders)
        if flores:
            esquerda = min(f.x for f in flores)
            direita = max(f.x + f.largura for f in flores)

            if direita >= LARGURA - 20:
                direcao = -1
                for f in flores:
                    f.y += 6  # passo menor = desce mais devagar
            elif esquerda <= 20:
                direcao = 1
                for f in flores:
                    f.y += 6

            for f in flores:
                f.x += velocidade_flores * direcao

        # colisão dos tiros do jogador
        for tiro in tiros[:]:
            tiro_rect = pygame.Rect(tiro.x, tiro.y, 6, 20)
            acertou = False

            for flor in flores[:]:
                flor_rect = pygame.Rect(flor.x, flor.y, flor.largura, flor.altura)
                if tiro_rect.colliderect(flor_rect):
                    flores.remove(flor)
                    if tiro in tiros:
                        tiros.remove(tiro)
                    pontos += 100
                    acertou = True
                    break

            if acertou:
                continue

            if candy and candy.ativo:
                candy_rect = pygame.Rect(candy.x, candy.y, 40, 35)
                if tiro_rect.colliderect(candy_rect):
                    pontos += 500
                    if tiro in tiros:
                        tiros.remove(tiro)
                    candy = None
                    continue

            for choc in chocolates[:]:
                if choc.vida <= 0:
                    continue
                choc_rect = pygame.Rect(choc.x, choc.y, choc.largura, choc.altura)
                if tiro_rect.colliderect(choc_rect):
                    choc.receber_dano()
                    if tiro in tiros:
                        tiros.remove(tiro)
                    break

        # colisão dos tiros inimigos
        for tiro in tiros_inimigos[:]:
            tiro_rect = pygame.Rect(tiro.x, tiro.y, 6, 20)
            jogador_rect = pygame.Rect(jogador.x, jogador.y, jogador.largura, jogador.altura)

            if tiro_rect.colliderect(jogador_rect):
                jogador.receber_dano()
                if tiro in tiros_inimigos:
                    tiros_inimigos.remove(tiro)
                continue

            for choc in chocolates[:]:
                if choc.vida <= 0:
                    continue
                choc_rect = pygame.Rect(choc.x, choc.y, choc.largura, choc.altura)
                if tiro_rect.colliderect(choc_rect):
                    choc.receber_dano()
                    if tiro in tiros_inimigos:
                        tiros_inimigos.remove(tiro)
                    break

        # flor encostou no jogador ou chegou muito perto = game over
        jogador_rect = pygame.Rect(jogador.x, jogador.y, jogador.largura, jogador.altura)
        for flor in flores:
            flor_rect = pygame.Rect(flor.x, flor.y, flor.largura, flor.altura)
            if flor_rect.colliderect(jogador_rect) or flor.y + flor.altura >= 555:
                jogador.vidas = 0

        candy_timer -= 1
        if candy_timer <= 0 and candy is None:
            candy = Candy()
            candy_timer = random.randint(500, 900)

        if candy:
            candy.atualizar()
            candy_rect = pygame.Rect(candy.x, candy.y, 40, 35)

            if candy_rect.colliderect(jogador_rect):
                pontos += 500
                candy = None
            elif not candy.ativo:
                candy = None

        if jogador.vidas <= 0:
            return "gameover", pontos

        if not flores:
            return ("proxima" if fase < 3 else "vitoria"), pontos + 1000

        desenhar_fundo(fase)

        for choc in chocolates:
            choc.desenhar()
        for flor in flores:
            flor.desenhar()
        for tiro in tiros:
            tiro.desenhar()
        for tiro in tiros_inimigos:
            tiro.desenhar()
        if candy:
            candy.desenhar()

        jogador.desenhar()
        desenhar_interface(pontos, jogador.vidas, fase)
        pygame.display.flip()


def main():
    estado = "menu"
    fase = 1
    pontos_total = 0

    while True:
        if estado == "menu":
            desenhar_menu()
            esperando = True

            while esperando:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                        fase = 1
                        pontos_total = 0
                        esperando = False
                        estado = "jogo"

        elif estado == "jogo":
            resultado, pontos = iniciar_fase(fase)
            pontos_total = pontos

            if resultado == "proxima":
                fase += 1
                estado = "jogo"
            elif resultado == "gameover":
                estado = "gameover"
            elif resultado == "vitoria":
                estado = "vitoria"
            elif resultado == "menu":
                estado = "menu"

        elif estado == "gameover":
            desenhar_game_over(pontos_total)
            esperando = True

            while esperando:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            fase = 1
                            pontos_total = 0
                            estado = "jogo"
                            esperando = False
                        elif evento.key == pygame.K_ESCAPE:
                            estado = "menu"
                            esperando = False

        elif estado == "vitoria":
            desenhar_vitoria(pontos_total)
            esperando = True

            while esperando:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            fase = 1
                            pontos_total = 0
                            estado = "jogo"
                            esperando = False
                        elif evento.key == pygame.K_ESCAPE:
                            estado = "menu"
                            esperando = False


if __name__ == "__main__":
    main()
