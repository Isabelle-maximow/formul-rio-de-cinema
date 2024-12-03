import pygame
import random


#     iniciar o pygame 

pygame.init()

pygame.display.set_caption("jogo da cobrinha")
LARGURA, ALTURA = 1200, 800
tela = pygame.display.set_mode((LARGURA,ALTURA))
fundo = pygame.image.load("image1.jpg")
fundo_rect = fundo.get_rect(topleft = (736,490))  # fundo e sua posição

relogio = pygame.time.Clock()  

#  cores e sua identificações

preta = (0,0,0)
verde = (0,255,0)
branca = (255,255,255)
vermelha = (255,0,0)

tamanho_quadrado = 20    # pixel 

#  EPS do jogo 
velocidade_jogo = 10

# gerar a comida inicial - aleatorio
comida_x = round(random.randrange(1, LARGURA - tamanho_quadrado) / float(tamanho_quadrado)) * float (tamanho_quadrado)
comida_y = round(random.randrange(1, ALTURA - tamanho_quadrado) / float(tamanho_quadrado)) * float (tamanho_quadrado)

#  posição inicial da cobra (cabeça)
cobra_x = LARGURA / 2
cobra_y = ALTURA / 2

vellocidade_x = 0 
velocidade_y = 0

# comprimento da cobra - começando pela cabeça
tamanho_cobra = 1

# corpo da cobra - lista 
segmentos_cobra = []

fim_jogo = False          
while not fim_jogo:  # enqaunto não for fim_jogo
    # criando a tela do jogo - cor 


 # teclado e mouse - jogabilidade 
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            pygame.quit()
            fim_jogo = True
        elif evento.type == pygame.KEYDOWN:
            if  evento.key == pygame.K_DOWN:    # tecla p baixo
                vellocidade_x = 0
                velocidade_y = tamanho_quadrado
            elif evento.key == pygame.K_UP:         #tecla p cima
                vellocidade_x = 0
                velocidade_y = -tamanho_quadrado         # colocar o  " - " 
            elif evento.key == pygame.K_RIGHT:           
                vellocidade_x  = tamanho_quadrado
                velocidade_y = 0
            elif evento.key == pygame.K_LEFT:              # lado
                vellocidade_x  = - tamanho_quadrado    # colocar o  " - " 
                velocidade_y = 0

        tela.blit(fundo,(0, 0))   # imagem de fundo

    # atualizar posição da cobra
    cobra_x += vellocidade_x
    cobra_y += velocidade_y

    # atualizar o corpo da cobra
    segmentos_cobra.append([cobra_x, cobra_y])
    if len(segmentos_cobra) > tamanho_cobra:
        del segmentos_cobra [0] # remover 
    
    # verificar colisão com o proprio corpo
    for lista in segmentos_cobra[: - 1]:
        if lista == [cobra_x, cobra_y]:
            fim_jogo == True
    
    # verificar colisão na parede
    if cobra_x < 0 or cobra_x >= LARGURA or cobra_y < 0 or cobra_y >= ALTURA:                # 0 = borda 
        fim_jogo = True

    # desenhar a cobra
    for pixel in segmentos_cobra:
        pygame.draw.rect(tela, verde, [pixel [0], pixel [1], tamanho_quadrado, tamanho_quadrado])

    # desenhar a comida 
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho_quadrado, tamanho_quadrado]) 

    # desenhar a pontuação 
    fonte = pygame.font.SysFont("Arial",22)
    texto = fonte.render(f"Pontos: {tamanho_cobra - 1}", True, vermelha) # texto do jogo - fica na tela
    tela.blit(texto, [10,5]) # distancia da tela 

    pygame.display.update()

# verificar se a cobrinha comeu a comid e cresceu
    if cobra_x == comida_x and cobra_y == comida_y:
        tamanho_cobra += 1
        comida_x = round(random.randrange(0, LARGURA - tamanho_quadrado) / float(tamanho_quadrado)) * float (tamanho_quadrado)
        comida_y = round(random.randrange(0, ALTURA - tamanho_quadrado) / float(tamanho_quadrado)) * float (tamanho_quadrado)

    relogio.tick(velocidade_jogo)
    
pygame.quit()
