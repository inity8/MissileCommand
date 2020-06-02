from math import degrees, acos
from turtle import Screen, Turtle
import os
from random import randint

BASE_PATH = os.path.dirname(__file__)
BASE_X, BASE_Y = 0, -300
number_enemy_missiles = 10


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


def calc_heading(x2, y2, x1, y1):
    dx = x2 - x1
    dy = y2 - y1
    length = (dx ** 2 + dy ** 2) ** 0.5
    cos_alpha = dx / length
    alpha = degrees(acos(cos_alpha))
    if dy < 0:
        alpha = -alpha
    return alpha


def fire_missile(x, y, pos_x=BASE_X, pos_y=BASE_Y):
    if pos_x != BASE_X:
        missile = Missile(x=BASE_X, y=BASE_Y, pos_x=pos_x, pos_y=pos_y, color='red')
        heading = calc_heading(x1=pos_x, y1=pos_y, x2=BASE_X, y2=BASE_Y)
    else:
        missile = Missile(x, y)
        heading = calc_heading(x1=pos_x, y1=pos_y, x2=x, y2=y)
    missile.pendown()
    missile.setheading(heading)
    missile.showturtle()
    missiles_store.append(missile)


# create game window
window = Screen()
window.setup(1200 + 3, 800 + 3)
window.bgpic(os.path.join(BASE_PATH, 'images', 'background.png'))
window.screensize(1200, 800)
# window.tracer(2)

# storing rocket objects
missiles_store = []

# enemy rocket launch
for i in range(randint(2, number_enemy_missiles + 1)):
    fire_missile(x=BASE_X, y=BASE_Y, pos_x=randint(-600, 600), pos_y=400)

while True:
    window.update()
    window.onclick(fire_missile)

    for missile in missiles_store:
        if missile.state == 'launched':
            missile.forward(4)
            if missile.distance(x=missile.target[0], y=missile.target[1]) < 20:
                missile.state = 'explode'
                missile.shape('circle')
        elif missile.state == 'explode':
            missile.radius += 1
            if missile.radius > 5:
                missile.clear()
                missile.hideturtle()
                missile.state = 'dead'
            else:
                missile.shapesize(missile.radius)

    dead_missiles = [i for i in missiles_store if i.state == 'dead']
    for dead in dead_missiles:
        missiles_store.remove(dead)
