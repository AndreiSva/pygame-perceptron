import pygame
from . import perceptron
import numpy as np

def paint(grid, brush):
    x, y = pygame.mouse.get_pos()
    x_cell = (x // 10) - 1
    y_cell = (y // 10) - 1
    if x_cell >= 0 and x_cell < 26 and y_cell >= 0 and y_cell < 26:
        grid[y_cell:y_cell + brush.shape[0], x_cell:x_cell + brush.shape[1]] += brush

def main():
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    pygame.display.set_caption("pygame-perceptron UI")

    grid = np.zeros((perceptron.CANVAS_WIDTH, perceptron.CANVAS_HEIGHT))
    brush = np.array([
        [8, 15, 8],
        [15, 20, 15],
        [8, 15, 8]])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    grid.fill(0)
                elif event.button == 1:
                    paint(grid, brush)
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0] == True:
                    paint(grid, brush)

        screen.fill("black")
        grid = np.clip(grid, 0, 255)
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                pygame.draw.rect(screen, (cell, cell, cell), pygame.Rect((j * 10, i * 10), (10, 10)))
                
        # forward propagate
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
