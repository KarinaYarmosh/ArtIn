import copy
import os

import pygame
import random

from gameObjects.Saper import Sapper
from gameObjects.kratka import Grid
from gameTools.tools import resize_image


class Game():
    def __init__(self, grid_size):
        pygame.init()
        self.win = pygame.display.set_mode((grid_size[0] * 60, grid_size[1] * 60))
        pygame.display.set_caption("Saper")
        self.run = True
        self.has_path = False
        self.clock = pygame.time.Clock()
        self.grid = Grid(grid_size, self.win)
        self.saper = Sapper(self.grid)

    def start_game(self):
        while self.run:
            # opóźnienie w grze
            pygame.time.delay(400)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            # obsługa zdarzeń
            keys = pygame.key.get_pressed()
            self.saper.saper = self.saper.saper_stay

            # Sapper moves according to the BFS-algorithm
            if not self.has_path and not self.saper.path:
                self.saper.find_path(copy.deepcopy(self.grid.grid_matrix), [12, 12])
                print(self.saper.path)
                self.has_path = True
            if self.saper.path:
                direction = self.saper.path.pop(0)
                if direction == 1:
                    self.saper.move_left()
                if direction == 2:
                    self.saper.move_down()
                if direction == 3:
                    self.saper.move_right()
                if direction == 4:
                    self.saper.move_up()

            if (self.saper.x_pos == 0) and (self.saper.y_pos == 0):
                self.saper.backpack.clear()
                self.saper.backpack_load = 0

            # print(f"pozycja gracza: x - {self.saper.x_pos}, y - {self.saper.y_pos}")

            if keys[pygame.K_LEFT] and self.saper.x_pos - self.saper.step > -60 and \
                    self.grid.grid_matrix[(self.saper.x_pos - self.saper.step) // 60][self.saper.y_pos // 60] != 2:
                self.saper.move_left()

            if keys[pygame.K_RIGHT] and self.saper.x_pos + self.saper.step < self.win.get_width() and \
                    self.grid.grid_matrix[(self.saper.x_pos + self.saper.step) // 60][self.saper.y_pos // 60] != 2:
                self.saper.move_right()

            if keys[pygame.K_UP] and self.saper.y_pos - self.saper.step > -60 and \
                    self.grid.grid_matrix[self.saper.x_pos // 60][(self.saper.y_pos - self.saper.step) // 60] != 2:
                self.saper.move_up()

            if keys[pygame.K_DOWN] and self.saper.y_pos + self.saper.step < self.win.get_height() and \
                    self.grid.grid_matrix[self.saper.x_pos // 60][(self.saper.y_pos + self.saper.step) // 60] != 2:
                self.saper.move_down()

            if not self.grid.mines and not self.grid.granats and not self.saper.backpack:
                print("You win!")
                self.grid.create_object((0, 0), "win.jpg", (540, 540))
                # self.run = False

            self.win.blit(self.saper.saper, self.saper.saper_rect)

            # odświeżenie ekranu
            pygame.display.update()
