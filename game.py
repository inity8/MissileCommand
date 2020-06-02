from math import degrees, acos
from turtle import Screen, Turtle
import os
from random import randint

BASE_PATH = os.path.dirname(__file__)

# coordinates of the base
BASE_X, BASE_Y = 0, -300

# create game window
window = Screen()
window.setup(1200 + 3, 800 + 3)
window.bgpic(os.path.join(BASE_PATH, 'images', 'background.png'))
window.screensize(1200, 800)
# window.tracer(2)

class Missile(Turtle):
    """The class that creates the rocket object.
     By default, missiles launched from the base are created.
     To create enemy missiles you need to transfer to
     class constructor all parameters:
         x, y - base coordinates (BASE_X and BASE_Y);
         pos_x, pos_y - the initial coordinates of the rocket;
         color = 'red' - sets red color for enemy missiles"""
    def __init__(self, x, y, pos_x=BASE_X, pos_y=BASE_Y, color='white'):
        super().__init__(visible=False)
        self.penup()
        self.speed(0)
        self.color = self.color(color)
        self.target = (x, y)
        self.setpos(pos_x, pos_y)

        self.state = 'launched'
        self.radius = 0


def create_missile(side, x1, y1, x2, y2):
    missile = Turtle(visible=False)
    missile.speed(0)
    if side == 'our':
        missile.color('#d0ea3e')
    elif side == 'enemy':
        missile.color('red')
    missile.penup()
    missile.setpos(x=x1, y=y1)
    missile.pendown()
    heading = missile.towards(x2, y2)
    missile.setheading(heading)
    missile.showturtle()
    info = {'missile': missile,
            'target': [x2, y2],
            'state': 'launched',
            'radius': 0,
            'side': side}
    missiles.append(info)


def fire_our_missile(x, y):
    create_missile(side='our', x1=BASE_X, y1=BASE_Y, x2=x, y2=y)


def fire_enemy_missile():
    half_width = divmod(window.window_width(), 2)[0]
    half_height = divmod(window.window_height(), 2)[0]
    x1 = randint(-half_width, half_width)
    y1 = half_height
    create_missile(side='enemy', x1=x1, y1=y1, x2=BASE_X, y2=BASE_Y)


missiles = []

window.onclick(fire_our_missile)
for i in range(randint(2, 8)):
    fire_enemy_missile()


while True:
    window.update()

    for info in missiles:
        state = info['state']
        missile = info['missile']
        if state == 'launched':
            missile.forward(4)
            target = info['target']
            if missile.distance(x=target[0], y=target[1]) < 20:
                info['state'] = 'explode'
                missile.shape('circle')
        elif state == 'explode':
            info['radius'] += 1
            if info['radius'] > 5:
                missile.clear()
                missile.hideturtle()
                info['state'] = 'dead'
            else:
                missile.shapesize(info['radius'])

    dead_missiles = [info for info in missiles if info['state'] == 'dead']
    for dead in dead_missiles:
        missiles.remove(dead)

