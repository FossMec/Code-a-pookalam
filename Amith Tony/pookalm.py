import turtle
a=turtle.Turtle()

a.up()
a.goto(-180,235)
a.down()

def square(length,angle):
    for i in range(4):
        a.forward(length)
        a.right(angle)

for i in range(10):
       a.color('black','yellow')
       a.speed(200)
       a.pensize(2)
       a.begin_fill()
       square(280, 60)
       a.right(12)
       a.end_fill()
a.up()
a.goto(0,0)
a.down()

for i in range(8):
    a.speed(100)
    a.color("black","orange")
    a.begin_fill()
    a.circle(140)
    a.left(45)
    a.end_fill()

a.penup()
a.goto(0,-250)
a.pendown()
a.pensize(22)
a.color("#dbffc5")
a.begin_fill()
a.circle(250)
a.end_fill()

a.penup()
a.goto(0,-230)
a.pendown()
a.pensize(21)
a.color("green")
a.circle(230)

a.speed(100)
a.up()
a.goto(0,-218)
a.pensize(10)
a.color("brown","yellow")
a.begin_fill()
a.circle(220)
a.end_fill()
a.goto(0,0)

for i in range(8):
    a.pensize(10)
    a.color("black","red")
    a.begin_fill()
    a.circle(100)
    a.right(60)
    a.end_fill()

for i in range(12):
    a.pensize(3)
    a.color("red","orange")
    a.begin_fill()
    a.circle(80)
    a.right(45)
    a.end_fill()

def square(length,angle):
    for i in range(4):
        a.forward(length)
        a.right(angle)

for i in range(6):
    for colours in{"red","violet","blue","yellow","cyan","green"}:
        a.speed(200)
        a.pensize(2)
        a.begin_fill()
        a.color(colours)
        square(100, 90)
        a.right(12)
        a.end_fill()

turtle.done()

