from tkinter import *

from game import Game


class ChooseGameMode():
    def __init__(self):
        self.root = Tk()
        self.root.title('SAPPER')
        self.root.geometry('400x400')
        self.screen_size = (self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        self.label_text = StringVar()
        self.label_text.set(f"Own grid size (must be between {self.screen_size[0] // 60} and {self.screen_size[1] // 60})")
        self.mainframe = Frame(self.root, width=200, height=200, bg='white')
        self.mainframe.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.label = Label(self.mainframe, textvariable=self.label_text, relief=RAISED)
        self.label.place(relx=0.15, rely=0.63, relwidth=0.7, relheight=0.05)
        self.init_ui()

    def initialize_game(self, grid_size):
        try:
            grid_size[0] = int(grid_size[0])
            grid_size[1] = int(grid_size[1])
        except ValueError:
            self.label_text.set("values x y must be digit")
            return
        if ((int(grid_size[0])) * 60) > self.screen_size[0] or ((int(grid_size[1])) * 60) > self.screen_size[1]:
            self.label_text.set("Grid is bigger than size of your screen")
            return

        self.root.destroy()
        game = Game(grid_size).start_game()

    def init_ui(self):

        btn1 = Button(self.mainframe, text='9x9', command=lambda: self.initialize_game([9, 9]))
        btn1.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.1)

        btn2 = Button(self.mainframe, text='11x11', command=lambda: self.initialize_game([11, 11]))
        btn2.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.1)

        btn3 = Button(self.mainframe, text='13x13', command=lambda: self.initialize_game([13, 13]))
        btn3.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)

        grid_size_x = Entry(self.mainframe, bg='white', font=30)
        grid_size_x.place(relx=0.15, rely=0.7, relwidth=0.20, relheight=0.05)

        grid_size_y = Entry(self.mainframe, bg='white', font=30)
        grid_size_y.place(relx=0.65, rely=0.7, relwidth=0.20, relheight=0.05)

        btn = Button(self.mainframe, text='start', command=lambda: self.initialize_game([grid_size_x.get(), grid_size_y.get()]))
        btn.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.05)

        info = Label(self.mainframe, text='SAPPER', bg='#ffb700', font=40)
        info.pack()

        self.root.mainloop()