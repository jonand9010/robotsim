# perception.py

class Perception:
    def __init__(self, sensor_range):
        self.sensor_range = sensor_range

    def sense(self, x, y, environment):
        sensor_data = []
        for obstacle in environment.obstacles:
            if abs(obstacle.x - x) <= self.sensor_range and abs(obstacle.y - y) <= self.sensor_range:
                sensor_data.append((obstacle.x, obstacle.y))
        return sensor_data
