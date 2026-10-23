import pygame
import math

# Inicializa o Pygame
pygame.init()

# Define o tamanho da tela
screen_width = 1080
screen_height = 2160
screen = pygame.display.set_mode((screen_width, screen_height))

# Define as cores da bandeira
green = (0, 128, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# Desenha o fundo da bandeira como verde
screen.fill(green)

# Desenha o escudo da bandeira no centro da tela
shield_size = 540
shield_x = screen_width // 2 - shield_size // 2
shield_y = screen_height // 2 - shield_size // 2
pygame.draw.ellipse(screen, yellow, (shield_x, shield_y, shield_size, shield_size))
pygame.draw.polygon(screen, blue, [(shield_x + shield_size / 2, shield_y),
                                   (shield_x + shield_size, shield_y + shield_size / 2),
                                   (shield_x + shield_size / 2, shield_y + shield_size),
                                   (shield_x, shield_y + shield_size / 2)])

# Desenha as estrelas brancas ao redor do escudo
star_size = 20

star_x = screen_width // 2 - star_size // 2
star_y = screen_height // 2 - star_size // 2
pygame.draw.polygon(screen, white, [(star_x, star_y + star_size // 3),
                                   (star_x + star_size // 2, star_y + star_size // 3),
                                   (star_x + star_size // 4, star_y),
                                   (star_x + star_size // 2, star_y - star_size // 3),
                                   (star_x, star_y - star_size // 3),
                                   (star_x - star_size // 2, star_y)])

star_x = screen_width // 2 - star_size // 2
star_y = screen_height // 2 + star_size // 2
pygame.draw.polygon(screen, white, [(star_x, star_y + star_size // 3),
                                   (star_x + star_size // 2, star_y + star_size // 3),
                                   (star_x + star_size // 4, star_y),
                                   (star_x + star_size // 2, star_y - star_size // 3),
                                   (star_x, star_y - star_size // 3),
                                   (star_x - star_size // 2, star_y)])


# Atualiza a tela para mostrar o desenho
pygame.display.flip()

# Finaliza o Pygame
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break

pygame.quit()
