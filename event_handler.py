from Grid import pygame
from Grid import GridSearchVisualizer
from colors import colors

START_CELL = None
GOAL_CELL = None
GRID_SEARCH_VISUALIZER = None


def get_clicked_mouse_position(mouse_position, rows, screen_size):
    square_size = screen_size // rows
    x, y = mouse_position
    row = y // square_size
    col = x // square_size
    return row, col


def handle_keydown(event, grid_search_visualizer):
    global START_CELL, GOAL_CELL

    if event.key == pygame.K_a and START_CELL and GOAL_CELL:
        grid_search_visualizer.a_star_search(START_CELL, GOAL_CELL)
        return

    if event.key == pygame.K_b and START_CELL and GOAL_CELL:
        grid_search_visualizer.bfs(START_CELL, GOAL_CELL)
        return

    if event.key == pygame.K_d and START_CELL and GOAL_CELL:
        grid_search_visualizer.dijkstra(START_CELL, GOAL_CELL)
        return

    if event.key == pygame.K_SPACE and START_CELL and GOAL_CELL:
        grid_search_visualizer.dfs(START_CELL, GOAL_CELL)
        return

    if event.key == pygame.K_c:
        init_global_variables()


def init_global_variables():
    global START_CELL, GOAL_CELL, GRID_SEARCH_VISUALIZER
    START_CELL, GOAL_CELL = None, None
    GRID_SEARCH_VISUALIZER = GridSearchVisualizer(GRID_SEARCH_VISUALIZER.size, GRID_SEARCH_VISUALIZER.window_size,
                                                  GRID_SEARCH_VISUALIZER.window)


def is_wall(current_cell):
    return current_cell != START_CELL and current_cell != GOAL_CELL


def is_start(current_cell):
    return not START_CELL and current_cell != GOAL_CELL


def is_goal(current_cell):
    return not GOAL_CELL and current_cell != START_CELL


def handle_left_mouse_press(grid_search_visualizer):
    row, col = get_clicked_mouse_position(pygame.mouse.get_pos(), grid_search_visualizer.size,
                                          grid_search_visualizer.window_size)

    global START_CELL, GOAL_CELL
    current_cell = grid_search_visualizer.get_cell(row, col)

    if is_start(current_cell):
        START_CELL = current_cell
        START_CELL.change_color(colors['start'])

    if is_goal(current_cell):
        GOAL_CELL = current_cell
        GOAL_CELL.change_color(colors['goal'])

    if is_wall(current_cell):
        current_cell.change_color(colors['wall'])


def handle_right_mouse_press(grid_search_visualizer):
    row, col = get_clicked_mouse_position(pygame.mouse.get_pos(), grid_search_visualizer.size,
                                          grid_search_visualizer.window_size)
    current_cell = grid_search_visualizer.get_cell(row, col)
    current_cell.change_color(colors['default'])

    global START_CELL, GOAL_CELL
    if current_cell == START_CELL:
        START_CELL = None
    if current_cell == GOAL_CELL:
        GOAL_CELL = None


def handle(event, grid_search_visualizer):
    global START_CELL, GOAL_CELL, GRID_SEARCH_VISUALIZER
    GRID_SEARCH_VISUALIZER = grid_search_visualizer

    if event.type == pygame.KEYDOWN:
        grid_search_visualizer.update_cells_neighbours()
        handle_keydown(event, grid_search_visualizer)

    if pygame.mouse.get_pressed()[0]:
        handle_left_mouse_press(grid_search_visualizer)

    if pygame.mouse.get_pressed()[2]:
        handle_left_mouse_press(grid_search_visualizer)
