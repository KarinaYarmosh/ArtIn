import copy
import os
from _queue import SimpleQueue

import pygame
import random

from gameObjects.Saper import Sapper
from gameObjects.kratka import Grid
from gameTools.tools import resize_image


def find_path(matrix, end):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            elif matrix[i][j] == 2:
                matrix[i][j] = -1
    matrix[0][0] = 1
    start = [0, 0]
    x_end = end[0]
    y_end = end[1]
    limit = list(range(9))
    # for row in matrix:
    #     print(' '.join([str(elem) for elem in row]))
    frontier = SimpleQueue()
    frontier.put(start)
    while not frontier.empty() and matrix[x_end][y_end] == 0:
        current = frontier.get()
        x = current[0]
        y = current[1]
        if (x + 1 in limit) and matrix[x + 1][y] == 0:
            matrix[x + 1][y] = matrix[x][y] + 1
            frontier.put([x + 1, y])
        if (y + 1 in limit) and matrix[x][y + 1] == 0:
            matrix[x][y + 1] = matrix[x][y] + 1
            frontier.put([x, y + 1])
        if (x - 1 in limit) and matrix[x - 1][y] == 0:
            matrix[x - 1][y] = matrix[x][y] + 1
            frontier.put([x - 1, y])
        if (y - 1 in limit) and matrix[x][y - 1] == 0:
            matrix[x][y - 1] = matrix[x][y] + 1
            frontier.put([x, y - 1])
    # print('\n')
    # for row in matrix:
    #     print(' '.join([str(elem) for elem in row]))
    counter = matrix[x_end][y_end]
    x = x_end
    y = y_end
    moves = []
    while counter != 1:
        if matrix[x][y] - matrix[x + 1][y] == 1:
            moves.append(1)
            counter -= 1
            x = x + 1
            continue
        if matrix[x][y] - matrix[x][y + 1] == 1:
            moves.append(4)
            counter -= 1
            y = y + 1
            continue
        if matrix[x][y] - matrix[x - 1][y] == 1:
            moves.append(3)
            counter -= 1
            x = x - 1
            continue
        if matrix[x][y] - matrix[x][y - 1] == 1:
            moves.append(2)
            counter -= 1
            y = y - 1
            continue
    moves.reverse()
    return moves

# That's how you can use this function
# 1 - up, 2 - right, 3 - down, 4 - left
# matrixx = copy.deepcopy(self.grid.grid_matrix)
# moves = find_path(matrixx, [3, 3])
# print(moves)


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
            pygame.time.delay(300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            # obsługa zdarzeń
            keys = pygame.key.get_pressed()
            self.saper.saper = self.saper.saper_stay

            if (self.saper.x_pos == 0) and (self.saper.y_pos == 0):
                self.saper.backpack.clear()
                self.saper.backpack_load = 0

            #print(f"pozycja gracza: x - {self.saper.x_pos}, y - {self.saper.y_pos}")

            if keys[pygame.K_LEFT] and self.saper.x_pos - self.saper.step > -60 and self.grid.grid_matrix[(self.saper.x_pos - self.saper.step)//60][self.saper.y_pos//60] != 2:
                self.saper.move_left()

            if keys[pygame.K_RIGHT] and self.saper.x_pos + self.saper.step < self.win.get_width() and self.grid.grid_matrix[(self.saper.x_pos + self.saper.step)//60][self.saper.y_pos//60] != 2:
                self.saper.move_right()

            if keys[pygame.K_UP] and self.saper.y_pos - self.saper.step > -60 and self.grid.grid_matrix[self.saper.x_pos//60][(self.saper.y_pos - self.saper.step)//60] != 2:
                self.saper.move_up()

            if keys[pygame.K_DOWN] and self.saper.y_pos + self.saper.step < self.win.get_height() and self.grid.grid_matrix[self.saper.x_pos//60][(self.saper.y_pos + self.saper.step)//60] != 2:
                self.saper.move_down()

            if not self.grid.mines and not self.grid.granats and not self.saper.backpack:
                print("You win!")
                self.grid.create_object((0,0), "win.jpg", (540, 540))
                #self.run = False

            self.win.blit(self.saper.saper, self.saper.saper_rect)

            # odświeżenie ekranu
            pygame.display.update()



