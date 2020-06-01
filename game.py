# noinspection PyUnresolvedReferences
import math
import tkinter
import turtle

window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.bgpic('images/background.png')
window.screensize(1200, 800)
# window.tracer(2)

BASE_X, BASE_Y = 0, -300


def calc_heading(x1, y1, x2, y2):
    dx = (x2-x1)
    dy = y2 - y1
    length = (dx ** 2 + dy ** 2) ** 0.5
    cos_alpha = dx / length
    alpha = math.degrees(math.acos(cos_alpha))
    if dy < 0:
        alpha = -alpha
    return alpha


def fire_missile(x, y):
    # global missile
    missile = turtle.Turtle(visible=False)
    missile.speed(0)
    missile.color('#d0ea3e')
    missile.penup()
    missile.setpos(x=BASE_X, y=BASE_Y)
    missile.pendown()
    heading = calc_heading(x1=BASE_X, y1=BASE_Y, x2=x, y2=y)
    missile.setheading(heading)
    missile.showturtle()
    our_missiles.append(missile)
    our_missiles_target.append([x, y])
    our_missiles_states.append('launched')
    our_missiles_radius.append(0)


window.onclick(fire_missile)
our_missiles = []
our_missiles_target = []
our_missiles_states = []
our_missiles_radius = []


while True:
    window.update()

    for num, missile in enumerate(our_missiles):
        if our_missiles_states[num] == 'launched':
            missile.forward(4)
            target = our_missiles_target[num]
            if missile.distance(x=target[0], y=target[1] < 20):
                our_missiles_states[num] = 'explode'
                missile.shape('circle')
        elif our_missiles_states[num] == 'explode':
            our_missiles_radius[num] += 1
            missile.shapesize(our_missiles_radius[num])
            # missile.shapesize(2)
            # missile.shapesize(3)
            # missile.shapesize(4)
            # missile.shapesize(5)


