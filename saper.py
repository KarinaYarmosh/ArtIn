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

    if keys[pygame.K_LEFT]:
        check = x
        check -= step
        if check <= -60:
            pass
        else:
            x -= step
    if keys[pygame.K_RIGHT]:
        check=x
        check += step
        if check >= 540:
            pass
        else:
            x += step
    if keys[pygame.K_UP]:
        check = y
        check -= step
        if check <= -60:
            pass
        else:
            y -= step
    if keys[pygame.K_DOWN] :
        check = y
        check += step
        if check >= 540:
            pass
        else:
            y += step
    # "czyszczenie" ekranu
    win.fill((0, 0, 0))
    # rysowanie prostokąta
    dog_surf = pygame.image.load('saper.png')
    dog_rect = dog_surf.get_rect(
        center=(x+25,y+25))
    win.blit(dog_surf, dog_rect)
    # pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    # odświeżenie ekranu
    pygame.display.update()