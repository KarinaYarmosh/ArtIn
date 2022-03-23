import pygame
import random
from sztuczna_inteligencja.gameObjects.kratka import Grid

pygame.init()

win = pygame.display.set_mode((540, 540))
pygame.display.set_caption("Saper")
TILE_SIZE = 60
x = 0
y = 0
step = 60
MINES_NUM = 8
GRANATS_NUM = 8
run = True
gran = True
clock = pygame.time.Clock()
grid = Grid((9, 9), win)
granats = []
mines = []
#bombs

i=0

while i != MINES_NUM:
    s = int(random.randrange(0, 540, 60))
    d = int(random.randrange(0, 540, 60))
    mine = [s, d]
    if (mine not in mines) and (mine != [0, 0]):
        mines.append(mine)
        i+=1

print(mines)

i=0

while i != GRANATS_NUM:
    l = int(random.randrange(0, 540, 60))
    m = int(random.randrange(0, 540, 60))
    granat = [l, m]
    if (granat not in mines) and (granat not in granats) and (granat != [0, 0]):
        granats.append(granat)
        i+=1

print(granats)
print(mines == granats)

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
    #print(x,y)
    if keys [pygame.K_LEFT] and x-step > -60:
        saper=saper_left
        #odswieżanie komórek
        grid.create_object((x, y), grid.objects.get(grid.grid_matrix[x // 60][y // 60]), (60, 60))
        grid.create_object((x, y - 60), grid.objects.get(grid.grid_matrix[x // 60][(y - 60) // 60]), (60, 60))
        # zmienić pozycję gracza
        x -= step

        print(x,y)
        yes_or_nor = [x, y]
        if yes_or_nor in mines:
            print("MINA")
        if yes_or_nor in granats:
            print("GRANAT")

    if keys[pygame.K_RIGHT] and x+step < 540:
        saper = saper_right

        #odswieżanie komórek
        grid.create_object((x, y), grid.objects.get(grid.grid_matrix[x // 60][y // 60]), (60, 60))
        grid.create_object((x, y - 60), grid.objects.get(grid.grid_matrix[x // 60][(y - 60) // 60]), (60, 60))
        # zmienić pozycję gracza
        x += step

        print(x,y)
        yes_or_nor = [x, y]
        if yes_or_nor in mines:
            print("MINA")
        if yes_or_nor in granats:
            print("GRANAT")

    if keys[pygame.K_UP] and y-step>-60:
        saper=saper_up

        #odswieżanie komórek
        grid.create_object((x, y), grid.objects.get(grid.grid_matrix[x // 60][y // 60]), (60, 60))
        grid.create_object((x, y - 60), grid.objects.get(grid.grid_matrix[x // 60][(y - 60) // 60]), (60, 60))
        # zmienić pozycję gracza
        y -= step

        print(x,y)
        yes_or_nor = [x, y]
        if yes_or_nor in mines:
            print("MINA")
        if yes_or_nor in granats:
            print("GRANAT")

    if keys[pygame.K_DOWN] and y+step<540:
        saper=saper_down

        #odswieżanie komórek

        grid.create_object((x, y), grid.objects.get(grid.grid_matrix[x//60][y//60]), (60, 60))
        grid.create_object((x, y - 60), grid.objects.get(grid.grid_matrix[x//60][(y-60)//60]), (60, 60))

        #zmienić pozycję gracza
        y += step

        print(x,y)
        yes_or_nor = [x, y]
        if yes_or_nor in mines:
            print("MINA")
        if yes_or_nor in granats:
            print("GRANAT")

    saper_rect=saper.get_rect(
        center=(x + 25, y + 25)
    )
    win.blit(saper, saper_rect)

    #if saper == mines:

    # odświeżenie ekranu
    pygame.display.update()