from tkinter import *
from gameview import GameView

class MainFrame(Frame):
    def __init__(self, parent, gui_listener=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.gui_listener = gui_listener

        self.testboard = ["X", "", "O", "O", "O", "O", "X", "", "X"]

        self.parent.minsize(500, 500)
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.parent.title("TicTacToe")

        self.grid(row=0, column=0, sticky=NSEW)

        self.show_menu()

    def update_board(self, board):
        self.gameview.cell1["text"] = board[0]
        self.gameview.cell2["text"] = board[1]
        self.gameview.cell3["text"] = board[2]
        self.gameview.cell4["text"] = board[3]
        self.gameview.cell5["text"] = board[4]
        self.gameview.cell6["text"] = board[5]
        self.gameview.cell7["text"] = board[6]
        self.gameview.cell8["text"] = board[7]
        self.gameview.cell9["text"] = board[8]



    def show_menu(self, event=None):
        try:
            self.gameview.destroy()
            self.backbutton.destroy()
        except AttributeError:
            pass
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        self.start_button1 = Button(self, text="Start as X")
        self.start_button1.grid(row=0, column=0)
        self.start_button2 = Button(self, text="Start as O")
        self.start_button2.grid(row=1, column=0)
        # self.start_button3 = Button(self, command=self.show_game, text="click me")
        # self.start_button3.grid(row=2, column=0)

        self.start_button1.bind("<Button-1>", lambda x: self.gui_listener(-1))
        self.start_button2.bind("<Button-1>", lambda x: self.gui_listener(-2))
        #self.start_button3.bind("<Button-1>", lambda x: self.gui_listener(-3))

    def show_game(self):
        self.start_button1.destroy()
        self.start_button2.destroy()
        #self.start_button3.destroy()

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=0)
        self.columnconfigure(0, weight=1)

        # self.backbutton = Button(self, command=self.show_menu, text="Go Back")
        self.backbutton = Button(self, text="Go Back")
        self.backbutton.grid(row=0, column=0)
        # self.backbutton.bind("<Button-1>", lambda x: self.update_board(self.testboard))
        self.backbutton.bind("<Button-1>", lambda x: self.gui_listener(-5))

        self.gameview = GameView(self)
        self.gameview.grid(row=1, column=0, sticky=NSEW)

