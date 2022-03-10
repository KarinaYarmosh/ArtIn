import enum
import random
from sztuczna_inteligencja.gameTools.tools import resize_image

class Grid():

    #baza objektów
    @enum.unique
    class Objects(enum.Enum):
        GRASS = "grass.png"
        ROCK = "rock.jpg"

    def __init__(self, size, window):
        self.grid_matrix = []
        self.size = size
        self.SCREEN_HEIGHT = window.get_height()
        self.SCREEN_WIDTH = window.get_width()
        self.window = window
        self.TILE_SIZE = (self.SCREEN_WIDTH / size[0], self.SCREEN_HEIGHT / size[1])
        self.create_grid(self.size)

    #powstanie macierzy z wylosowanymi nazwami objektów, a potem rysowanie kratki na podstawie tej macierzy
    def create_grid(self, size):
        matrix = []
        for i in range(size[0]):
            matrix.append(list())
            row = matrix[i]
            for j in range(size[1]):
                row.append(random.randint(0, 1))
            random.shuffle(matrix[i])
        random.shuffle(matrix)
        self.grid_matrix = matrix
        self.draw_grid(matrix, self.window)

    def draw_grid(self, grid_matrix, window):
        # rysowanie wierszy
        for i in range(len(grid_matrix)):
            # rysowanie kolumn
            for j in range(len(grid_matrix[i])):
                #sprawdzamy wartości w macierzy i na podstawie wartości rysujemy odpowiedni object
                if grid_matrix[i][j] == 1:
                    self.create_object((i * self.TILE_SIZE[0], j * self.TILE_SIZE[1]), self.Objects.ROCK.value, (60, 60), window)
                else:
                    self.create_object((i * self.TILE_SIZE[0], j * self.TILE_SIZE[1]), self.Objects.GRASS.value, (60, 60), window)
    #funkcja rysowania objektów
    def create_object(self, position, object_name, object_size, window):
        window.blit(resize_image(f"./sprites/{object_name}", f"temporaryFiles/{object_name}", object_size), position)