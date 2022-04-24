from abc import ABC as abstract, abstractmethod
from random import randint

class Elementy(abstract):

    @abstractmethod
    def __init__(self):
        self.koszt = int()

    @abstractmethod
    def elementy_type(self):
        pass

class Grass(Elementy):

    def __init__(self, location):
        self.koszt = 0

    def elementy_type(self):
        return "grass"

class Rock(Elementy):

    def __init__(self, location):
        self.koszt = 1

    def elementy_type(self):
        return "rock"

class Duzykamien(Elementy):

    def __init__(self, location):
        self.koszt = 100

    def elementy_type(self):
        return "duzykamien"

class Kaluza(Elementy):

    def __init__(self, location):
        self.koszt = 3

    def elementy_type(self):
        return "kaluza"