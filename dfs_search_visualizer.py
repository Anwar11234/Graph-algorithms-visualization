from colors import colors


def search(grid_visualizer, start, goal):
    stack = [start]
    while stack:
        current_cell = stack.pop()

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

            neighbour.parent = current_cell
            stack.append(neighbour)
            neighbour.change_color(colors['active'])

        grid_visualizer.update_screen()
        if current_cell != start:
            current_cell.change_color(colors['visited'])

    return False
