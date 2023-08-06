import pygame
from colors import colors
from Grid import Grid


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
                self.draw_grid_cell(cell)

    def draw_grid_lines(self):
        for i in range(self.size):
            pygame.draw.line(self.window, colors['line'], (0, i * self.cell_size),
                             (self.window_size, i * self.cell_size))
            for j in range(self.size):
                pygame.draw.line(self.window, colors['line'], (j * self.cell_size, 0), (j * self.cell_size,
                                                                                        self.window_size))

    def draw_grid_cell(self, cell):
        pygame.draw.rect(self.window, cell.color, (cell.x, cell.y, cell.size, cell.size))

    def draw_path(self, current):
        while current.parent:
            current.change_color(colors['path'])
            current = current.parent
            self.update_screen()
