"""Memory, puzzle game of number pairs.

Source: http://www.grantjenks.com/docs/freegames/
Install module with:
pip install freegames

Collaborators:
Joaquín Badillo
Pablo Banzo
Shaul Zayat

"""

from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(8)) * 2
state = {'mark': None}
hide = [True] * 16

def square(x, y):
    """ Draw white square with black outline at (x, y). """
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(100)
        left(90)
    end_fill()

def index(x, y):
    """ Convert (x, y) coordinates to tiles index. """
    return int((x + 200) // 100 + ((y + 200) // 100) * 4)

def xy(count):
    """ Convert tiles count to (x, y) coordinates. """
    return (count % 4) * 100 - 200, (count // 4) * 100 - 200

def tap(x, y):
    """ Update mark and hidden tiles based on tap. """
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    """ Draw image and tiles. """
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
