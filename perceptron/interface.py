import pygame
import numpy as np

def main():
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    pygame.display.set_caption("pygame-perceptron UI")

    grid = np.zeros(28 * 28).reshape((28, 28))
    brush = np.array([[1, 3, 1], [2, 5, 2], [1, 3, 1]])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                pygame.draw.rect(screen, (cell, cell, cell), pygame.Rect((j * 10, i * 10), (10, 10)))

        if pygame.mouse.get_pressed()[0] == True:
            x, y = pygame.mouse.get_pos()
            x_cell = (x // 10) - 1
            y_cell = (y // 10) - 1
            if x_cell >= 0 and x_cell < 26 and y_cell >= 0 and y_cell < 26:
                grid[y_cell:y_cell + brush.shape[0], x_cell:x_cell + brush.shape[1]] += brush
            grid = np.clip(grid, 0, 255)
                
        # forward propagate

        pygame.display.flip()

    pygame.quit()
