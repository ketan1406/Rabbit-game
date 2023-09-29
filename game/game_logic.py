import curses
from game.grid import initialize_grid
from game.movement import move_direction, pick, drop, jump
from game.find_shortest_solution import find_shortest_carrot_path, find_shortest_hole_path


def play_game(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(0)
    stdscr.addstr("Enter grid size (e.g., 5 for a 5x5 grid):\n")
    stdscr.refresh()
    grid_size = int(stdscr.getstr().decode())
    stdscr.addstr("Enter the number of carrots:\n ")
    stdscr.refresh()
    num_carrots = int(stdscr.getstr().decode())
    stdscr.addstr("Enter the number of rabbit holes: \n")
    stdscr.refresh()
    num_holes = int(stdscr.getstr().decode())

    grid, rabbit_x, rabbit_y, carrots, holes = initialize_grid(
        grid_size, num_carrots, num_holes)
    carrot_held = False
    count = 0
    while True:
        stdscr.clear()
        stdscr.addstr(
            0, 0, f"Grid Size: {grid_size}  Carrots: {num_carrots} Holes: {num_holes}")
        stdscr.addstr(
            1, 0, "Controls: w=up, s=down, a=left, d=right, q=up-left, e=up-right, z=down-left, c=down-right, j=jump, p=pick/drop carrot, g=Solution Generator, t=quit")
        stdscr.addstr(2, 0, f"Number of Steps: {count}")

        for i in range(grid_size):
            for j in range(grid_size):
                stdscr.addstr(i + 3, j * 2, grid[i][j])
        move = stdscr.getkey().lower()

        if move == 't':
            break
        elif move in ['w', 's', 'a', 'd', 'q', 'e', 'z', 'c']:
            grid, rabbit_x, rabbit_y = move_direction(
                move, grid, rabbit_x, rabbit_y, carrot_held)
            count +=1
        elif move == 'j':
            grid, rabbit_x, rabbit_y = jump(grid, rabbit_x, rabbit_y, holes)
        elif move == 'p':
            if not (carrot_held):
                grid, rabbit_x, rabbit_y, carrot_held = pick(
                    grid, rabbit_x, rabbit_y, carrots, carrot_held)
            else:
                grid, rabbit_x, rabbit_y, carrot_held = drop(
                    grid, rabbit_x, rabbit_y, holes, carrot_held)
                if carrots == []:
                    break
        elif move == 'g':
            if carrot_held:
                # If the rabbit is carrying a carrot, try to find the shortest path to a hole
                hole_x, hole_y, solution = find_shortest_hole_path(grid, rabbit_x, rabbit_y, holes)
                if solution:
                    for x, y in solution:
                        stdscr.clear()
                        grid[x][y] = 'R'
                        if grid[rabbit_x][rabbit_y] == 'R':
                            grid[rabbit_x][rabbit_y] = '-'
                        count += 1
                        stdscr.addstr(
                            0, 0, f"Grid Size: {grid_size}  Carrots: {num_carrots} Holes: {num_holes}")
                        stdscr.addstr(
                            1, 0, "Controls: w=up, s=down, a=left, d=right, q=up-left, e=up-right, z=down-left, c=down-right, j=jump, p=pick/drop carrot, g=Solution Generator, t=quit")
                        stdscr.addstr(
                            2, 0, f"Number of Steps: {count}")
                        for i in range(grid_size):
                            for j in range(grid_size):
                                stdscr.addstr(i + 3, j * 2, grid[i][j])
                        stdscr.refresh()
                        curses.napms(500)  # Pause for 500 milliseconds
                        grid[rabbit_x][rabbit_y] = '-'
                        grid[x][y] = 'R'
                        rabbit_x, rabbit_y = x, y
                    grid[x][y] = 'r'
                    grid[hole_x][hole_y] = 'o'
                    carrot_held = False
                if carrots == []:
                    break
            else:
                solution = find_shortest_carrot_path(grid, rabbit_x, rabbit_y, carrots)
                if solution:
                    for x, y in solution:
                        stdscr.clear()
                        grid[x][y] = 'r'
                        if grid[rabbit_x][rabbit_y] == 'r':
                            grid[rabbit_x][rabbit_y] = '-'
                        count += 1
                        stdscr.addstr(
                            0, 0, f"Grid Size: {grid_size}  Carrots: {num_carrots} Holes: {num_holes}")
                        stdscr.addstr(
                            1, 0, "Controls: w=up, s=down, a=left, d=right, q=up-left, e=up-right, z=down-left, c=down-right, j=jump, p=pick/drop carrot, g=Solution Generator, t=quit")
                        stdscr.addstr(
                            2, 0, f"Number of Steps: {count}")
                        for i in range(grid_size):
                            for j in range(grid_size):
                                stdscr.addstr(i + 3, j * 2, grid[i][j])
                        stdscr.refresh()
                        curses.napms(500)  # Pause for 500 milliseconds
                        grid[rabbit_x][rabbit_y] = '-'
                        grid[x][y] = 'r'
                        rabbit_x, rabbit_y = x, y
                    grid[x][y] = 'R'  # Reset the rabbit position
                    carrot_held = True
                    carrots.remove((x, y))

    if grid_size + 4 < curses.LINES and 5 < curses.COLS:
        stdscr.addstr(grid_size + 4, 5, f"Game Over! Press any key to exit. The number of steps taken were: {count}")
        curses.napms(10000)
        stdscr.refresh()
        stdscr.getch()