# noinspection PyUnresolvedReferences
import tkinter
import turtle

window = turtle.Screen()
window.bgcolor('#85869E')
pen = turtle.Turtle()
pen.color('#25415B')
for current_x in [-400, -200, 0, 200, 400]:
    pen.setpos(x=current_x, y=0)
    pen.circle(radius=100)
    pen.forward(100)
    pen.circle(radius=100)

window.mainloop()





window.mainloop()
