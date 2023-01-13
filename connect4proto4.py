import numpy as np

class Connect4:
    def __init__(self):
        self.board = np.zeros((6,7))
        self.player = 1

    def check_winner(self):
        # check rows
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3] != 0:
                    return self.board[row][col]

        # check columns
        for row in range(3):
            for col in range(7):
                if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col] != 0:
                    return self.board[row][col]

        # check diagonals
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] != 0:
                    return self.board[row][col]

        for row in range(3):
            for col in range(4):
                if self.board[row+3][col] == self.board[row+2][col+1] == self.board[row+1][col+2] == self.board[row][col+3] != 0:
                    return self.board[row][col]
        
        return 0

    def drop_piece(self, col):
        for row in range(6):
            if self.board[row][col] == 0:
                self.board[row][col] = self.player
                break
    
    def play(self):
        while True:
            print(self.board)
            col = int(input("Player {}: Which column do you want to drop your piece in? (0-6) ".format(self.player)))
            self.drop_piece(col)
            winner = self.check_winner()
            if winner != 0:
                print("Player {} wins!".format(winner))
                break
            self.player = 3 - self.player

game = Connect4()
game.play()
