#Przyszly agent
import queue

def createMaze2():
    maze3 = []
    maze3.append([1, 1, 0, 1, 2, 0])
    maze3.append([1, 2, 0, 1, 0, 0])
    maze3.append([1, 1, 0, 1, 0, 0])
    maze3.append([1, 2, 0, 1, 1, 0])
    maze3.append([1, 1, 0, 1, 0, 0])


    for i in range(len(maze3)):
        # print(f"i={i} matrix={matrix[i]}")
        for j in range(len(maze3[i])):
            if maze3[i][j] == maze3[0][0]:
                maze3[i][j] = "O"
            elif i==4 and j==0:
                maze3[i][j] = "X"
            elif maze3[i][j] == 2:
                maze3[i][j] = "2"
            elif maze3[i][j] == 1:
                maze3[i][j] = "1"
            elif maze3[i][j] == 0:
                maze3[i][j] = "0"
    print(maze3)
    return maze3


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):

    for x, pos in enumerate(maze[0]):
        #print(pos)
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "2"):
            return False

    return True

states = {"L": {"LEFT": ["MOVE"], "RIGHT": ["LEFT", "LEFT", "MOVE"], "UP": ["LEFT", "MOVE"], "DOWN": ["RIGHT", "MOVE"]},
          "R": {"LEFT": ["RIGHT", "RIGHT", "MOVE"] , "RIGHT": ["MOVE"], "UP": ["RIGHT", "MOVE"], "DOWN": ["LEFT", "MOVE"]},
          "U": {"LEFT": ["RIGHT", "MOVE"], "RIGHT": ["LEFT", "MOVE"], "UP": ["MOVE"], "DOWN": ["RIGHT", "RIGHT", "MOVE"]},
          "D": {"LEFT": ["LEFT", "MOVE"], "RIGHT": ["RIGHT", "MOVE"], "UP": ["RIGHT", "RIGHT", "MOVE"], "DOWN": ["MOVE"]}}

def findEnd(maze, moves, state):
    steps = []
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            steps.extend(states.get("L").get(state))
            state = "LEFT"
            i -= 1

        elif move == "R":
            steps.extend(states.get("R").get(state))
            state = "RIGHT"
            i += 1

        elif move == "U":
            steps.extend(states.get("U").get(state))
            state = "UP"
            j -= 1

        elif move == "D":
            steps.extend(states.get("D").get(state))
            state = "DOWN"
            j += 1

    if maze[j][i] == "X":
        #print("Found: " + moves)
        printMaze(maze, moves)
        print(steps)
        return True

    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
maze = createMaze2()

state = "UP"
while not findEnd(maze, add, state):
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)

#print(nums.get())