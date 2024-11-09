# main.py

import pygame
import sys
from robot.robot_state import Robot
from environment.map import Environment

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
GRID_SIZE = 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Autonomous Robot Simulation")

# Initialize robot and environment
robot = Robot(x=GRID_SIZE, y=GRID_SIZE, size=GRID_SIZE, speed=GRID_SIZE, grid_size=GRID_SIZE)
environment = Environment(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)

# Generate the maze
environment.generate_maze()

# Main simulation loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update and draw the robot
    robot.update(environment)
    screen.fill((255, 255, 255))  # Clear screen
    environment.draw(screen)       # Draw obstacles (maze)
    robot.draw(screen)             # Draw robot
    pygame.display.flip()          # Update display
    pygame.time.delay(100)         # Control simulation speed (10 FPS)
