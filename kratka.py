#!/usr/bin/env python
from tkinter import *
import random

GRID_SIZE = 8 #dodac wybor 8x8 czy 10x10 -> min bomby
SQUARE_SIZE = 50
MINES_NUM = 10

root = Tk()
root.title("Saper")
c = Canvas(root, width=GRID_SIZE * SQUARE_SIZE,
           height=GRID_SIZE * SQUARE_SIZE)
c.pack()


for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        c.create_rectangle(i * SQUARE_SIZE, j * SQUARE_SIZE,
                           i * SQUARE_SIZE + SQUARE_SIZE,
                           j * SQUARE_SIZE + SQUARE_SIZE, fill='brown')

root.mainloop()