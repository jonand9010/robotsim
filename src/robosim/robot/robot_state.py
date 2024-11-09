# robot.py

import pygame
from robot.perception import Perception
from robot.localization import Localization
from robot.mapping import Mapping
from robot.planning import Planning

class Robot:
    def __init__(self, x, y, size, speed, grid_size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.grid_size = grid_size
        self.perception = Perception(sensor_range=3)
        self.localization = Localization()
        self.mapping = Mapping(grid_size)
        self.planning = Planning()

    def update(self, environment):
        # Perception: Sense obstacles around the robot
        sensor_data = self.perception.sense(self.x, self.y, environment)
        
        # Localization: Update robot's position
        self.localization.update_position(self.x, self.y)

        # Mapping: Update the map based on sensor data
        self.mapping.update_map(sensor_data, self.localization.position)

        # Planning: Use A* to plan a path if needed
        target_position = (environment.cols - 2, environment.rows - 2)
        direction = self.planning.plan_move(self.localization.position, target_position, self.mapping.grid)

        # Move the robot in the planned direction
        self.move(direction, environment)

    def move(self, direction, environment):
        new_x, new_y = self.x, self.y
        if direction == "left":
            new_x -= self.speed
        elif direction == "right":
            new_x += self.speed
        elif direction == "up":
            new_y -= self.speed
        elif direction == "down":
            new_y += self.speed

        # Check for obstacle collisions
        if not any(obstacle.collides(new_x, new_y, self.size) for obstacle in environment.obstacles):
            self.x, self.y = new_x, new_y
            print(f"Robot moved {direction} to ({self.x}, {self.y})")
        else:
            print(f"Obstacle detected at ({new_x}, {new_y}), staying at ({self.x}, {self.y})")

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.size, self.size))
