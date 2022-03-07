import pygame
from kratka import draw_map
from kratka import grass

pygame.init()
win = pygame.display.set_mode((540, 540))
pygame.display.set_caption("Saper")
TILE_SIZE = 60

x = 0
y = 0
step = 60
run = True
clock = pygame.time.Clock()
draw_map((9, 9), win)

while run:
    pygame.time.delay(60)
    # opóźnienie w gorze

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # obsługa zdarzeń
    keys = pygame.key.get_pressed()
    # warunki do zmiany pozycji obiektu
    clock.tick(75)
    # Keep player on the screen
    saper_surf = saper_down = saper_up = pygame.image.load('saper.png')
    saper_left=pygame.image.load('saper_left.png')
    saper_right=pygame.image.load('saper_right.png')

    saper=saper_surf

    if keys[pygame.K_LEFT]:
        saper=saper_left
        check = x
        check -= step
        if check <= -60:
            pass
        else:
            grass(x, y, win)
            grass(x-60, y, win)
            grass(x+60, y, win)
            grass(x, y-60, win)
            grass(x, y+60, win)
            x -= step
    if keys[pygame.K_RIGHT]:
        saper=saper_right
        check=x
        check += step
        if check >= 540:
            pass
        else:
            grass(x - 60, y, win)
            grass(x + 60, y, win)
            grass(x, y - 60, win)
            grass(x, y + 60, win)
            grass(x, y, win)
            x += step
    if keys[pygame.K_UP]:
        saper=saper_up
        check = y
        check -= step
        if check <= -60:
            pass
        else:
            grass(x - 60, y, win)
            grass(x + 60, y, win)
            grass(x, y - 60, win)
            grass(x, y + 60, win)
            grass(x, y, win)
            y -= step
    if keys[pygame.K_DOWN]:
        saper=saper_down
        check = y
        check += step
        if check >= 540:
            pass
        else:
            grass(x - 60, y, win)
            grass(x + 60, y, win)
            grass(x, y - 60, win)
            grass(x, y + 60, win)
            grass(x, y, win)
            y += step
    # "czyszczenie" ekranu
    #draw_map((9,9), win)
    #win.fill((0, 0, 0))
    saper_rect=saper.get_rect(
        center=(x + 25, y + 25)
    )
    win.blit(saper,saper_rect)

    # odświeżenie ekranu
    pygame.display.update()