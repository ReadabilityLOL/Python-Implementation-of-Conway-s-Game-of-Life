# Conway's game of life implementation

This is my python implementation of Conway's game of life. More about it on [my website](https://glitched.tech/gameoflife/).

## What is Conway's game of life?

Conway's game of life is a cellular automaton, which is just a grid with cells that are on or off, with different rules determining which cells turn on and off each turn. Though it's called the Game of Life, it's not really a game, as it has no objective and no real player interaction except for the starting setup. The game of life itself follows a few simple rules for each turn about which cells become living (on), and which become dead (off).

1. If a living cell has 2 or 3 living neighbors, it remains alive.
2. If it has 0-1 or 4-8 living neighbors, it dies.
3. If a dead cell has exactly 3 living neighbors, it comes to life.

Despite the fact that these are the only rules, the game itself can become surprisingly complex. It is, for example, Turing Complete, meaning that any computation possible to create on a computer is theoretically possible in Conway's Game of Life. For an example of something awesome you can do in the Game of Life, check out [Life in Life](https://www.youtube.com/watch?v=xP5-iIeKXE8).

## My project

My project is a simple implementation of Conway's Game of Life made in Python, HTML, and CSS, with pyscript used to connect the Python to the HTML and CSS. I used Python because I originally made it a CLI, and because Javascript is scary. It's a bit more limited than the actual game of life, due to problems like it not actually having an infinite board. You can visit the project at [gameoflife.glitched.tech](https://gameoflife.glitched.tech). After the project loads, the user is provided with a blank grid, which can be clicked to toggle between dead and living cells. There are also three buttons available at the bottom, which allow for the ability to randomize the board, reset it, or advance to the next turn, which evaluates all the cells and sets them as living or dead based on the aforementioned rules.
