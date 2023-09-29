import random

def initialize_grid(grid_size, num_carrots, num_holes):
    grid = [['-' for _ in range(grid_size)] for _ in range(grid_size)]
    rabbit_x, rabbit_y = random.randint(
        0, grid_size - 1), random.randint(0, grid_size - 1)
    grid[rabbit_x][rabbit_y] = 'r'

    carrots = []
    for _ in range(num_carrots):
        carrot_x, carrot_y = random.randint(
            0, grid_size - 1), random.randint(0, grid_size - 1)
        while grid[carrot_x][carrot_y] != '-':
            carrot_x, carrot_y = random.randint(
                0, grid_size - 1), random.randint(0, grid_size - 1)
        grid[carrot_x][carrot_y] = 'C'
        carrots.append((carrot_x, carrot_y))

    holes = []
    for _ in range(num_holes):
        hole_x, hole_y = random.randint(
            0, grid_size - 1), random.randint(0, grid_size - 1)
        while grid[hole_x][hole_y] != '-':
            hole_x, hole_y = random.randint(
                0, grid_size - 1), random.randint(0, grid_size - 1)
        grid[hole_x][hole_y] = 'O'
        holes.append((hole_x, hole_y))

    return grid, rabbit_x, rabbit_y, carrots, holes