import turtle
import math
import random
turtle.speed(0)
turtle.home()
def circ(cl,r): 
    turtle.begin_fill()
    turtle.fillcolor(cl)
    turtle.speed(0)
    turtle.pen(pencolor=cl,pensize="1")
    turtle.pu()
    turtle.rt(90)
    turtle.fd(r)
    turtle.left(90)
    turtle.down()
    turtle.circle(r)
    turtle.end_fill()
    turtle.pu()
    turtle.home()
    turtle.down()
def square(size):
    for i in range(4):
        turtle.fd(size)
        turtle.lt(90)
def big_flower(shade):
    for i in range(13):
        turtle.up()
        turtle.goto(0,0)
        turtle.down()
        turtle.fillcolor(shade)
        turtle.pen(pencolor=shade,pensize="1")
        turtle.begin_fill()
        turtle.circle(300,70)
        turtle.left(110)
        turtle.circle(300,70)
        turtle.end_fill()
        turtle.right(1)
def draw_square(square):
	for i in range(0,2):
		square.forward(100)
		square.right(30)
		square.forward(100)
		square.right(150)


def draw_flower():
	window = turtle.Screen()
	window.bgcolor("white")

	hello = turtle.Turtle()
	hello.speed(0)
	hello.shape("triangle")
    #turtle.pen(pencolor="99FF00",pensize="1")
	hello.color("#99FF00")

	for i in range(0,36):
		draw_square(hello)
		hello.right(10)
turtle.pen(pencolor="#770E13",pensize="1")
circ("#770E13",400)
turtle.pen(pencolor="#E67B47",pensize="1")
circ("#E67B47",390)
turtle.pen(pencolor="#ECE19F",pensize="1")
circ("#ECE19F",380)
turtle.begin_fill()
turtle.pen(pencolor="red",pensize="1")
turtle.fillcolor("red")
turtle.speed(0)
turtle.pen(pencolor="red",pensize="1")
for k in range(40):
    square(270)
    turtle.rt(10)
turtle.end_fill()
turtle.pen(pencolor="orange",pensize="1")
circ("orange",350)
turtle.pen(pencolor="#383629",pensize="1")
big_flower("#383629")
turtle.right(60)
turtle.pen(pencolor="#EFE19A",pensize="1")
big_flower("#EFE19A")
turtle.pen(pencolor="#C8520A",pensize="1")
turtle.right(30)
big_flower("#C8520A")
turtle.pen(pencolor="red",pensize="1")
circ("red",280)


t = turtle.Turtle()
t.speed(0)
turtle.pen(pencolor="#FFD504",pensize="1")
t.begin_fill()
#turtle.pen(pencolor="#FFD504",pensize="1")
t.fillcolor("#FFD504")
for k in range(12):
    for i in range(6):
        t.forward(140)
        t.right(60) 
    t.rt(30)
t.end_fill()
#draw_flower()
turtle.pen(pencolor="#F4E389",pensize="1")
circ("#F4E389",250)
turtle.pen(pencolor="#E67B47",pensize="1")
circ("#E67B47",230)
turtle.pen(pencolor="#2E7644",pensize="1")
circ("#2E7644",210)

turtle.begin_fill()
turtle.pen(pencolor="orange",pensize="1")
turtle.fillcolor("orange")
#draw_flower()
for k in range(40):
    square(148)
    turtle.rt(10)
turtle.end_fill()
turtle.speed(0)
turtle.pen(pencolor="#F4E389",pensize="1")
circ("#F4E389",160)
turtle.speed(0)
turtle.begin_fill()
turtle.pen(pencolor="red",pensize="1")
turtle.fillcolor("red")
#draw_flower()
for k in range(9):
    for i in range(6):
        turtle.forward(100) #Assuming the side of a hexagon is 100 units
        turtle.right(60) #Turning the turtle by 60 degree
    turtle.rt(40)
turtle.end_fill()
turtle.pen(pencolor="#C8520A",pensize="1")
circ("#C8520A",160)
turtle.pen(pencolor="#770E13",pensize="1")
circ("#770E13",145)
turtle.pen(pencolor="#E67B47",pensize="1")
circ("#E67B47",130)
turtle.pen(pencolor="#ECE19F",pensize="1")
circ("#ECE19F",115)

turtle.pen(pencolor="orange",pensize="1")
for k in range(6):
    turtle.begin_fill()
    if k%2==0:
        turtle.pen(pencolor="yellow",pensize="1")
        turtle.fillcolor("yellow")
    else:
        turtle.pen(pencolor="orange",pensize="1")
        turtle.fillcolor("orange")
    square(80)
    turtle.rt(60)
    turtle.end_fill()
turtle.exitonclick()


    

    
    
    
