import turtle
import time
turtle.setup(800,800,None,None)
turtle.speed(4)
turtle.up()
turtle.pensize(2)
def coord_draw(x,y,l):
    turtle.pensize(2)
    turtle.goto(x-l/2,y)
    turtle.down()
    time.sleep(1)
    turtle.goto(x+1-l/2,y)
    turtle.fd(l-1)
    turtle.up()
    turtle.home()
    turtle.rt(90)
    turtle.fd(l/2)
    turtle.rt(180)
    turtle.down()
    turtle.fd(l)
    turtle.up()
    turtle.home()
    time.sleep(1)
coord_draw(0, 0, 500)