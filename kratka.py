#!/usr/bin/env python
from tkinter import *
import random

GRID_SIZE = 9 #dodac wybor 9x9 czy 15x15 czy 21x21  -> min bomby sie zmieniaja
SQUARE_SIZE = 50
#MINES_NUM = 12-15, 35-40, 68-70

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