from AI.BFS import BFS
from collections import deque


class connectAItoGame:
    def __init__(self, grid_matrix):
        # transposing matrix
        self.grid_matrix = [[grid_matrix[j][i] for j in range(len(grid_matrix))] for i in range(len(grid_matrix[0]))]

    def get_BFS_path(self):
        return BFS(self.grid_matrix).graphsearch(deque(), [], [0, 0], "D")
