from abc import ABC as abstract, abstractmethod
from random import randint


class Bomb(abstract):

    @abstractmethod
    def __init__(self):
        self.weight = int()
        self.place_ground = []
        self.visibility = int()
        self.old_or_not = bool()
        self.location = []

    @abstractmethod
    def bomb_type(self):
        pass


class Mine(Bomb):

    def __init__(self, location):
        self.weight = 2
        self.place_ground = ["grass"]
        self.visibility = 75
        self.old_or_not = bool(randint(0, 1))
        self.location = location

    def bomb_type(self):
        return "mine"


class Granade(Bomb):

    def __init__(self, location):
        self.weight = 1
        self.place_ground = ["grass", "rock"]
        self.visibility = 100
        self.old_or_not = bool(randint(0, 1))
        self.location = location

    def bomb_type(self):
        return "granade"
