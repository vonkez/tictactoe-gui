from tkinter import *

class GameView(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        default_font = ("Arial", 80, "bold")

        self.cell1 = Label(self, text="", font=default_font, relief="solid", borderwidth=3)
        self.cell1.grid(row=0, column=0, sticky=NSEW)
        self.cell2 = Label(self, text="", font=default_font, relief="solid", borderwidth=3)
        self.cell2.grid(row=0, column=1, sticky=NSEW)
        self.cell3 = Label(self, text="", font=default_font, relief="solid", borderwidth=3)
        self.cell3.grid(row=0, column=2, sticky=NSEW)

        self.cell4 = Label(self, text="", font=default_font, relief="solid", borderwidth=3)
        self.cell4.grid(row=1, column=0, sticky=NSEW)
        self.cell5 = Label(self, text="", font=default_font, relief="solid", borderwidth=3)
        self.cell5.grid(row=1, column=1, sticky=NSEW)
        self.cell6 = Label(self, text="", font=default_font, relief="solid", borderwidth=3)
        self.cell6.grid(row=1, column=2, sticky=NSEW)

        self.cell7 = Label(self, text="", font=default_font, relief="solid", borderwidth=3)
        self.cell7.grid(row=2, column=0, sticky=NSEW)
        self.cell8 = Label(self, text="", font=default_font, relief="solid", borderwidth=3)
        self.cell8.grid(row=2, column=1, sticky=NSEW)
        self.cell9 = Label(self, text="", font=default_font, relief="solid", borderwidth=3)
        self.cell9.grid(row=2, column=2, sticky=NSEW)

        self.cell1.bind("<Button-1>", lambda x: self.parent.gui_listener(0))
        self.cell2.bind("<Button-1>", lambda x: self.parent.gui_listener(1))
        self.cell3.bind("<Button-1>", lambda x: self.parent.gui_listener(2))
        self.cell4.bind("<Button-1>", lambda x: self.parent.gui_listener(3))
        self.cell5.bind("<Button-1>", lambda x: self.parent.gui_listener(4))
        self.cell6.bind("<Button-1>", lambda x: self.parent.gui_listener(5))
        self.cell7.bind("<Button-1>", lambda x: self.parent.gui_listener(6))
        self.cell8.bind("<Button-1>", lambda x: self.parent.gui_listener(7))
        self.cell9.bind("<Button-1>", lambda x: self.parent.gui_listener(8))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

