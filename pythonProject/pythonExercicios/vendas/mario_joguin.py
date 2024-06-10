import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela do jogo
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Super Mario")

# Cores
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)

# Posição inicial do Mario
mario_x = 50
mario_y = window_height - 100
mario_width = 50
mario_height = 50
mario_speed = 5
mario_jump = False
mario_jump_count = 10

# Posição inicial das plataformas
platforms = [
    (0, window_height - 50, window_width, 50),
    (window_width // 2 - 50, window_height - 150, 100, 20)
]

# Loop principal do jogo
clock = pygame.time.Clock()
running = True
while running:
    window.fill(white)

    # Eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimentação do Mario
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and mario_x > mario_speed:
        mario_x -= mario_speed
    if keys[pygame.K_RIGHT] and mario_x < window_width - mario_width - mario_speed:
        mario_x += mario_speed
    if not mario_jump:
        if keys[pygame.K_SPACE]:
            mario_jump = True
    else:
        if mario_jump_count >= -10:
            neg = 1
            if mario_jump_count < 0:
                neg = -1
            mario_y -= (mario_jump_count ** 2) * 0.5 * neg
            mario_jump_count -= 1
        else:
            mario_jump = False
            mario_jump_count = 10

    # Desenha o Mario
    pygame.draw.rect(window, blue, (mario_x, mario_y, mario_width, mario_height))

    # Desenha as plataformas
    for platform in platforms:
        pygame.draw.rect(window, green, platform)

        # Lógica de colisão do Mario com as plataformas
        if mario_y + mario_height >= platform[1] and mario_y + mario_height <= platform[1] + 10:
            if mario_x + mario_width >= platform[0] and mario_x <= platform[0] + platform[2]:
                mario_jump = False
                mario_jump_count = 10
                mario_y = platform[1] - mario_height

    # Atualiza a tela
    pygame.display.update()

    # Limita a taxa de quadros por segundo
    clock.tick(60)

# Encerra o Pygame
pygame.quit()
sys.exit()
