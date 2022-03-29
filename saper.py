import pygame
import random
from sztuczna_inteligencja.gameObjects.kratka import Grid

class Game():
    def __init__(self, grid_size):
        pygame.init()
        self.win = pygame.display.set_mode((grid_size[0]*60, grid_size[1]*60))
        pygame.display.set_caption("Saper")
        self.x = 0
        self.y = 0
        self.step = 60
        self.MINES_NUM = 8
        self.GRANATS_NUM = 8
        self.run = True
        self.gran = True
        self.clock = pygame.time.Clock()
        self.grid = Grid(grid_size, self.win)
        self.granats = []
        self.mines = []
        self.spawn_hazards()

    def spawn_hazards(self):
        counter=0
        #bombs
        while counter != self.MINES_NUM:
            s = int(random.randrange(0, 540, 60))
            d = int(random.randrange(0, 540, 60))
            mine = [s, d]
            if (mine not in self.mines) and (mine != [0, 0]):
                self.mines.append(mine)
                counter += 1
        print(self.mines)

        counter = 0
        while counter != self.GRANATS_NUM:
            l = int(random.randrange(0, 540, 60))
            m = int(random.randrange(0, 540, 60))
            granat = [l, m]
            if (granat not in self.mines) and (granat not in self.granats) and (granat != [0, 0]):
                self.granats.append(granat)
                counter += 1
        print(self.granats)
        print(self.mines == self.granats)

    def start_game(self):
        while self.run:
            pygame.time.delay(60)
            # opóźnienie w grze

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            # obsługa zdarzeń
            keys = pygame.key.get_pressed()
            # warunki do zmiany pozycji obiektu
            # clock.tick(75)
            # Trzymanie gracza na ekranie
            saper_surf = saper_down = saper_up = pygame.image.load('sprites/saper.png')
            saper_left = pygame.image.load('sprites/saper_left.png')
            saper_right = pygame.image.load('sprites/saper_right.png')

            saper = saper_surf
            # print(x,y)
            if keys[pygame.K_LEFT] and self.x - self.step > -60:
                saper = saper_left
                # odswieżanie komórek
                self.grid.create_object((self.x, self.y), self.grid.objects.get(self.grid.grid_matrix[self.x // 60][self.y // 60]), (60, 60))
                self.grid.create_object((self.x, self.y - 60), self.grid.objects.get(self.grid.grid_matrix[self.x // 60][(self.y - 60) // 60]), (60, 60))
                # zmienić pozycję gracza
                self.x -= self.step

                print(self.x, self.y)
                yes_or_nor = [self.x, self.y]
                if yes_or_nor in self.mines:
                    print("MINA")
                if yes_or_nor in self.granats:
                    print("GRANAT")

            if keys[pygame.K_RIGHT] and self.x + self.step < 540:
                saper = saper_right

                # odswieżanie komórek
                self.grid.create_object((self.x, self.y), self.grid.objects.get(self.grid.grid_matrix[self.x // 60][self.y // 60]), (60, 60))
                self.grid.create_object((self.x, self.y - 60), self.grid.objects.get(self.grid.grid_matrix[self.x // 60][(self.y - 60) // 60]), (60, 60))
                # zmienić pozycję gracza
                self.x += self.step

                print(self.x, self.y)
                yes_or_nor = [self.x, self.y]
                if yes_or_nor in self.mines:
                    print("MINA")
                if yes_or_nor in self.granats:
                    print("GRANAT")

            if keys[pygame.K_UP] and self.y - self.step > -60:
                saper = saper_up

                # odswieżanie komórek
                self.grid.create_object((self.x, self.y), self.grid.objects.get(self.grid.grid_matrix[self.x // 60][self.y // 60]), (60, 60))
                self.grid.create_object((self.x, self.y - 60), self.grid.objects.get(self.grid.grid_matrix[self.x // 60][(self.y - 60) // 60]), (60, 60))
                # zmienić pozycję gracza
                self.y -= self.step

                print(self.x, self.y)
                yes_or_nor = [self.x, self.y]
                if yes_or_nor in self.mines:
                    print("MINA")
                if yes_or_nor in self.granats:
                    print("GRANAT")

            if keys[pygame.K_DOWN] and self.y + self.step < 540:
                saper = saper_down

                # odswieżanie komórek

                self.grid.create_object((self.x, self.y), self.grid.objects.get(self.grid.grid_matrix[self.x // 60][self.y // 60]), (60, 60))
                self.grid.create_object((self.x, self.y - 60), self.grid.objects.get(self.grid.grid_matrix[self.x // 60][(self.y - 60) // 60]), (60, 60))

                # zmienić pozycję gracza
                self.y += self.step

                print(self.x, self.y)
                yes_or_nor = [self.x, self.y]
                if yes_or_nor in self.mines:
                    print("MINA")
                if yes_or_nor in self.granats:
                    print("GRANAT")

            saper_rect = saper.get_rect(
                center=(self.x + 25, self.y + 25)
            )
            self.win.blit(saper, saper_rect)

            # if saper == mines:

            # odświeżenie ekranu
            pygame.display.update()



