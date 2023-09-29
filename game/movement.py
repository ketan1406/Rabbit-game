def move_direction(move, grid, rabbit_x, rabbit_y, carrot_held):
    new_x, new_y = rabbit_x, rabbit_y

    if move == 'w':    # Up
        new_x -= 1
    elif move == 's':  # Down
        new_x += 1
    elif move == 'a':  # Left
        new_y -= 1
    elif move == 'd':  # Right
        new_y += 1
    elif move == 'q':  # Diagonal: up-left
        new_x -= 1
        new_y -= 1
    elif move == 'e':  # Diagonal: up-right
        new_x -= 1
        new_y += 1
    elif move == 'z':  # Diagonal: down-left
        new_x += 1
        new_y -= 1
    elif move == 'c':  # Diagonal: down-right
        new_x += 1
        new_y += 1

    # Check if the new position is within the grid boundaries
    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
        if carrot_held:
            if grid[new_x][new_y] == '-':
                grid[new_x][new_y] = 'R'  # Update the new position
                grid[rabbit_x][rabbit_y] = '-'  # Clear the old position
                rabbit_x, rabbit_y = new_x, new_y
        else:
            if grid[new_x][new_y] == '-':
                grid[new_x][new_y] = 'r'  # Update the new position
                grid[rabbit_x][rabbit_y] = '-'  # Clear the old position
                rabbit_x, rabbit_y = new_x, new_y

    return grid, rabbit_x, rabbit_y


def pick(grid, rabbit_x, rabbit_y, carrots, carrot_held):
    new_x, new_y = rabbit_x, rabbit_y

    if carrot_held == False:
        for carrot_x, carrot_y in carrots:
            x_diff = abs(rabbit_x - carrot_x)
            y_diff = abs(rabbit_y - carrot_y)

            if x_diff + y_diff == 1:
                new_x, new_y = carrot_x, carrot_y
                carrots.remove((carrot_x, carrot_y))
                carrot_held = True
                break

    grid[new_x][new_y] = 'R' if carrot_held else 'r'
    grid[rabbit_x][rabbit_y] = '-' if carrot_held else 'r'

    return grid, new_x, new_y, carrot_held


def drop(grid, rabbit_x, rabbit_y, holes, carrot_held):
    new_x, new_y = rabbit_x, rabbit_y

    if carrot_held:
        for hole_x, hole_y in holes:
            if rabbit_x == hole_x and abs(rabbit_y - hole_y) == 1:
                # Check if the rabbit is next to a hole horizontally
                if grid[rabbit_x][rabbit_y] == 'R' and grid[hole_x][hole_y] == 'O':
                    grid[rabbit_x][rabbit_y] = 'r'
                    grid[hole_x][hole_y] = 'o'  # Change 'O' to 'o'
                    holes.remove((hole_x, hole_y))
                    carrot_held = False
                    break
            elif rabbit_y == hole_y and abs(rabbit_x - hole_x) == 1:
                # Check if the rabbit is next to a hole vertically
                if grid[rabbit_x][rabbit_y] == 'R' and grid[hole_x][hole_y] == 'O':
                    grid[rabbit_x][rabbit_y] = 'r'
                    grid[hole_x][hole_y] = 'o'  # Change 'O' to 'o'
                    holes.remove((hole_x, hole_y))
                    carrot_held = False
                    break

    return grid, rabbit_x, rabbit_y, carrot_held


def jump(grid, rabbit_x, rabbit_y, holes, carrot_held):
    new_x, new_y = rabbit_x, rabbit_y

    for hole_x, hole_y in holes:
        if rabbit_x == hole_x and 0 <= rabbit_y < len(grid[0]):
            if rabbit_y < hole_y and rabbit_y == hole_y - 1 and grid[hole_x][hole_y + 1] == '-':
                new_y = hole_y + 1
            elif rabbit_y > hole_y and rabbit_y == hole_y + 1 and grid[hole_x][hole_y - 1] == '-':
                new_y = hole_y - 1
        elif rabbit_y == hole_y and 0 <= rabbit_x < len(grid[0]):
            if rabbit_x < hole_x and rabbit_x == hole_x - 1 and grid[hole_x + 1][hole_y] == '-':
                new_x = hole_x + 1
            elif rabbit_x > hole_x and rabbit_x == hole_x + 1 and grid[hole_x - 1][hole_y] == '-':
                new_x = hole_x - 1

    grid[rabbit_x][rabbit_y] = '-'
    if carrot_held:
        grid[new_x][new_y] = 'R'
    else:
        grid[new_x][new_y] = 'r'

    return grid, new_x, new_y, carrot_held