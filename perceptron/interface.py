import pygame
import numpy as np

def main():
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    pygame.display.set_caption("pygame-perceptron UI")

    grid = np.zeros(28 * 28).reshape((28, 28))
    #brush = np.array([1, 3, 1], [2, 5, 2], [1, 3, 1]).reshape((3,3))
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
            x_cell = x // 10
            y_cell = y // 10
            if grid[y_cell][x_cell] < 255:
                grid[y_cell][x_cell] += 1
                
        # forward propagate

        pygame.display.flip()

    pygame.quit()
