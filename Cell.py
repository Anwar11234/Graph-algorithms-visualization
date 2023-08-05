import pygame
from colors import colors 


class Cell:
    def __init__(self, row, col, size):
        self.row = row 
        self.col = col 
        self.x = col * size
        self.y = row * size
        self.size = size 
        self.color = colors['default']
        self.neighbours = []
        self.g = float("inf")
        self.h = 0
        self.f = float("inf") 
        self.parent = None
        self.visited = False
    
    def get_grid_pos(self):
        return self.row, self.col
        
    def is_wall(self):
        return self.color == colors['wall']
    
    def change_color(self, color):
        self.color = color
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))
    
    def get_neighbours(self):
        return self.neighbours
    
    def update_neighbours(self, grid):
        total_rows = len(grid)
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
            self.neighbours.append(grid[self.row][self.col - 1])  # left

        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
            self.neighbours.append(grid[self.row - 1][self.col])  # top
            
        if self.col < total_rows - 1 and not grid[self.row][self.col + 1].is_wall():
            self.neighbours.append(grid[self.row][self.col + 1])  # right

        if self.row < total_rows - 1 and not grid[self.row + 1][self.col].is_wall():
            self.neighbours.append(grid[self.row + 1][self.col])  # bottom

    def update_cost(self, parent, new_cost):
        self.parent = parent
        self.g = new_cost
        self.f = self.g + self.h
    
    def calculate_heuristic(self, goal):
        row, col = goal.get_grid_pos()
        return abs(self.row - row) + abs(self.col - col)
