import event_handler
from GridSearchVisualizer import GridSearchVisualizer
import pygame


class GraphAlgorithmsVisualizer:
    def __init__(self, screen_size, visualization_caption):
        self.screen_size = screen_size
        self.visualization_caption = visualization_caption
        self.rows = 25
        self.window = pygame.display.set_mode((screen_size, screen_size))
        self.grid_search_visualizer = GridSearchVisualizer(self.rows, screen_size, self.window)

    def visualize(self):
        pygame.display.set_caption(self.visualization_caption)
        while True:
            self.grid_search_visualizer.update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                event_handler.handle(event, self.grid_search_visualizer)
