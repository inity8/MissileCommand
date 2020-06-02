import math
import turtle

window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.bgpic('images/background.png')
window.screensize(1200, 800)
# window.tracer(2)

BASE_X, BASE_Y = 0, -300
ENEMY_COUNT = 5


def create_missile(color, x, y, x2, y2):
    missile = turtle.Turtle(visible=True)
    missile.speed(0)
    missile.color(color)
    missile.penup()
    missile.setpos(x=x, y=y)
    missile.pendown()
    heading = calc_heading(x2, y2)
    missile.setheading(heading)
    missile.showturtle()
    info = {'missile': missile,
            'target': [x2, y2],
            'state': 'launched',
            'radius': 0}
    return info


def calc_heading(x1, y1, x2, y2):
    dx = (x2-x1)
    dy = (y2-y1)
    length = (dx ** 2 + dy ** 2) ** 0.5
    cos_alpha = dx / length
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    if dy < 0:
        alpha = - alpha
    return alpha


def fire_missile(x, y):
    info = create_missile(color='wite', x=BASE_X, y=BASE_Y, x2=x, y2 =y)
    our_missiles.append(info)


def fire_enemy_missile():
    pass


def move_missiles(missiles):
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


window.onclick(fire_missile)
our_missiles = []
enemy_missiles = []


while True:
    window.update()
    if len(enemy_missiles) < ENEMY_COUNT:
        fire_enemy_missile()
    move_missiles(missiles=our_missiles)
    move_missiles(missiles=enemy_missiles)



