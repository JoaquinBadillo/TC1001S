"""Snake, classic arcade game.

Source: http://www.grantjenks.com/docs/freegames/
Install module with:
pip install freegames

Collaborators:
Joaquín Badillo
Pablo Banzo
Shaul Zayat
"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    """ Change snake direction. """
    aim.x = x
    aim.y = y

def inside(head):
    """ Return True if head inside boundaries. """
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """ Move snake forward one segment. """
    head = snake[-1].copy()
    head.move(aim)

    if  head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    
    if head.x < -200:
        head.x = 190

    if head.y > 190:
        head.y = -200

    if head.x > 190:
        head.x = -200
    
    if head.y < -200:
        head.y = 190
        snake.append(head)    

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
move()
done()
