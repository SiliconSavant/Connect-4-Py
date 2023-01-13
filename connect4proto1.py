import pygame

# Initialize pygame
pygame.init()

# Set the window size and title
size = (700, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")

# Define colors
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

# Create a 2D array to represent the game board
board = [[0 for x in range(7)] for y in range(6)]

# Initialize the game variables
current_player = 1
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Draw the game board
    screen.fill(black)
    for row in range(6):
        for col in range(7):
            if board[row][col] == 1:
                color = red
            elif board[row][col] == 2:
                color = yellow
            else:
                color = black
            pygame.draw.circle(screen, color, (col * 100 + 50, row * 100 + 50), 40)

    # Check for player input
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        col = pos[0] // 100
        for row in range(6):
            if board[row][col] == 0:
                board[row][col] = current_player
                current_player = 3 - current_player
                break

    # Check for a win
    for row in range(6):
        for col in range(7):
            if board[row][col] != 0:
                if col <= 3 and board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
                    print("Player", board[row][col], "wins!")
                    game_over = True
                if row <= 2 and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                    print("Player", board[row][col], "wins!")
                    game_over = True
                if col <= 3 and row <= 2 and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                    print("Player", board[row][col], "wins!")
                    game_over = True
                if col >= 3 and row <= 2 and board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board[row + 3][col - 3]:
                    print("Player", board[row][col], "wins!")
                    game_over = True

    pygame.display.flip()

pygame.quit()
