# Connect 4 Game

import numpy as np

# Initialize the game board
board = np.zeros((6,7))

# Function to print the game board
def print_board():
    for row in board:
        print(row)

# Function to check if a player has won
def check_win(player):
    # Check for horizontal win
    for row in board:
        for i in range(4):
            if row[i] == player and row[i+1] == player and row[i+2] == player and row[i+3] == player:
                return True
    # Check for vertical win
    for col in range(7):
        for row in range(3):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
    # Check for diagonal win (top-left to bottom-right)
    for col in range(4):
        for row in range(3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
    # Check for diagonal win (bottom-left to top-right)
    for col in range(4):
        for row in range(3, 6):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True
    return False

# Initialize variables for the game loop
player = 1
game_over = False

# Game loop
while not game_over:
    # Print the game board
    print_board()

    # Get the player's move
    move = int(input("Player {}: Which column would you like to drop your piece in (0-6)? ".format(player)))

    # Check if the column is full
    if board[0][move] != 0:
        print("Column is full. Please choose a different column.")
        continue

    # Find the first empty spot in the chosen column
    for i in range(5, -1, -1):
        if board[i][move] == 0:
            board[i][move] = player
            break

    # Check if the player has won
    if check_win(player):
        print("Player {} wins!".format(player))
        game_over = True
        break

    # Check for a tie
    if np.count_nonzero(board) == 42:
        print("Tie game!")
        game_over = True
        break

    # Switch to the other player
    player = 2 if player == 1 else 1

