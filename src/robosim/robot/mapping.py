# mapping.py

class Mapping:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = {
            'data': {},      # Store (x, y) as keys and 1 for obstacles, 0 for free cells
            'size': grid_size  # Grid cell size
        }

    def update_map(self, sensor_data, position):
        for obs_x, obs_y in sensor_data:
            grid_x = obs_x // self.grid_size
            grid_y = obs_y // self.grid_size
            self.grid['data'][(grid_x, grid_y)] = 1  # 1 indicates obstacle

        # Mark the robot's current position as free
        robot_x, robot_y = position
        self.grid['data'][(robot_x // self.grid_size, robot_y // self.grid_size)] = 0
