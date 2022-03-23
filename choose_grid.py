import os
from tkinter import *


root = Tk()
root.title('sapper')
root.geometry('400x400')

def start_sapper(grid_size):
    root.destroy()
    import saper

mainframe = Frame(root, width=200, height=200, bg='white')
mainframe.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(mainframe, text='9x9', command=lambda:start_sapper((9,9)))
btn1.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.1)

btn2 = Button(mainframe, text='11x11', command=lambda:start_sapper((11,11)))
btn2.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.1)

btn3 = Button(mainframe, text='13x13', command=lambda:start_sapper((13,13)))
btn3.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)

grid_size_x = Entry(mainframe, bg='white', font=30)
grid_size_x.place(relx=0.15, rely=0.7, relwidth=0.20, relheight=0.05)

grid_size_y = Entry(mainframe, bg='white', font=30)
grid_size_y.place(relx=0.65, rely=0.7, relwidth=0.20, relheight=0.05)

btn = Button(mainframe, text='start')
btn.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.05)

info = Label(mainframe, text='SAPPER', bg='#ffb700', font=40)
info.pack()

root.mainloop()