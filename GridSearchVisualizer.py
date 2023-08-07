from GridVisualizer import GridVisualizer
import dijkstra_search_visualizer
import a_star_search_visualizer
import dfs_search_visualizer
import bfs_search_visualizer


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


