import pygame


class Sapper():
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

    def move_left(self):
        self.saper = self.saper_left
        # odswieżanie komórek
        self.grid.create_object((self.x_pos, self.y_pos),
                                self.grid.objects.get(self.grid.grid_matrix[self.x_pos // 60][self.y_pos // 60]), (60, 60))
        self.grid.create_object((self.x_pos, self.y_pos - 60),
                                self.grid.objects.get(self.grid.grid_matrix[self.x_pos // 60][(self.y_pos - 60) // 60]),
                                (60, 60))
        # zmienić pozycję gracza
        self.x_pos -= self.step

        print(self.x_pos, self.y_pos)
        yes_or_nor = [self.x_pos, self.y_pos]
        if yes_or_nor in self.grid.mines:
            print("MINA")
        if yes_or_nor in self.grid.granats:
            print("GRANAT")

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

        print(self.x_pos, self.y_pos)
        yes_or_nor = [self.x_pos, self.y_pos]
        if yes_or_nor in self.grid.mines:
            print("MINA")
        if yes_or_nor in self.grid.granats:
            print("GRANAT")
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

        print(self.x_pos, self.y_pos)
        yes_or_nor = [self.x_pos, self.y_pos]
        if yes_or_nor in self.grid.mines:
            print("MINA")
        if yes_or_nor in self.grid.granats:
            print("GRANAT")
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

        print(self.x_pos, self.y_pos)
        yes_or_nor = [self.x_pos, self.y_pos]
        if yes_or_nor in self.grid.mines:
            print("MINA")
        if yes_or_nor in self.grid.granats:
            print("GRANAT")

        self.saper_rect = self.saper.get_rect(
            center=(self.x_pos + 25, self.y_pos + 25)
        )


