import pygame
import random

from sztuczna_inteligencja.gameObjects.Saper import Sapper
from sztuczna_inteligencja.gameObjects.kratka import Grid

class Game():
    def __init__(self, grid_size):
        pygame.init()
        self.win = pygame.display.set_mode((grid_size[0]*60, grid_size[1]*60))
        pygame.display.set_caption("Saper")
        self.run = True
        self.clock = pygame.time.Clock()
        self.grid = Grid(grid_size, self.win)
        self.saper = Sapper(self.grid)

    def start_game(self):
        while self.run:
            # opóźnienie w grze
            pygame.time.delay(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            # obsługa zdarzeń
            keys = pygame.key.get_pressed()
            # warunki do zmiany pozycji obiektu
            # Trzymanie gracza na ekranie

            # print(x,y)

            self.saper.saper = self.saper.saper_stay

            if keys[pygame.K_LEFT] and self.saper.x_pos - self.saper.step > -60:
                self.saper.move_left()

            if keys[pygame.K_RIGHT] and self.saper.x_pos + self.saper.step < self.win.get_width():
                self.saper.move_right()

            if keys[pygame.K_UP] and self.saper.y_pos - self.saper.step > -60:
                self.saper.move_up()

            if keys[pygame.K_DOWN] and self.saper.y_pos + self.saper.step < self.win.get_height():
                self.saper.move_down()


            self.win.blit(self.saper.saper, self.saper.saper_rect)

            # if saper == mines:

            # odświeżenie ekranu
            pygame.display.update()



