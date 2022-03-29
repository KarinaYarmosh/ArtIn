from tkinter import *

from sztuczna_inteligencja.saper import Game


class ChooseGameMode():
    def __init__(self):
        self.root = Tk()
        self.root.title('SAPPER')
        self.root.geometry('400x400')
        self.init_ui()

    def start_game(self, grid_size):
        self.root.destroy()
        game = Game(grid_size).start_game()

    def init_ui(self):
        mainframe = Frame(self.root, width=200, height=200, bg='white')
        mainframe.place(relx=0, rely=0, relwidth=1, relheight=1)

        btn1 = Button(mainframe, text='9x9', command=lambda: self.start_game((9,9)))
        btn1.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.1)

        btn2 = Button(mainframe, text='11x11', command=lambda: self.start_game((11,11)))
        btn2.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.1)

        btn3 = Button(mainframe, text='13x13', command=lambda: self.start_game((13,13)))
        btn3.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)

        grid_size_x = Entry(mainframe, bg='white', font=30)
        grid_size_x.place(relx=0.15, rely=0.7, relwidth=0.20, relheight=0.05)

        grid_size_y = Entry(mainframe, bg='white', font=30)
        grid_size_y.place(relx=0.65, rely=0.7, relwidth=0.20, relheight=0.05)

        btn = Button(mainframe, text='start')
        btn.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.05)

        info = Label(mainframe, text='SAPPER', bg='#ffb700', font=40)
        info.pack()

        self.root.mainloop()