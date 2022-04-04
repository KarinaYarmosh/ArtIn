from queue import SimpleQueue

import pygame


class Sapper:

    def __init__(self, grid):
        self.saper_stay = pygame.image.load('sprites/saper.png')
        self.saper_down = pygame.image.load('sprites/saper.png')
        self.saper_up = pygame.image.load('sprites/saper.png')
        self.saper_left = pygame.image.load('sprites/saper_left.png')
        self.saper_right = pygame.image.load('sprites/saper_right.png')
        self.saper = pygame.image.load('sprites/saper.png')
        self.grid = grid
        self.x_pos = 0
        self.y_pos = 0
        self.step = 60
        self.saper_rect = self.saper.get_rect(
            center=(self.x_pos + 25, self.y_pos + 25)
        )
        self.backpack = []
        self.backpack_load = 0
        self.path = []

    def mines_do(self, pos):
        # print(len(self.backpack))
        print(f"Backpack: {self.backpack}")
        if pos in self.grid.mines.keys():
            if self.backpack_load + self.grid.mines[pos].weight <= 3:
                self.backpack.append("mina")
                self.backpack_load += self.grid.mines[pos].weight
                # print(self.grid.mines[pos].old_or_not)
                self.grid.mines.pop(pos)
            else:
                print("nie mogę więcej unieść, bo to jest mina, składż bomby w miescu dla bomb (pozycja 0, 0)")

        if pos in self.grid.granats.keys():
            if self.backpack_load + self.grid.granats[pos].weight <= 3:

                self.backpack.append("granat")
                self.backpack_load += self.grid.granats[pos].weight
                self.grid.granats.pop(pos)
            else:
                print("nie mogę więcej unieść, bo to jest granat, składż bomby w miescu dla bomb (pozycja 0, 0)")

    def move_left(self):
        self.saper = self.saper_left
        # odswieżanie komórek
        self.grid.create_object((self.x_pos, self.y_pos),
                                self.grid.objects.get(self.grid.grid_matrix[self.x_pos // 60][self.y_pos // 60]),
                                (60, 60))
        self.grid.create_object((self.x_pos, self.y_pos - 60),
                                self.grid.objects.get(self.grid.grid_matrix[self.x_pos // 60][(self.y_pos - 60) // 60]),
                                (60, 60))
        # zmienić pozycję gracza
        self.x_pos -= self.step

        # print("self.x_pos, self.y_pos")
        yes_or_not = (self.x_pos, self.y_pos)

        self.mines_do(yes_or_not)

        self.saper_rect = self.saper.get_rect(
            center=(self.x_pos + 25, self.y_pos + 25)
        )

    def move_right(self):
        self.saper = self.saper_right
        # odswieżanie komórek
        self.grid.create_object((self.x_pos, self.y_pos),
                                self.grid.objects.get(self.grid.grid_matrix[self.x_pos // 60][self.y_pos // 60]),
                                (60, 60))
        self.grid.create_object((self.x_pos, self.y_pos - 60),
                                self.grid.objects.get(self.grid.grid_matrix[self.x_pos // 60][(self.y_pos - 60) // 60]),
                                (60, 60))
        # zmienić pozycję gracza
        self.x_pos += self.step

        # print(self.x_pos, self.y_pos)
        yes_or_nor = (self.x_pos, self.y_pos)

        self.mines_do(yes_or_nor)

        self.saper_rect = self.saper.get_rect(
            center=(self.x_pos + 25, self.y_pos + 25)
        )

    def move_up(self):
        self.saper = self.saper_up
        # odswieżanie komórek
        self.grid.create_object((self.x_pos, self.y_pos),
                                self.grid.objects.get(self.grid.grid_matrix[self.x_pos // 60][self.y_pos // 60]),
                                (60, 60))
        self.grid.create_object((self.x_pos, self.y_pos - 60),
                                self.grid.objects.get(self.grid.grid_matrix[self.x_pos // 60][(self.y_pos - 60) // 60]),
                                (60, 60))
        # zmienić pozycję gracza
        self.y_pos -= self.step

        # print(self.x_pos, self.y_pos)
        yes_or_nor = (self.x_pos, self.y_pos)

        self.mines_do(yes_or_nor)

        self.saper_rect = self.saper.get_rect(
            center=(self.x_pos + 25, self.y_pos + 25)
        )

    def move_down(self):
        self.saper = self.saper_down
        # odswieżanie komórek
        self.grid.create_object((self.x_pos, self.y_pos),
                                self.grid.objects.get(self.grid.grid_matrix[self.x_pos // 60][self.y_pos // 60]),
                                (60, 60))
        self.grid.create_object((self.x_pos, self.y_pos - 60),
                                self.grid.objects.get(self.grid.grid_matrix[self.x_pos // 60][(self.y_pos - 60) // 60]),
                                (60, 60))
        # zmienić pozycję gracza
        self.y_pos += self.step

        # print(self.x_pos, self.y_pos)
        yes_or_nor = (self.x_pos, self.y_pos)

        self.mines_do(yes_or_nor)

        self.saper_rect = self.saper.get_rect(
            center=(self.x_pos + 25, self.y_pos + 25)
        )

    def find_path(self, matrix, end):
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
        self.path = moves

