import tkinter
from gui import MainFrame
from ticktactoe import Tictactoe

root = tkinter.Tk()
app = MainFrame(root)
ttt = Tictactoe(app)
root.mainloop()
