#Przyszly agent
import queue

import pyautogui as pyautogui


class Agent():
    def __init__(self, state, grid):
        self.state = state
        self.grid = grid
        self.states = {"L": {"L": "D", "R": "U"},
                       "R": {"L": "U" , "R": "D"},
                       "U": {"L": "L", "R": "R"},
                       "D": {"L": "R", "R": "L"}}
        self.moves = []
        self.prepare_matrix()
        print(self.grid)

    def prepare_matrix(self):
        rows_cnt = len(self.grid)
        cols_cnt = len(self.grid[0])

        new_matix = [[0] * rows_cnt for _ in range(cols_cnt)]

        for i in range(rows_cnt):
            for j in range(cols_cnt):
                new_matix[j][i] = self.grid[i][j]
        self.grid = new_matix

    def create_agent_grid(self, goaltest):

        for i in range(len(self.grid)):
            # print(f"i={i} matrix={matrix[i]}")
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == self.grid[0][0]:
                    self.grid[i][j] = "O"
                elif self.grid[i][j] == 2:
                    self.grid[i][j] = "2"
                elif self.grid[i][j] == 1:
                    self.grid[i][j] = "1"
                elif self.grid[i][j] == 0:
                    self.grid[i][j] = "0"
        if self.grid[goaltest[0]][goaltest[1]] != "2":
            self.grid[goaltest[0]][goaltest[1]] = "X"
        else:
            return False
        print(self.grid)
        return self.grid

    def print_grid(self, state, path):
        start = int()
        for x, pos in enumerate(self.grid[0]):
            if pos == "O":
                start = x

        i = start
        j = 0
        pos = set()
        for move in path:
            if move == "L":
                state = self.states.get(state).get(move)

            elif move == "R":
                state = self.states.get(state).get(move)

            elif move == "M":
                if state == "L":
                    j -= 1
                if state == "R":
                    j += 1
                if state == "U":
                    i -= 1
                if state == "D":
                    i += 1
            pos.add((j, i))

    def valid(self, moves):
        start = int()
        state = self.state
        for x, pos in enumerate(self.grid[0]):
            if pos == "O":
                start = x
        i = 0
        j = start

        for move in moves:
            if move == "L":
                state = self.states.get(state).get(move)

            elif move == "R":
                state = self.states.get(state).get(move)

            elif move == "M":
                if state == "L":
                    j -= 1
                if state == "R":
                    j += 1
                if state == "U":
                    i -= 1
                if state == "D":
                    i += 1
            if not (0 <= j < len(self.grid[0]) and 0 <= i < len(self.grid)):
                return False
            elif (self.grid[i][j] == "2"):
                return False

        return True

    def findEnd(self, moves):
        steps = []
        state = self.state
        start = int()
        for x, pos in enumerate(self.grid[0]):
            if pos == "O":
                start = x
        i = 0
        j = start

        print(f"moves={moves}")
        for move in moves:
            if move == "L":
                steps.append(move)
                state = self.states.get(state).get(move)

            elif move == "R":
                steps.append(move)
                state = self.states.get(state).get(move)

            elif move == "M":

                if state == "L":
                    j -= 1
                    steps.append(move)
                if state == "R":
                    j += 1
                    steps.append(move)
                if state == "U":
                    i -= 1
                    steps.append(move)
                if state == "D":
                    i += 1
                    steps.append(move)
            print(f"move={move} state={state} pos={(i, j)}")
        print()
        if self.grid[i][j] == "X":
            print("Found: " + moves)
            self.print_grid(self.state, moves)
            self.moves = moves
            print(steps)
            return True

        return False

    def findPath(self, goaltest):
        nums = queue.Queue()
        nums.put("")
        add = ""
        maze = self.create_agent_grid(goaltest)
        if maze == False:
            return "nie ma rozwiązania"

        while not self.findEnd(add):
            add = nums.get()
            for j in ["L", "R", "M"]:
                put = add + j
                if self.valid(put):
                    nums.put(put)

        self.start_aim_move(self.moves)

    def start_aim_move(self, moves):
        steps = []
        state = self.state
        i = 0
        j = 0

        for move in moves:
            if move == "L":
                state = self.states.get(state).get(move)

            elif move == "R":
                state = self.states.get(state).get(move)

            elif move == "M":

                if state == "L":
                    pyautogui.press('left')
                if state == "R":
                    pyautogui.press('right')
                if state == "U":
                    pyautogui.press('up')
                if state == "D":
                    pyautogui.press('down')








maze3 = []
maze3.append([1, 1, 0, 1, 2, 0])
maze3.append([1, 2, 0, 1, 0, 0])
maze3.append([1, 1, 0, 1, 0, 0])
maze3.append([1, 2, 0, 1, 1, 0])
maze3.append([1, 1, 0, 1, 0, 0])
#agent = Agent("R", maze3)

#agent.findPath([0, 5])
#print(agent.grid)

