import os
import random
import pygame
import sys
from PIL import Image


#flags=["kamien.jpg",
 #       "grass.png"]
#randofile = random.choice(flags)
#photo = randofile
#grass_count = random.randint(30, 50)
#rock_count = 91 - grass_count
field = []
for i in range(9):
    field.append(list())
    row = field[i]
    for cell in range(9):
        row.append(random.randint(0,1))
    random.shuffle(field[i])

random.shuffle(field)
print(field)

#zmienne globalne
SCREEN_HEIGHT = 540
SCREEN_WIDTH = SCREEN_HEIGHT
MAP_SIZE = 9
TILE_SIZE = int(SCREEN_HEIGHT / MAP_SIZE)
x = (SCREEN_WIDTH % 2) + (SCREEN_WIDTH / 2)
y = (SCREEN_HEIGHT % 2) + (SCREEN_HEIGHT / 2)

#funkcja zmiany rozmiaru modelu zgodnie z zapotrzebowaniem
def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size)
    resized_image.save(output_image_path)
    photo = pygame.image.load(output_image_path)
    #os.remove('resisedGrass.png')
    return photo



def grass(x,y, window):
    window.blit(resize_image("grass.png", "resisedGrass.png", (60, 60)), (x, y))
    return 0

def rock(x, y, window):
    window.blit(resize_image("kamien.jpg", "kam_resized.jpg", (60, 60)), (x, y))

#inicjalizacja kratki o rozmiarach grid_size[0] x grid_size[1]
def draw_map(grid_size, window):
    #rysowanie wierszy
    for i in range(len(field)):
        #rysowanie kolumn
        for j in range(9):
            #print(f"col= {j}, row={i}, el_i_j={field[i][j]}")
            if field[i][j] == 1:
                print(f"plant grass x={i * 60}, y={j * 60}")
                rock(i * 60, j * 60, window)
            else:
                print(f"plant rock x={i*60}, y={j*60}")
                grass(i * 60, j * 60, window)