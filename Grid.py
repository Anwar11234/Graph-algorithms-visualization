import pygame 
from Cell import Cell
from colors import colors 
import heapq
from collections import deque

class Grid:
    def __init__(self , size , window_size):
        self.grid = []
        self.window_size = window_size 
        self.size = size
        self.cell_size = window_size // self.size
        self.build()

    def build(self):
        for i in range(self.size):
            self.grid.append([])
            for j in range(self.size):
                self.grid[i].append(Cell(i , j , self.cell_size))
        
    def get_cell(self , row,col):
        return self.grid[row][col]
    
    def update_cells_neighbours(self):
        for row in self.grid:
            for cell in row:
                cell.update_neighbours(self.grid)

class GridVisualizer(Grid):
    def __init__(self , size , window_size , window):
        super().__init__(size , window_size)
        self.window = window
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

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
            pygame.draw.line(self.window , colors['line'] , (0 , i * self.cell_size) , (self.window_size , i * self.cell_size))
            for j in range(self.size):
                pygame.draw.line(self.window , colors['line'] , (j * self.cell_size , 0) , (j * self.cell_size , self.window_size)) 

    def draw_path(self , current):
        while current.parent:
            current.change_color(colors['path'])
            current = current.parent
            self.update_screen()

class GridSearchVisualizer(GridVisualizer):
    def __init__(self, size , window_size , window):
        super().__init__(size, window_size , window)

    def dijkstra(self, start, goal):
        distance = {cell: float('inf') for row in self.grid for cell in row}
        distance[start] = 0
        count = 0 
        pq = [(distance[start],count,start)]
        heapq.heapify(pq)

        while pq:
            self.handle_events()

            current_cell = heapq.heappop(pq)[2]

            if current_cell.is_wall() or current_cell.visited:
                continue

            current_cell.visited = True

            if current_cell == goal:
                self.draw_path(goal)
                goal.change_color(colors['goal'])
                return True

            for neighbour in current_cell.get_neighbours():
                if neighbour.is_wall() or neighbour.visited:
                    continue

                new_distance = distance[current_cell] + 1

                if new_distance < distance[neighbour]:
                    neighbour.parent = current_cell
                    distance[neighbour] = new_distance
                    count += 1
                    heapq.heappush(pq, (new_distance,count, neighbour))
                    neighbour.change_color(colors['active'])

            self.update_screen()
            if current_cell != start:
                current_cell.change_color(colors['visited'])

        return False
    
    def a_star_search(self  , start , goal):
        count = 0
        start.g = 0
        start.h = start.calculate_heuristic(goal)
        start.f = start.g + start.h
        pq = [(start.f , count , start)]
        heapq.heapify(pq)

        while pq:
            self.handle_events()
            
            current_cell = heapq.heappop(pq)[2]

            if current_cell.is_wall() or current_cell.visited:
                continue

            current_cell.visited = True

            if current_cell == goal:
                self.draw_path(goal)
                goal.change_color(colors['goal'])
                return True            
            
            for neighbour in current_cell.get_neighbours():

                if neighbour.is_wall() or neighbour.visited:
                    continue

                new_distance = current_cell.g + 1

                if new_distance < neighbour.g:
                    neighbour.update_cost(current_cell , new_distance)
                    count += 1
                    neighbour.h = neighbour.calculate_heuristic(goal)
                    neighbour.f = neighbour.g + neighbour.h
                    heapq.heappush(pq ,  (neighbour.f , count , neighbour))
                    neighbour.change_color(colors['active'])

            self.update_screen()
            if current_cell != start:
                current_cell.change_color(colors['visited'])
            
        return False    
        
    def dfs(self , start , goal):
        stack = [start]
        while stack:
            self.handle_events()

            current_cell = stack.pop()
            
            if current_cell.is_wall() or current_cell.visited:
                continue

            current_cell.visited = True

            if current_cell == goal:
                self.draw_path(goal)
                goal.change_color(colors['goal'])
                return True        
            
            for neighbour in current_cell.get_neighbours():
                if neighbour.is_wall() or neighbour.visited:
                    continue
                
                neighbour.parent = current_cell
                stack.append(neighbour)
                neighbour.change_color(colors['active'])
            
            self.update_screen()
            if current_cell != start:
                current_cell.change_color(colors['visited'])
            
        return False

    def bfs(self  , start , goal):
        q = deque([start])
        while q:
            self.handle_events()

            current_cell = q.popleft()

            if current_cell.is_wall() or current_cell.visited:
                continue

            current_cell.visited = True
            if current_cell == goal:
                self.draw_path(goal)
                goal.change_color(colors['goal'])
                return True        
                        
            for neighbour in current_cell.get_neighbours():
                if neighbour.is_wall() or neighbour.visited:
                    continue
                neighbour.parent = current_cell
                q.append(neighbour)
                neighbour.change_color(colors['active'])
            
            self.update_screen()
            if current_cell != start:
                current_cell.change_color(colors['visited'])
            
        return False