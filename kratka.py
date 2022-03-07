import os

import pygame
import sys
from PIL import Image

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
    grass_img = pygame.image.load('resisedGrass.png')
    #os.remove('resisedGrass.png')
    return grass_img



def grass(x,y, window):
    window.blit(resize_image("grass.png", "resisedGrass.png", (60, 60)), (x,y))
    return 0

#inicjalizacja kratki o rozmiarach grid_size[0] x grid_size[1]
def draw_map(grid_size, window):
    #rysowanie wierszy
    for row in range(grid_size[0]):
        #rysowanie kolumn
        for col in range(grid_size[1]):
            grass(col * 60, row * 60, window)


