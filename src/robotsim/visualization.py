# visualization.py

import pygame

# Color definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (169, 169, 169)  # Color for obstacles

# Visualization class to handle drawing the grid, path, robot, and goal
class Visualization:
    def __init__(self, screen, grid_size, grid_width, grid_height, start, goal):
        self.screen = screen
        self.grid_size = grid_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.start = start
        self.goal = goal

    def draw_grid(self, grid):
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                if grid[y][x] == 0:
                    color = WHITE  # Free space
                elif grid[y][x] == 1:
                    color = GRAY   # Obstacle
                pygame.draw.rect(self.screen, color, (x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size))

    def draw_goal(self):
        pygame.draw.circle(self.screen, RED, (self.goal[0] * self.grid_size + self.grid_size // 2, self.goal[1] * self.grid_size + self.grid_size // 2), self.grid_size // 4)

    def draw_path(self, path):
        for pos in path:
            pygame.draw.rect(self.screen, GREEN, (pos[0] * self.grid_size, pos[1] * self.grid_size, self.grid_size, self.grid_size))

    def draw_robot(self, position):
        pygame.draw.circle(self.screen, BLUE, (position[0] * self.grid_size + self.grid_size // 2, position[1] * self.grid_size + self.grid_size // 2), self.grid_size // 4)

    def update(self):
        pygame.display.update()
