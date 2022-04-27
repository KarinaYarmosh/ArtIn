import heapq
from collections import deque

# from queue import PriorityQueue
# 1 - wall
# 2 - grass
# 3 - rocks
# 4 - water

# matrix = [[2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
#           [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
#           [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
#           [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
#           [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
#           [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0],
#           [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
#           [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
#           [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#           [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
#           [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#           [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

# matrix = [[2, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2],
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


# matrix = [[2,3,3], [2,4,4], [2,4,4]]


def h(a, b):
    # Manhattan distance on a square grid
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_moves(node):
    moves = []
    while node.parent is not None:
        moves.append(node.action)
        node = node.parent
    return list(reversed(moves))


class AStar:
    def __init__(self, matrix, endpoint):
        self.matrix = matrix
        self.endpoint = endpoint

    def goaltest(self, state):
        return state == self.endpoint

    def g(self, state):
        # try:
        if state.action in ["L", "R"]:
            state.cost = state.parent.cost
        elif state.action == "M":
            state.cost = state.parent.cost + self.matrix[state.state[0]][state.state[1]]
        # except N:
        #     if state.action in ["L", "R"]:
        #         state.cost = 1
        #     else:
        #         state.cost = 0 + matrix[state.state[0]][state.state[1]]
        return state.cost

    def f(self, state):
        return self.g(state) + h(state.state, self.endpoint)

    def succ(self, state, direction):
        states = []
        for action in ["L", "R", "M"]:

            node_new = node(state, direction)
            if action == "L":
                if direction == "L":
                    node_new.direction = "D"
                    node_new.action = action
                    states.append(node_new)
                elif direction == "R":
                    node_new.direction = "U"
                    node_new.action = action
                    states.append(node_new)
                elif direction == "U":
                    node_new.direction = "L"
                    node_new.action = action
                    states.append(node_new)
                else:
                    node_new.direction = "R"
                    node_new.action = action
                    states.append(node_new)
            elif action == "R":
                if direction == "L":
                    node_new.direction = "U"
                    node_new.action = action
                    states.append(node_new)
                elif direction == "R":
                    node_new.direction = "D"
                    node_new.action = action
                    states.append(node_new)
                elif direction == "U":
                    node_new.direction = "R"
                    node_new.action = action
                    states.append(node_new)
                else:
                    node_new.direction = "L"
                    node_new.action = action
                    states.append(node_new)

            elif action == "M":
                if direction == "L" and (0 <= state[1] - 1 <= len(self.matrix[0]) - 1) and (
                        self.matrix[state[0]][state[1] - 1] != 2):
                    node_new.state = [state[0], state[1] - 1]
                    node_new.action = action
                    states.append(node_new)
                elif direction == "R" and (0 <= state[1] + 1 <= len(self.matrix[0]) - 1) and (
                        self.matrix[state[0]][state[1] + 1] != 2):
                    node_new.state = [state[0], state[1] + 1]
                    node_new.action = action
                    states.append(node_new)
                elif direction == "U" and (0 <= state[0] - 1 <= len(self.matrix) - 1) and (
                        self.matrix[state[0] - 1][state[1]] != 2):
                    node_new.state = [state[0] - 1, state[1]]
                    node_new.action = action
                    states.append(node_new)
                elif direction == "D" and (0 <= state[0] + 1 <= len(self.matrix) - 1) and (
                        self.matrix[state[0] + 1][state[1]] != 2):
                    node_new.state = [state[0] + 1, state[1]]
                    node_new.action = action
                    states.append(node_new)
        return states

    def graphsearch(self, fringe, explored, istate, direction):
        fringe.put(node(istate, direction), 0)
        i = 0
        while True:
            print(i)
            if not fringe:
                return False

            elem = fringe.get()

            if self.goaltest(elem.state):
                return get_moves(elem)

            explored.append(elem)

            for state in self.succ(elem.state, elem.direction):
                state.parent = elem
                p = self.f(state)
                state.cost = self.g(state)
                print(state)
                if (state not in fringe) and (state not in explored):
                    fringe.put(state, p)
                elif (state in fringe) and state.cost > p:
                    fringe.replace(state, p)
            i += 1


class node():
    def __init__(self, state, direction):
        self.state = state
        self.parent = None
        self.action = None
        self.direction = direction
        self.cost = 0

    def __eq__(self, other):
        if isinstance(other, node):
            return (self.state == other.state and
                    self.action == other.action and
                    self.direction == other.direction)

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def __ge__(self, other):
        return self.cost >= other.cost


# print(1 in pq)
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def put(self, item, priority):
        heapq.heappush(self.queue, [priority, item])

    def get(self):
        return heapq.heappop(self.queue)[1]

    def empty(self):
        return len(self.queue) == 0

    def replace(self, item, priority):
        for i in range(len(self.queue)):
            if self.queue[i][1] == item:
                self.queue[i] = (priority, item)
                heapq.heapify(self.queue)
                return
        raise ValueError("Item not found")

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.queue)


# pq = PriorityQueue()
# pq.put("suck", 1)
# pq.put("fuckwithme", 2)
# pq.put("lickmyasshole", 3)
# pq.put("eatmyshitfromass", 4)
# print(pq.get() and pq.queue)
# print(h([0, 0], [12, 12]))

# pq = PriorityQueue()
# pq.put(node([0, 0], "D"), f(node([0, 0], "D")))
# pq.put(node([0, 0], "L"), f(node([0, 0], "L")))
# pq.put(node([0, 0], "R"), f(node([0, 0], "R")))
# print(pq)

# node1 = node([0, 0], "D")
# node2 = node([0, 0], "L")
# node1.cost = 10
# node2.cost = 10
# print(node1 == node2)
