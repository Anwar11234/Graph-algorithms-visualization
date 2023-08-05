import pygame

import a_star_search_visualizer
import bfs_search_visualizer
import dfs_search_visualizer
import dijkstra_search_visualizer
from Cell import Cell
from colors import colors


class Grid:
    def __init__(self, size, window_size):
        self.grid = []
        self.window_size = window_size 
        self.size = size
        self.cell_size = window_size // self.size
        self.build()

    def build(self):
        for i in range(self.size):
            self.grid.append([])
            for j in range(self.size):
                self.grid[i].append(Cell(i, j, self.cell_size))
        
    def get_cell(self, row, col):
        return self.grid[row][col]
    
    def update_cells_neighbours(self):
        for row in self.grid:
            for cell in row:
                cell.update_neighbours(self.grid)


class GridVisualizer(Grid):
    def __init__(self, size, window_size, window):
        super().__init__(size, window_size)
        self.window = window

    def update_screen(self):
        self.window.fill(colors['default'])
        self.draw_grid()
        pygame.display.update()

    def draw_grid(self):
        self.draw_grid_cells()
        self.draw_grid_lines()

    def draw_grid_cells(self):
        for row in self.grid:
            for cell in row:
                cell.draw(self.window)

    def draw_grid_lines(self):
        for i in range(self.size):
            pygame.draw.line(self.window, colors['line'], (0, i * self.cell_size),
                             (self.window_size, i * self.cell_size))
            for j in range(self.size):
                pygame.draw.line(self.window, colors['line'], (j * self.cell_size, 0), (j * self.cell_size,
                                                                                        self.window_size))

    def draw_path(self, current):
        while current.parent:
            current.change_color(colors['path'])
            current = current.parent
            self.update_screen()


class GridSearchVisualizer(GridVisualizer):
    def __init__(self, size, window_size, window):
        super().__init__(size, window_size, window)

    def dijkstra(self, start, goal):
        dijkstra_search_visualizer.search(self, start, goal)
    
    def a_star_search(self, start, goal):
        a_star_search_visualizer.search(self, start, goal)
        
    def dfs(self, start, goal):
        dfs_search_visualizer.search(self, start, goal)

    def bfs(self, start, goal):
        bfs_search_visualizer.search(self, start, goal)
