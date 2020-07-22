
# Conway's Game of Life

## Rules
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction. (Wikipedia: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

![image](https://drive.google.com/uc?export=view&id=1JaQfODd179rshMorxEXSsgX4bXGZGfN6)


## Files

> cell_state.py — this file is responsible for processing information about the cell and its neighbours.

> create.py — this file creates a game field.

>  population_process.py — this file responsible for a population life process.

> main.py — this file launches the game.


## Installation
App requires Python 3+.
### Clone
Clone this repo to your local machine using  `https://github.com/tatiana-cooper/Conway-s-Game-of-Life.git`

### Setup
Windows 10:

For launching app:
```sh
> python main.py
```


## Usage
All usage steps are described dynamically during the program run.

