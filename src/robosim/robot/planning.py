# planning.py

import heapq

class Planning:
    def __init__(self):
        self.path = []

    def heuristic(self, a, b):
        # Manhattan distance heuristic
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def a_star(self, start, goal, grid):
        print(f"Starting A* from {start} to {goal}")
        self.path = []
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                # Reconstruct path
                while current in came_from:
                    self.path.append(current)
                    current = came_from[current]
                self.path.reverse()
                print(f"Path found: {self.path}")
                return

            neighbors = [
                (current[0] + 1, current[1]), (current[0] - 1, current[1]),
                (current[0], current[1] + 1), (current[0], current[1] - 1)
            ]
            
            for neighbor in neighbors:
                if neighbor not in grid or grid[neighbor] == 1:
                    continue

                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        print("No path found")
        self.path = []

    def plan_move(self, current_position, target_position, grid):
        # Only calculate path if it hasn't been calculated yet
        if not self.path:
            start = (current_position[0] // grid['size'], current_position[1] // grid['size'])
            goal = (target_position[0] // grid['size'], target_position[1] // grid['size'])
            self.a_star(start, goal, grid['data'])

        # Follow the path if there are steps left
        if self.path:
            next_step = self.path.pop(0)
            dx, dy = next_step[0] * grid['size'], next_step[1] * grid['size']
            print(f"Next move to ({dx}, {dy})")
            if dx > current_position[0]:
                return "right"
            elif dx < current_position[0]:
                return "left"
            elif dy > current_position[1]:
                return "down"
            elif dy < current_position[1]:
                return "up"
        return None
