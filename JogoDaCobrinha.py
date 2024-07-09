import pygame
import time
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
cor_cobra = (0, 255, 0)  # Verde
cor_comida = (255, 0, 0)  # Vermelho
cor_fundo = (0, 0, 0)  # Preto

# Tamanho da tela e outros parâmetros
largura = 600
altura = 400
tamanho_cobra = 20
velocidade = 15

# Fonte para o placar
fonte = pygame.font.SysFont(None, 30)

# Função para desenhar a cobra
def desenhar_cobra(tamanho_cobra, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, cor_cobra, [x[0], x[1], tamanho_cobra, tamanho_cobra])

# Função para mostrar mensagem na tela
def mensagem(msg, cor):
    tela_texto = fonte.render(msg, True, cor)
    tela.blit(tela_texto, [largura / 6, altura / 3])

# Configuração da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Loop principal do jogo
def jogo():
    game_over = False
    game_close = False

    # Posição inicial da cobra
    x_cobra = largura / 2
    y_cobra = altura / 2

    # Movimento inicial da cobra
    dx = 0
    dy = 0

    # Lista que contém todas as partes da cobra
    lista_cobra = []
    comprimento_cobra = 1

    # Posição inicial da comida
    posicao_comida = [random.randrange(1, largura // tamanho_cobra) * tamanho_cobra,
                      random.randrange(1, altura // tamanho_cobra) * tamanho_cobra]

    while not game_over:

        while game_close == True:
            tela.fill(cor_fundo)
            mensagem("Você perdeu! Pressione Q-Sair ou C-Recomeçar", cor_cobra)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -tamanho_cobra
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = tamanho_cobra
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -tamanho_cobra
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = tamanho_cobra

        # Verifica se a cobra sai da tela
        if x_cobra >= largura or x_cobra < 0 or y_cobra >= altura or y_cobra < 0:
            game_close = True
        x_cobra += dx
        y_cobra += dy

        tela.fill(cor_fundo)
        pygame.draw.rect(tela, cor_comida, [posicao_comida[0], posicao_comida[1], tamanho_cobra, tamanho_cobra])
        cabeça_cobra = []
        cabeça_cobra.append(x_cobra)
        cabeça_cobra.append(y_cobra)
        lista_cobra.append(cabeça_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for segmento in lista_cobra[:-1]:
            if segmento == cabeça_cobra:
                game_close = True

        desenhar_cobra(tamanho_cobra, lista_cobra)

        pygame.display.update()

        if x_cobra == posicao_comida[0] and y_cobra == posicao_comida[1]:
            posicao_comida = [random.randrange(1, largura // tamanho_cobra) * tamanho_cobra,
                              random.randrange(1, altura // tamanho_cobra) * tamanho_cobra]
            comprimento_cobra += 1

        pygame.time.Clock().tick(velocidade)

    pygame.quit()
    quit()

jogo()
