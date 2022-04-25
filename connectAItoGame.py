from AI.BFS import BFS
from AI.AStar import AStar
from collections import deque

from AI.AStar import PriorityQueue


class connectAItoGame:
    def __init__(self, grid_matrix):
        # transposing matrix
        # self.grid_matrix = [[2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        #           [1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        #           [2, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2],
        #           [2, 2, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2],
        #           [2, 2, 2, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2],
        #           [2, 2, 2, 2, 1, 1, 2, 3, 2, 2, 2, 2, 2],
        #           [2, 2, 2, 2, 2, 1, 1, 2, 3, 2, 2, 2, 2],
        #           [2, 2, 2, 2, 2, 2, 1, 1, 2, 3, 2, 2, 2],
        #           [2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 3, 2, 2],
        #           [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 3, 2],
        #           [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 3],
        #           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2],
        #           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2]]
        self.grid_matrix = [[grid_matrix[j][i] for j in range(len(grid_matrix))] for i in range(len(grid_matrix[0]))]
        # self.grid_matrix = grid_matrix

    def get_BFS_path(self):
        return BFS(self.grid_matrix).graphsearch(deque(), [], [0, 0], "D")

    def get_AStar_path(self):
        for i in self.grid_matrix:
            for i2 in i:
                print(i2, end=' ')
            print()
        return AStar(self.grid_matrix).graphsearch(PriorityQueue(), [], [0, 0], "D")
