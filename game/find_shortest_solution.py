from collections import deque

def find_shortest_carrot_path(grid, rabbit_x, rabbit_y, carrots):
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    queue = deque([(rabbit_x, rabbit_y, [])])

    while queue:
        x, y, path = queue.popleft()
        visited[x][y] = True

        if grid[x][y] == 'C':
            return path

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and not visited[new_x][new_y]:
                new_path = path + [(new_x, new_y)]

                queue.append((new_x, new_y, new_path))
                visited[new_x][new_y] = True

    return None

def find_shortest_hole_path(grid, rabbit_x, rabbit_y, holes):
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    queue = deque([(rabbit_x, rabbit_y, [])])

    while queue:
        x, y, path = queue.popleft()
        visited[x][y] = True

        # Check if the rabbit is next to a hole horizontally or vertically
        for hole_x, hole_y in holes:
            if (x == hole_x and abs(y - hole_y) == 1) or (y == hole_y and abs(x - hole_x) == 1):
                holes.remove((hole_x,hole_y))
                return hole_x, hole_y, path

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and not visited[new_x][new_y]:
                new_path = path + [(new_x, new_y)]

                queue.append((new_x, new_y, new_path))
                visited[new_x][new_y] = True

    return None