import event_handler
from Grid import GridSearchVisualizer
from Grid import pygame

ROWS = 25


def run_visualization(screen_size, visualization_caption):
    window = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption(visualization_caption)
    grid_search_visualizer = GridSearchVisualizer(ROWS, screen_size, window)

    while True:
        grid_search_visualizer.update_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            event_handler.handle(event, grid_search_visualizer)