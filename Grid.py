from Cell import Cell


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
