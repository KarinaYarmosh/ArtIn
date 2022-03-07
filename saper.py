import pygame

pygame.init()
win = pygame.display.set_mode((540, 540))
pygame.display.set_caption("Saper")
x = 0
y = 0
width = 60
height = 60
step = 60
run = True
clock = pygame.time.Clock()
while run:
    # opóźnienie w gorze
    pygame.time.delay(85)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # obsługa zdarzeń
    keys = pygame.key.get_pressed()
    # warunki do zmiany pozycji obiektu
    clock.tick(100)
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
            x -= step
    if keys[pygame.K_RIGHT]:
        saper=saper_right
        check=x
        check += step
        if check >= 540:
            pass
        else:
            x += step
    if keys[pygame.K_UP]:
        saper=saper_up
        check = y
        check -= step
        if check <= -60:
            pass
        else:
            y -= step
    if keys[pygame.K_DOWN]:
        saper=saper_down
        check = y
        check += step
        if check >= 540:
            pass
        else:
            y += step
    # "czyszczenie" ekranu
    win.fill((0, 0, 0))

    saper_rect=saper.get_rect(
        center=(x + 25, y + 25)
    )
    win.blit(saper,saper_rect)

    # odświeżenie ekranu
    pygame.display.update()