"""Cannon, hitting targets with projectiles.

Source: http://www.grantjenks.com/docs/freegames/
Install module with:
pip install freegames

Collaborators:
Joaquín Badillo
Pablo Banzo
Shaul Zayat
"""

from random import randrange
from turtle import *
from freegames import vector

state = {'score': 0}
writer = Turtle(visible=False)

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    """ Respond to screen tap """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15

def inside(xy):
    """ Return True if xy within screen. """
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """ Draw ball and targets. """
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """ Move ball and targets. """
    """ Generate a new target at random times """
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    """ Move the existing targets """
    for target in targets:
        target.x -= 0.5
        target.y -= 0.3 # Gravity on targets

    """ Move the cannon shot """
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    """ Make a copy of the existing target list before redrawing """
    dupe = targets.copy()
    targets.clear()

    """ Detect if the bullet hits a target """
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            state['score'] += 1
            writer.undo()
            writer.write(state['score'])

    draw()

    """ Detect when a target reaches the left side """
    for target in targets:
        if not inside(target):
            #targets.remove(target)
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
writer.undo()
writer.write(state['score'])
onscreenclick(tap)
move()
done()
