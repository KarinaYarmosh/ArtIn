import enum
import os
import random

from gameObjects.bomby import Mine, Granade
from gameTools.tools import resize_image

class Grid():

    def __init__(self, size, window):
        self.objects = {0: "grass.png", 1: "rock.jpg", 2:"duzykamien.jpg", 3:"kaluza1.jpg"}
        self.window = window
        self.grid_matrix = []
        self.size = size
        self.SCREEN_HEIGHT = window.get_height()
        self.SCREEN_WIDTH = window.get_width()
        self.window = window
        self.TILE_SIZE = (60, 60)#(int(self.SCREEN_WIDTH / size[0]), int(self.SCREEN_HEIGHT / size[1]))
        self.MINES_NUM = size[0]-1 #9krat - 8 mines; 11krat - 10 mines; 13krat - 12 mines
        self.GRANATS_NUM = size[0]-1
        self.granats = {}
        self.mines = {}
        self.create_grid(self.size)
        self.spawn_hazards()


    #powstanie macierzy z wylosowanymi nazwami objektów, a potem rysowanie kratki na podstawie tej macierzy
    def create_grid(self, size):
        #print(size[0])
        matrix = []
        for i in range(size[0]):
            matrix.append(list())
            row = matrix[i]
            for j in range(size[1]):
                if (i==2 and j==3) or (i==3 and j==6) or (i==1 and j==2) or (i==8 and j==8) or (i==3 and j==3) \
                        or (i==0 and j==7) or (i==7 and j==1) or (i==9 and j==0) or (i==9 and j==0) or (i==7 and j==9) \
                        or (i==2 and j==6) or (i==0 and j==2) or (i==0 and j==9) or (i==5 and j==8) or (i==4 and j==6) \
                        or (i==3 and j==0) or (i==5 and j==1) or (i==9 and j==10) or (i==8 and j==11) or (i==13 and j==6) \
                        or (i==7 and j==12) or (i==1 and j==13) or (i==0 and j==12):
                    row.append(2)
                else:
                    row.append(random.choice([0, 1, 3]))
            #random.shuffle(matrix[i])
        #random.shuffle(matrix)
        # print(matrix)
        # for i in range(len(matrix)):
        #     #print(f"i={i} matrix={matrix[i]}")
        #     for j in range(len(matrix[i])):
        #         print(f"i={i} j={j} matrix={matrix[i][j]}")
        #         if matrix[i][j] == 2 and (matrix[i][j-1]==2 or matrix[i-1][j-1]==2 or matrix[i-1][j]==2 or matrix[i][j-1]==2):
        #             matrix[i][j] = random.randrange(0, 2)
        # matrix = []
        # for i in range(size[0]):
        #     matrix.append(list())
        #     row = matrix[i]
        #     for j in range(size[1]):
        #         if (i==0 and j==0) or (i==0 and j==1) or (i==1 and j==0):
        #             row.append(random.randrange(0, 2))
        #         else:
        #             row.append(random.randrange(0, 3))
        #     #random.shuffle(matrix[i])
        # #random.shuffle(matrix)
        # print(matrix)
        # for i in range(len(matrix)):
        #     #print(f"i={i} matrix={matrix[i]}")
        #     for j in range(len(matrix[i])):
        #         print(f"i={i} j={j} matrix={matrix[i][j]}")
        #         if matrix[i][j] == 2 and (matrix[i][j-1]==2 or matrix[i-1][j-1]==2 or matrix[i-1][j]==2 or matrix[i][j-1]==2):
        #             matrix[i][j] = random.randrange(0, 2)
        print(matrix)
        self.grid_matrix = matrix
        self.draw_grid(matrix, self.window)
        print(self.grid_matrix)
        print(self.grid_matrix[1][2])

    def draw_grid(self, grid_matrix, window):
        # rysowanie wierszy
        for i in range(len(grid_matrix)):
            # rysowanie kolumn
            for j in range(len(grid_matrix[i])):
                #sprawdzamy wartości w macierzy i na podstawie wartości rysujemy odpowiedni object

                self.create_object((i * self.TILE_SIZE[0], j * self.TILE_SIZE[1]), self.objects.get(self.grid_matrix[i][j]), self.TILE_SIZE)

    def spawn_hazards(self):
        counter=0
        #bombs
        while counter != self.MINES_NUM:
            s = int(random.randrange(0, self.SCREEN_HEIGHT, 60))
            d = int(random.randrange(0, self.SCREEN_WIDTH, 60))
            mine_pos = (s, d)
            #print(self.grid_matrix[s//60][d//60])
            if (mine_pos not in self.mines.keys()) and (mine_pos != [0, 0]) and (self.grid_matrix[s//60][d//60] == 0):
                self.mines[mine_pos] = Mine(mine_pos)
                self.grid_matrix[s//60][d//60] = 0
                self.create_object(mine_pos, self.objects.get(0), self.TILE_SIZE)
                counter += 1
        #print(self.mines)

        counter = 0
        while counter != self.GRANATS_NUM:
            l = int(random.randrange(0, self.SCREEN_HEIGHT, 60))
            m = int(random.randrange(0, self.SCREEN_WIDTH, 60))
            granat_pos = (l, m)
            if (granat_pos not in self.mines.keys()) and (granat_pos not in self.granats.keys()) \
                    and (granat_pos != [0, 0]) and (self.grid_matrix[l//60][m//60] == 0 or self.grid_matrix[l//60][m//60] == 1):
                self.granats[granat_pos] = Granade(granat_pos)
                #print(self.granats)
                counter += 1
        #print(self.granats)
        #print(self.mines == self.granats)
        return

    #funkcja rysowania objektów
    def create_object(self, position, object_name, object_size):
        self.window.blit(resize_image(f"./sprites/{object_name}", f"./temporaryFiles/{object_name}", object_size), position)
