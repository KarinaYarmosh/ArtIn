import threading

import pygame

from sztuczna_inteligencja.gameObjects.Saper import Sapper
from sztuczna_inteligencja.gameObjects.elementy import Duzykamien
from sztuczna_inteligencja.gameObjects.kratka import Grid
from sztuczna_inteligencja.connectAItoGame import connectAItoGame

class Game():
    def __init__(self, grid_size):
        pygame.init()
        self.win = pygame.display.set_mode((grid_size[0]*60, grid_size[1]*60))
        pygame.display.set_caption("Saper")
        self.run = True
        self.clock = pygame.time.Clock()
        self.grid = Grid(grid_size, self.win)
        self.saper = Sapper(self.grid)
        self.find_path = False
        self.path = []

    def start_game(self):
        while self.run:
            # opóźnienie w grze
            pygame.time.delay(500)

            if not self.find_path:
                connect = connectAItoGame(self.grid.grid_matrix)
                self.path = connect.get_AStar_path()
                # self.path = connect.get_BFS_path()
                self.find_path = True
                print(self.path)

            if self.path:
                step = self.path.pop(0)
                direction = self.saper.direction
                if step == 'L':
                    match direction:
                        case 'D':
                            self.saper.direction = 'R'
                        case 'R':
                            self.saper.direction = 'U'
                        case 'U':
                            self.saper.direction = 'L'
                        case 'L':
                            self.saper.direction = 'D'
                if step == 'R':
                    match direction:
                        case 'D':
                            self.saper.direction = 'L'
                        case 'L':
                            self.saper.direction = 'U'
                        case 'U':
                            self.saper.direction = 'R'
                        case 'R':
                            self.saper.direction = 'D'
                if step == 'M':
                    match direction:
                        case 'D':
                            self.saper.move_down()
                        case 'L':
                            self.saper.move_left()
                        case 'U':
                            self.saper.move_up()
                        case 'R':
                            self.saper.move_right()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            # obsługa zdarzeń
            keys = pygame.key.get_pressed()

            match self.saper.direction:
                case 'D':
                    self.saper.saper = self.saper.saper_ddown
                case 'R':
                    self.saper.saper = self.saper.saper_rright
                case 'L':
                    self.saper.saper = self.saper.saper_lleft
                case 'U':
                    self.saper.saper = self.saper.saper_uup

            if (self.saper.x_pos == 0) and (self.saper.y_pos == 0):
                self.saper.backpack.clear()
                self.saper.backpack_load = 0

            #print(f"pozycja gracza: x - {self.saper.x_pos}, y - {self.saper.y_pos}")

            if keys[pygame.K_LEFT] and self.saper.x_pos - self.saper.step > -60 \
                    and self.grid.grid_matrix[(self.saper.x_pos - self.saper.step)//60][self.saper.y_pos//60] != Duzykamien().koszt:
                self.saper.move_left()

            if keys[pygame.K_RIGHT] and self.saper.x_pos + self.saper.step < self.win.get_width() \
                    and self.grid.grid_matrix[(self.saper.x_pos + self.saper.step)//60][self.saper.y_pos//60] != Duzykamien().koszt:
                self.saper.move_right()

            if keys[pygame.K_UP] and self.saper.y_pos - self.saper.step > -60 \
                    and self.grid.grid_matrix[self.saper.x_pos//60][(self.saper.y_pos - self.saper.step)//60] != Duzykamien().koszt:
                self.saper.move_up()

            if keys[pygame.K_DOWN] and self.saper.y_pos + self.saper.step < self.win.get_height() \
                    and self.grid.grid_matrix[self.saper.x_pos//60][(self.saper.y_pos + self.saper.step)//60] != Duzykamien().koszt:
                self.saper.move_down()

            if not self.grid.mines and not self.grid.granats and not self.saper.backpack:
                print("You win!")
                self.grid.create_object((0,0), "win.jpg", (540, 540))
                #self.run = False

            self.win.blit(self.saper.saper, self.saper.saper_rect)

            # odświeżenie ekranu
            pygame.display.update()
