import pygame
from sys import exit

# Inicializa o pygame
pygame.init()

# Cria a tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

##
## Importa os arquivos necessários
##

# Carrega o plano de fundo
plano_fundo = pygame.image.load('assets/fundo/Night-Background8.png').convert()
fundo_estrelas = pygame.image.load('assets/fundo/Night-Background7.png').convert_alpha()
fundo_estrelas_2 = pygame.image.load('assets/fundo/Night-Background6.png').convert_alpha()
fundo_estrelas_3 = pygame.image.load('assets/fundo/Night-Background5.png').convert_alpha()
fundo_rochas = pygame.image.load('assets/fundo/Night-Background4.png').convert_alpha()
fundo_chao = pygame.image.load('assets/fundo/Night-Background3.png').convert_alpha()
fundo_lua = pygame.image.load('assets/fundo/Night-Background2.png').convert_alpha()
fundo_rochas_voadoras = pygame.image.load('assets/fundo/Night-Background1.png').convert_alpha()

# Transforma o tamanho da imagem de fundo
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
fundo_estrelas = pygame.transform.scale(fundo_estrelas, tamanho)
fundo_estrelas_2 = pygame.transform.scale(fundo_estrelas_2, tamanho)
fundo_estrelas_3 = pygame.transform.scale(fundo_estrelas_3, tamanho)
fundo_rochas = pygame.transform.scale(fundo_rochas, tamanho)
fundo_chao = pygame.transform.scale(fundo_chao, tamanho)
fundo_lua = pygame.transform.scale(fundo_lua, tamanho)
fundo_rochas_voadoras = pygame.transform.scale(fundo_rochas_voadoras, tamanho)

# Importa o personagem
jogador_parado_surf = pygame.image.load('assets/jogador/parado/Hero Boy Idle1.png').convert_alpha()
jogador_parado_rect = jogador_parado_surf.get_rect( midbottom = (100, 530))

# Define o Titulo da Janela
pygame.display.set_caption("ChuvaMortal")

# Cria um relógio para controlar os FPS
relogio = pygame.time.Clock()

movimento_personagem = 0
# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 5

            if evento.key == pygame.K_LEFT:
                movimento_personagem = -5

    # Desenha o fundo na tela
    tela.blit(plano_fundo, (0, 0))
    tela.blit(fundo_estrelas, (0, 0))
    tela.blit(fundo_estrelas_2, (0, 0))
    tela.blit(fundo_estrelas_3, (0, 0))
    tela.blit(fundo_rochas, (0, 0))
    tela.blit(fundo_chao, (0, 0))
    tela.blit(fundo_lua, (0, 0))
    tela.blit(fundo_rochas_voadoras, (0, 0))
    
    # Desenha o jogador na tela
    jogador_parado_rect.x += movimento_personagem
    tela.blit(jogador_parado_surf, jogador_parado_rect)

    # Atualiza a tela com o conteudo
    pygame.display.update()

    # Define a quantidade de frames por segundo
    relogio.tick(60)