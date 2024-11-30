# main.py

import pygame
import random
from robot import Robot
from visualization import Visualization

# Colors (define them here)
BLACK = (0, 0, 0)

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
START = (1, 1)
END = (GRID_WIDTH - 2, GRID_HEIGHT - 2)

# Clock for FPS
clock = pygame.time.Clock()

def generate_obstacles(grid, num_obstacles=50):
    for _ in range(num_obstacles):
        x = random.randint(1, GRID_WIDTH - 2)
        y = random.randint(1, GRID_HEIGHT - 2)
        if (x, y) != START and (x, y) != END:  # Ensure start and end are not obstacles
            grid[y][x] = 1  # Mark the cell as an obstacle
    return grid

def main():
    # Create an empty grid and place obstacles
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    grid = generate_obstacles(grid)

    # Create Robot object
    robot = Robot(START, END, grid, GRID_WIDTH, GRID_HEIGHT)
    robot.plan_route()  # Calculate the initial path

    # Initialize the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Create Visualization object
    visualization = Visualization(screen, GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, START, END)

    running = True
    while running:
        screen.fill(BLACK)

        # Draw grid, obstacles, path, goal, and robot
        visualization.draw_grid(grid)
        visualization.draw_path(robot.path)  # Draw the calculated path
        visualization.draw_robot(robot.position)
        visualization.draw_goal()  # Draw the goal

        # Move the robot step by step along the path
        if robot.path:
            robot.move()  # Execute the movement along the path

        # Stop pathfinding when the robot reaches the goal
        if robot.position == END:
            robot.path = []  # Stop moving once we reach the goal

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        visualization.update()  # Update the display
        clock.tick(10)  # Limit the FPS to 10

    pygame.quit()

if __name__ == "__main__":
    main()
