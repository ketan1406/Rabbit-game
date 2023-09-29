import curses
import random
from game.game_logic import play_game
from game.grid import initialize_grid
from game.movement import move_direction, pick, drop, jump
from game.find_shortest_solution import find_shortest_carrot_path, find_shortest_hole_path
from collections import deque

if __name__ == "__main__":
    curses.wrapper(play_game)