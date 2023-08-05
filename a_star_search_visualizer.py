from colors import colors
import heapq


def search(grid_visualizer, start, goal):
    count = 0
    start.g = 0
    start.h = start.calculate_heuristic(goal)
    start.f = start.g + start.h
    pq = [(start.f, count, start)]
    heapq.heapify(pq)

    while pq:
        current_cell = heapq.heappop(pq)[2]

        if current_cell.is_wall() or current_cell.visited:
            continue

        current_cell.visited = True

        if current_cell == goal:
            grid_visualizer.draw_path(goal)
            goal.change_color(colors['goal'])
            return True

        for neighbour in current_cell.get_neighbours():

            if neighbour.is_wall() or neighbour.visited:
                continue

            new_distance = current_cell.g + 1

            if new_distance < neighbour.g:
                neighbour.update_cost(current_cell, new_distance)
                count += 1
                neighbour.h = neighbour.calculate_heuristic(goal)
                neighbour.f = neighbour.g + neighbour.h
                heapq.heappush(pq, (neighbour.f, count, neighbour))
                neighbour.change_color(colors['active'])

        grid_visualizer.update_screen()
        if current_cell != start:
            current_cell.change_color(colors['visited'])

    return False
