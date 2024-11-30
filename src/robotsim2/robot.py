# robot.py

import heapq
import pygame

BLUE = (0, 0, 255)

# Robot class
class Robot:
    def __init__(self, start, goal, grid, grid_width, grid_height):
        self.position = start
        self.goal = goal
        self.grid = grid
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.path = []
        self.planner = Planning()
        self.activation = Activation()

    def plan_route(self):
        self.path = self.planner.a_star(self.position, self.goal, self.grid, self.grid_width, self.grid_height)

    def move(self):
        self.path = self.activation.execute_movement(self, self.path)

# Planning module (A* pathfinding)
class Planning:
    @staticmethod
    def a_star(start, end, grid, grid_width, grid_height):
        open_list = []
        closed_list = set()

        start_node = Node(start, 0, Planning.heuristic(start, end))
        heapq.heappush(open_list, start_node)

        while open_list:
            current_node = heapq.heappop(open_list)
            if current_node.pos == end:
                path = []
                while current_node:
                    path.append(current_node.pos)
                    current_node = current_node.parent
                return path[::-1]

            closed_list.add(current_node.pos)
            neighbors = Planning.get_neighbors(current_node.pos, grid, grid_width, grid_height)
            for neighbor in neighbors:
                if neighbor in closed_list:
                    continue

                g = current_node.g + 1  # all moves cost the same
                h = Planning.heuristic(neighbor, end)
                neighbor_node = Node(neighbor, g, h, current_node)

                if not any(n.pos == neighbor and n.f <= neighbor_node.f for n in open_list):
                    heapq.heappush(open_list, neighbor_node)

        return []

    @staticmethod
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

    @staticmethod
    def get_neighbors(pos, grid, grid_width, grid_height):
        x, y = pos
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_width and 0 <= ny < grid_height and grid[ny][nx] != 1:
                neighbors.append((nx, ny))
        return neighbors

class Node:
    def __init__(self, pos, g=0, h=0, parent=None):
        self.pos = pos
        self.g = g  # cost from start
        self.h = h  # heuristic (estimated cost to goal)
        self.f = g + h  # total cost
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

# Activation module (Execution of robot movement)
class Activation:
    @staticmethod
    def execute_movement(robot, path):
        if path:
            # Move one step along the path
            robot.position = path[1] if len(path) > 1 else robot.position
            # Remove the first element of the path as the robot moves
            path = path[1:] if path else []
        return path
