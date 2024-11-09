# environment.py

import pygame
import random

class Obstacle:
    def __init__(self, x, y, size, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def collides(self, x, y, size):
        # Check if the given position overlaps with this obstacle
        return self.x == x and self.y == y


class Environment:
    def __init__(self, screen_width, screen_height, grid_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_size = grid_size
        self.rows = screen_height // grid_size
        self.cols = screen_width // grid_size
        self.obstacles = []

    def generate_maze(self):
        # Initialize grid for the maze generation
        maze_grid = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Starting point for maze generation
        start_row, start_col = 1, 1
        maze_grid[start_row][start_col] = 0  # 0 represents a free cell

        # DFS-based maze generation
        stack = [(start_row, start_col)]
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # Moving two steps in cardinal directions

        while stack:
            row, col = stack[-1]
            random.shuffle(directions)  # Shuffle directions to create random paths
            carved = False

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check if the new cell is within bounds and is a wall
                if 1 <= new_row < self.rows - 1 and 1 <= new_col < self.cols - 1 and maze_grid[new_row][new_col] == 1:
                    # Carve out a path between the current cell and the new cell
                    maze_grid[row + dr // 2][col + dc // 2] = 0  # Midpoint between cells
                    maze_grid[new_row][new_col] = 0
                    stack.append((new_row, new_col))
                    carved = True
                    break

            if not carved:
                stack.pop()

        # Convert maze grid into obstacles
        for row in range(self.rows):
            for col in range(self.cols):
                if maze_grid[row][col] == 1:
                    self.add_obstacle(col * self.grid_size, row * self.grid_size)

    def add_obstacle(self, x, y):
        obstacle = Obstacle(x, y, self.grid_size)
        self.obstacles.append(obstacle)

    def is_obstacle(self, x, y):
        # Check if there's an obstacle at the given (x, y) position
        for obstacle in self.obstacles:
            if obstacle.collides(x, y, self.grid_size):
                return True
        return False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
