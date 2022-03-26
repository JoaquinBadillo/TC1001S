# TC1001S 💻🔧

Source code for the Computer Tools course challenges, imparted by Gil Echeverria.

## Authors:

Joaquín Badillo (ITC - 2nd semester)

Pablo Banzo Prida (ITC - 2nd semester)

Shaul Zayat (ITC - 2nd semester)

The original games in this repository were obtained from [Gil&#39;s Repository](https://github.com/gilecheverria/TC1001S.100-202211), for which we implemented new features.

## List of games and modifications

* Snake
  * Pablo implemented "A, W, S, D" key response.
  * Joaquín changed the speed of the snake.
  * Shaul made the snake go around the edges.
* Paint
  * Pablo added draw rectangle function.
  * Joaquín added draw triangle function.
  * Shaul added draw circle function.
* Pacman
  * Pablo added two ghosts to the game.
  * Joaquín changed the board.
  * Shaul changed pacman's speed.
* Cannon
  * Pablo added gravity to the targets.
  * Joaquín added scoreboard.
* Memory
  * Shaul decreased the number of tiles to a 4x4 grid.

## Software requirements and installation

### Python

We recommend using Python 3.7 or any future release. You can check your version by executing

`$ python --version`

If the version is lower than 3.x try

`$ python3 --version`

if the version is still lower or if the python3 command is not recognized, it can be installed from their webpage ([click me](https://www.python.org/)), from the microsoft store or using a package manager like apt (debian linux distros).

### Freegames

To install freegames we encourage you to use pip (python's package-management system). Execute

`$ pip --version`

or

`$ pip3 --version`

to check if its already installed. If pip is not installed, download the pip installer from their [webpage](https://bootstrap.pypa.io/get-pip.py), then run the installer

`$ python3 get-pip.py`

Finally install the freegames module:

`$ pip install freegames`
