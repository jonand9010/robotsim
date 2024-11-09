# perception.py

class Perception:
    def __init__(self, sensor_range=1):
        self.sensor_range = sensor_range  # Number of cells the robot can "see"

    def sense(self, x, y, environment):
        sensor_data = []
        grid_size = environment.grid_size

        # Calculate neighboring cell positions
        for dx in range(-self.sensor_range, self.sensor_range + 1):
            for dy in range(-self.sensor_range, self.sensor_range + 1):
                if dx == 0 and dy == 0:
                    continue  # Skip the robot's current cell

                neighbor_x = x + dx * grid_size
                neighbor_y = y + dy * grid_size

                # Check if this neighbor cell has an obstacle
                if environment.is_obstacle(neighbor_x, neighbor_y):
                    sensor_data.append((neighbor_x, neighbor_y))

        return sensor_data
