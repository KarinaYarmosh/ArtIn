import pygame, sys
from pygame.math import Vector2

class SAPER:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.pos = Vector2(self.x, self.y)

    def draw_saper(self):
        saper_rect = pygame.Rect(self.pos.x, self.pos.y, cell_size, cell_size)
        #pygame.draw.rect(screen, (126, 166, 114), saper_rect)
        pygame.draw.rect(screen, (126, 166, 114), pygame.Rect(50, 50, 50, 50), 2)
        pygame.display.flip()

pygame.init()
cell_size = 40
cell_number = 15
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

saper = SAPER()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill((0,255,255))
        saper.draw_saper()
        pygame.display.update()
        clock.tick(60)