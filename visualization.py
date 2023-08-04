import pygame 
from colors import colors 
from Grid import *

SIZE = 800
WINDOW = pygame.display.set_mode((SIZE , SIZE))
pygame.display.set_caption("Graph algorithms visualization")

def get_clicked_pos(mouse_pos , rows , screen_size):
    square_size = screen_size // rows
    x , y = mouse_pos
    row = y // square_size
    col = x // square_size
    return row, col

def main(window , screen_size):
    ROWS = 25
    running = True 
    start_cell = None 
    goal_cell = None
    grid_search_visualizer = GridSearchVisualizer(ROWS , screen_size , window)

    while running:
        grid_search_visualizer.update_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                row , col = get_clicked_pos(mouse_pos , ROWS , screen_size)
                current_cell = grid_search_visualizer.get_cell(row,col)

                if not start_cell and current_cell != goal_cell:
                    start_cell = current_cell
                    start_cell.change_color(colors['start'])

                elif not goal_cell and current_cell != start_cell:
                    goal_cell = current_cell
                    goal_cell.change_color(colors['goal'])
                    
                elif  current_cell != start_cell and current_cell != goal_cell:
                    current_cell.change_color(colors['wall'])
                
            elif pygame.mouse.get_pressed()[2]:
                mouse_pos = pygame.mouse.get_pos()
                row , col = get_clicked_pos(mouse_pos , ROWS , screen_size)
                current_cell = grid_search_visualizer.get_cell(row,col)
                current_cell.change_color(colors['default'])
                if current_cell == start_cell:
                    start_cell = None 
                if current_cell == goal_cell:
                    goal_cell = None
            
            if event.type == pygame.KEYDOWN:
                grid_search_visualizer.update_cells_neighbours()
                if event.key == pygame.K_a and start_cell and goal_cell:
                    grid_search_visualizer.a_star_search(start_cell , goal_cell)

                if event.key == pygame.K_b and start_cell and goal_cell:
                    grid_search_visualizer.bfs(start_cell , goal_cell)

                if event.key == pygame.K_d and start_cell and goal_cell:
                    grid_search_visualizer.dijkstra(start_cell , goal_cell)

                if event.key == pygame.K_SPACE and start_cell and goal_cell:
                    grid_search_visualizer.dfs(start_cell , goal_cell)

                if event.key == pygame.K_c:
                    start_cell = None 
                    goal_cell = None
                    grid_search_visualizer = GridSearchVisualizer(ROWS , screen_size , window)
            
    pygame.quit()

main(WINDOW , SIZE)