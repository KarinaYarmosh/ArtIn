import pygame
from sztuczna_inteligencja.gameObjects.kratka import Grid

pygame.init()

win = pygame.display.set_mode((540, 540))
pygame.display.set_caption("Saper")
TILE_SIZE = 60
x = 0
y = 0
step = 60
run = True
clock = pygame.time.Clock()
grid = Grid((10, 10), win)

while run:
    pygame.time.delay(60)
    # opóźnienie w grze

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # obsługa zdarzeń
    keys = pygame.key.get_pressed()
    # warunki do zmiany pozycji obiektu
    #clock.tick(75)
    # Trzymanie gracza na ekranie
    saper_surf = saper_down = saper_up = pygame.image.load('sprites/saper.png')
    saper_left=pygame.image.load('sprites/saper_left.png')
    saper_right=pygame.image.load('sprites/saper_right.png')

    saper=saper_surf
    print(x,y)
    if keys [pygame.K_LEFT] and x-step > -60:
        saper=saper_left
        #odswieżanie komórek
        grid.create_object((x, y), grid.objects.get(grid.grid_matrix[x // 60][y // 60]), (60, 60))
        grid.create_object((x, y - 60), grid.objects.get(grid.grid_matrix[x // 60][(y - 60) // 60]), (60, 60))
        # zmienić pozycję gracza
        x -= step
    if keys[pygame.K_RIGHT] and x+step < 540:
        saper = saper_right

        #odswieżanie komórek
        grid.create_object((x, y), grid.objects.get(grid.grid_matrix[x // 60][y // 60]), (60, 60))
        grid.create_object((x, y - 60), grid.objects.get(grid.grid_matrix[x // 60][(y - 60) // 60]), (60, 60))
        # zmienić pozycję gracza
        x += step
    if keys[pygame.K_UP] and y-step>-60:
        saper=saper_up

        #odswieżanie komórek
        grid.create_object((x, y), grid.objects.get(grid.grid_matrix[x // 60][y // 60]), (60, 60))
        grid.create_object((x, y - 60), grid.objects.get(grid.grid_matrix[x // 60][(y - 60) // 60]), (60, 60))
        # zmienić pozycję gracza
        y -= step
    if keys[pygame.K_DOWN] and y+step<540:
        saper=saper_down

        #odswieżanie komórek

        grid.create_object((x, y), grid.objects.get(grid.grid_matrix[x//60][y//60]), (60, 60))
        grid.create_object((x, y - 60), grid.objects.get(grid.grid_matrix[x//60][(y-60)//60]), (60, 60))

        #zmienić pozycję gracza
        y += step
    saper_rect=saper.get_rect(
        center=(x + 25, y + 25)
    )
    win.blit(saper,saper_rect)

    # odświeżenie ekranu
    pygame.display.update()