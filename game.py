# noinspection PyUnresolvedReferences
import tkinter
import turtle

window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.bgpic('images/background.png')
window.screensize(1200, 800)

BASE_X, BASE_Y = 0, -300

missile = turtle.Turtle()
missile.color('#d0ea3e')
missile.penup()
missile.setpos(x=BASE_X, y=BASE_Y)
missile.pendown()
missile.setheading(60)
missile.forward(500)
missile.shape('circle')
missile.shapesize(2)
missile.shapesize(3)
missile.shapesize(4)
# missile.shapesize(5)
missile.clear()
missile.hideturtle()

window.onclick()

window.mainloop()


