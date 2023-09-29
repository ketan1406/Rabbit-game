# Rabbit-Game

## Description

Rabbit-Game is a grid-based game created using Python and the `curses` library to refresh the screen view. In this game, you control a rabbit as it navigates a grid, picks up carrots, avoids obstacles, and tries to reach rabbit holes. It's a fun and interactive game that showcases basic game development concepts in Python.

## Table of Contents

- [Installation](#installation)
- [Usage and Game Features](#usage-and-game-features)
  - [Usage](#usage)
  - [Game Features](#game-features)

## Installation

To play Rabbit-Game on your local machine, follow these installation steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ketan1406/Rabbit-Game.git

   ```

2. Navigate to your project directory:

   ```bash
   cd Rabbit-Game
   ```

3. Install the required dependencies using pip install:

```bash
 pip install -r requirements.txt
```

4. Run the game:

   ```bash
   python main.py
   ```

## Usage and Game Features

### Usage

1. **Grid Size**: Enter the desired grid size when prompted, e.g., `5` for a 5x5 grid.

2. **Number of Carrots**: Specify the number of carrots you want in the game.

3. **Number of Rabbit Holes**: Determine the number of rabbit holes on the grid.

4. **Controls**: Use the following controls to navigate the game:

   - **w**: Move the rabbit up.
   - **s**: Move the rabbit down.
   - **a**: Move the rabbit left.
   - **d**: Move the rabbit right.
   - **q**: Move the rabbit diagonally up-left.
   - **e**: Move the rabbit diagonally up-right.
   - **z**: Move the rabbit diagonally down-left.
   - **c**: Move the rabbit diagonally up-right.
   - **j**: Make the rabbit jump to the nearest rabbit hole.
   - **p**: Pick or drop a carrot.
   - **g**: Command the rabbit to execute actions :
     - If carrying a carrot, it seeks the shortest path to a hole.
     - If not carrying a carrot, it finds the shortest path to a carrot.

5. **Quit**: Press `t` to go back to the terminal.

### Game Features

- **Grid Display**: The game grid is displayed on the screen, and you control the rabbit's movements within it.

- **Carrots and Rabbit Holes**: Carrots and rabbit holes are randomly placed on the grid. The rabbit's goal is to collect and drop carrots into the holes.

- **Jump Mechanism**: The rabbit can jump over the nearest rabbit hole if the path is clear.

- **Carrot Handling**: Use the `p` key to pick up or drop carrots. The rabbit can carry one carrot at a time.

- **Goal**: The objective of the game is to collect all the carrots and place them in the rabbit holes. Command the rabbit (`g`) strategically to accomplish this or do it manually. The game ends when the rabbit has put all the carrots into the holes.
