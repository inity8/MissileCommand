# noinspection PyUnresolvedReferences
import math
import tkinter
import turtle

window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.bgpic('images/background.png')
window.screensize(1200, 800)
window.tracer(2)

BASE_X, BASE_Y = 0, -300


def calc_heading(x1, y1, x2, y2):
    dx = (x2-x1)
    dy = (y2-y1)
    length = (dx ** 2 + dy ** 2) ** 0.5
    cos_alpha = dx / length
    alpha = math.degrees(math.acos(cos_alpha))
    return alpha


def fire_missile(x, y):
    # global missile
    missile = turtle.Turtle()
    missile.hideturtle()
    missile.color('#d0ea3e')
    missile.penup()
    missile.setpos(x=BASE_X, y=BASE_Y)
    missile.pendown()
    heading = calc_heading(x1=BASE_X, y1=BASE_Y, x2=x, y2=y)
    missile.setheading(heading)
    missile.showturtle()
    missiles.append(missile)


window.onclick(fire_missile)
missiles = []

while True:
    window.update()

    for missile in missiles:
        missile.forward(4)

