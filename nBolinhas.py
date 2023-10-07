
import pygame

pygame.init()

tamanho = (1000, 400)

tela = pygame.display.set_mode(tamanho)

relogio = pygame.time.Clock()

# Importaçao das imagens
projetil1 = pygame.image.load("assets/objetos/projetil/Hero Bullet1.png").convert_alpha()
projetil1_rect = projetil1_superficie.get_rect(center=(300, 200))

projetil2 = pygame.image.load("assets/objetos/projetil/Hero Bullet1.png").convert_alpha()
projetil2_rect = projetil2_superficie.get_rect(center=(600, 200))



while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    projetil1_rect.y += 1
    projetil1_rect.x += 5

    if projetil1_rect.x > 1000: projetil1_rect.x = -5
    if projetil1_rect.y > 400: projetil1_rect.x = 1

    tela.fill('#ffffff')
    tela.blit(projetil1_superficie, projetil1_rect)
    tela.blit(projetil2_superficie, projetil2_rect)

    if projetil1_rect.colliderect(projetil2_rect):
        print(f"House uma colisao: ", colisoes)
        colisoes += 1
        projetil2_rect.y += 5

    pygame.display.update()
    relogio.tick(60)