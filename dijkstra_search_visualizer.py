from colors import colors
import heapq


def search(grid_visualizer, start, goal):
    distance = {cell: float('inf') for row in grid_visualizer.grid for cell in row}
    distance[start] = 0
    count = 0
    priority_queue = [(distance[start], count, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_cell = heapq.heappop(priority_queue)[2]

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

            new_distance = distance[current_cell] + 1

            if new_distance < distance[neighbour]:
                neighbour.parent = current_cell
                distance[neighbour] = new_distance
                count += 1
                heapq.heappush(priority_queue, (new_distance, count, neighbour))
                neighbour.change_color(colors['active'])

        grid_visualizer.update_screen()
        if current_cell != start:
            current_cell.change_color(colors['visited'])

    return False
