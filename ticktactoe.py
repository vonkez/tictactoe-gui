import random
from time import sleep

class Tictactoe:
    def __init__(self, gui):
        self.gui = gui
        self.gui.gui_listener = self.listener
        self.player_mark = None
        self.computer_mark = None
        self.turn = "X"
        self.board = [" "]*9

    def listener(self, signal):
        if signal == -1:
            # selected X
            self.player_mark = "X"
            self.computer_mark = "O"
            self.gui.show_game()
        elif signal == -2:
            # selected O
            self.player_mark = "O"
            self.computer_mark = "X"
            self.gui.show_game()
            self.play(self.computer_move())
        elif signal == -5:
            # reset game
            self.turn = "X"
            self.player_mark = None
            self.board = [" "]*9
        elif signal >= 0:
            cell = signal
            if self.turn != self.player_mark:
                return
            if not self.cell_available(cell):
                return
            print(f"player: {cell}")

            if self.play(cell):  # if game ends
                return
            c = self.computer_move()
            self.play(c)
            print(f"computer: {c}")


    def play(self, cell):
        self.board[cell] = self.turn
        self.gui.update_board(self.board)
        if self.check_win():
            print(f"Winner: {self.turn}")
            # reset game
            self.listener(-5)
            self.gui.show_menu()
            return True
        if self.is_full():
            print(f"Draw")
            # reset game
            self.listener(-5)
            self.gui.show_menu()
            return True
        self.new_turn()

    def computer_move(self):
        x = random.randint(0, 8)
        while not self.cell_available(x):
            x = random.randint(0, 8)
        return x

    def cell_available(self, cell):
        if self.board[cell] == " ":
            return True
        else:
            return False

    def new_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def is_full(self):
        for cell in self.board:
            if cell == " ":
                return False
        return True


    def check_win(self):
        if self.board[0] == self.turn and self.board[4] == self.turn and self.board[8] == self.turn:
            return True
        if self.board[1] == self.turn and self.board[4] == self.turn and self.board[7] == self.turn:
            return True
        if self.board[2] == self.turn and self.board[4] == self.turn and self.board[6] == self.turn:
            return True
        if self.board[5] == self.turn and self.board[4] == self.turn and self.board[3] == self.turn:
            return True
        if self.board[0] == self.turn and self.board[1] == self.turn and self.board[2] == self.turn:
            return True
        if self.board[2] == self.turn and self.board[5] == self.turn and self.board[8] == self.turn:
            return True
        if self.board[8] == self.turn and self.board[7] == self.turn and self.board[6] == self.turn:
            sleep(1)
            return True
        if self.board[6] == self.turn and self.board[3] == self.turn and self.board[0] == self.turn:
            return True
        return False
