import turtle
import math

t = turtle.Turtle()
t.speed(20)
t.shape("turtle")
t.getscreen().bgcolor("yellow")
outer_radius = 300
inner_radius = 250


def petals(num, length):
    t.pu()
    t.home()
    t.pd()
    t.setheading(0)
    angle = 360 / num
    theta = 0
    t.begin_fill()
    for i in range(num):
        t.setheading(theta)
        t.circle(length)
        theta += angle
    t.end_fill()

# petals(5,small_radius)

t.color("darkgreen", "green")
t.begin_fill()
t.pu()
t.goto(outer_radius, 0)
t.left(90)
t.pd()
t.circle(outer_radius)
t.end_fill()


t.goto(inner_radius, 0)
t.color("white", "orange")
t.begin_fill()
t.circle(inner_radius)
t.end_fill()
t.color("blue")

print(t.pos())
t.left(45)
t.pu()
t.pd()
t.begin_fill()
c = inner_radius * math.sqrt(2)
for i in range(4):
    t.forward(c)
    t.left(90)
t.end_fill()

y = inner_radius/2+60
# y=c
t.setheading(90)
t.circle(inner_radius,90/3)
t.color("red")
t.pd()
t.begin_fill()
t.left(45)
for i in range(4):
    t.forward(c)
    t.left(90)
t.end_fill()

t.color("magenta")
t.pu()
t.goto(inner_radius,0)
t.setheading(90)
t.circle(inner_radius,60)
t.pd()
t.begin_fill()
t.left(45)
for i in range(4):
    t.forward(c)
    t.left(90)
t.end_fill()

t.setheading(90)
t.color("yellow")
n = 6  # no.of petals
petals(n, inner_radius)
t.color("brown")
petals(6,inner_radius-143.5)

t.color("blue")
t.pu()
z = outer_radius-15 #for filling
t.goto(z, 0)
t.setheading(90)
t.width(30)
t.pd()
t.circle(z)
t.width(5)

t.color("lightgreen")
small_radius = y/2
t.pu()
t.setpos(small_radius,0)
t.setheading(90)
t.width(25)
t.pd()
t.circle(small_radius)
t.pu()
t.goto(30,0)
t.color("brown")
t.begin_fill()
t.circle(30)
t.end_fill()
t.setpos(10,0)
t.color("khaki")
t.begin_fill()
t.circle(10)
t.end_fill()
t.pu()
t.color("yellow")
t.goto(310,0)
turtle.done()
