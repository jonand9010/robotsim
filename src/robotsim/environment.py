import random

class Environment:
    def __init__(self, GRID_WIDTH, GRID_HEIGHT):
        self.GRID_WIDTH = GRID_WIDTH
        self.GRID_HEIGHT = GRID_HEIGHT


    def generate_grid(self, start, end):
        grid = [[0 for _ in range(self.GRID_WIDTH)] for _ in range(self.GRID_HEIGHT)]
        grid = self.generate_obstacles(grid, start, end)
        return grid

    def generate_obstacles(self, grid, START, END, num_obstacles=50):
        for _ in range(num_obstacles):
            x = random.randint(1, self.GRID_WIDTH - 2)
            y = random.randint(1, self.GRID_HEIGHT - 2)
            if (x, y) != START and (x, y) != END:  # Ensure start and end are not obstacles
                grid[y][x] = 1  # Mark the cell as an obstacle
        return grid