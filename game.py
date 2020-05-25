# noinspection PyUnresolvedReferences
import tkinter
import turtle
import random

window = turtle.Screen()
window.setup(600 + 3, 400 + 3)
# window.bgcolor('#85869E')
window.bgpic('images/background.png')
window.screensize(1200, 800)

def airplane(y):
    pen = turtle.Turtle()
    if y < 0:
        pen.color('#ea483c')
    else:
        pen.color('#d0ea3e')
    # pen.shape('triangle')
    for current_x in [-100, 0, 100]:
        pen.penup()
        pen.setpos(x=current_x, y=y)
        pen.pendown()
        # pen.circle(radius=50)
        pen.forward(100)
        pen.circle(radius=random.randint(40, 80))

airplane(y=100)
airplane(y=-100)

window.mainloop()


