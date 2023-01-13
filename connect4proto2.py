import pygame

# Initialize game parameters
width = 700
height = 600
grid_size = 7
num_to_win = 4

# Initialize pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Connect 4")

# Create the game grid
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game grid
    for row in range(grid_size):
        for col in range(grid_size):
            pygame.draw.rect(screen, (255, 255, 255), (col*width/grid_size, row*height/grid_size, width/grid_size, height/grid_size), 2)
            if grid[row][col] == 1:
                pygame.draw.circle(screen, (255, 0, 0), (int((col*width/grid_size) + (width/grid_size)/2), int((row*height/grid_size) + (height/grid_size)/2)), int(height/grid_size/2) - 10)
            elif grid[row][col] == 2:
                pygame.draw.circle(screen, (0, 0, 255), (int((col*width/grid_size) + (width/grid_size)/2), int((row*height/grid_size) + (height/grid_size)/2)), int(height/grid_size/2) - 10)

    pygame.display.update()

# Exit pygame
pygame.quit()
