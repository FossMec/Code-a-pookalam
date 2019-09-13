from turtle import *
import turtle

size=300

screen = Screen()
screen.screensize(400,400,"white")

def draw_petal(turtle, radius):
    heading = turtle.heading()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.setheading(heading)

def petal(my_radius,my_petals,c):
    for _ in range(my_petals):
        bob.color(c)
        bob.fillcolor(c)
        bob.begin_fill()
        draw_petal(bob, my_radius)
        bob.left(360 / my_petals)
        bob.end_fill()
        bob.hideturtle()

bob = Turtle()
pen = Pen()
bob.speed(1000)
pen.speed(1000)

flag=0

def fillshape(steps,radius,c1,c2):
    if(flag==0):
        c2=c1
    pen.color(c1)
    pen.fillcolor(c2)
    pen.begin_fill()
    pen.down()
    if(steps!=0):
        pen.circle(radius,steps=steps)
    else:
        pen.circle(radius)
    pen.end_fill()
    pen.up()
    pen.hideturtle()

pen.goto(0,-size)
c1="black"
c2="black"

fillshape(0,size,c1,c2)

pen.goto(0,0)
x=0
turtle.delay(0)
colormode(255)
no=12

for i in range (no*6):
    pen.goto(0,0)
    pen.right(30)
    if(i<no):
        c1="darkred"
        fillshape(4,size/2,c1,c2)

        my_radius = 270
        my_petals = 36

        if(i%no==11):
            for _ in range(my_petals):
                bob.color('crimson')
                bob.fillcolor('crimson')
                bob.begin_fill()
                draw_petal(bob, my_radius)
                bob.left(360 / my_petals)
                bob.end_fill()

    elif(i<no*2):
        c1="orangered"
        fillshape(4,size/2-10,c1,c2)

    elif(i<no*3):
        c1="orange"
        fillshape(4,size/2-20,c1,c2)

        my_radius = 240
        my_petals = 36

        if(i%no==11):
            for _ in range(my_petals):
                bob.color('tomato')
                bob.fillcolor('tomato')
                bob.begin_fill()
                draw_petal(bob, my_radius)
                bob.left(360 / my_petals)
                bob.end_fill()
        
    elif(i<no*4):
        c1="white"
        fillshape(4,size/2-30,c1,c2)

    elif(i<no*5):
        c1="steelblue"
        fillshape(4,size/2-40,c1,c2)

    elif(i<no*6):
        c1="black"
        fillshape(4,size/2-50,c1,c2)
    
x=30
pen.right(15)
pen.pensize(10)
for i in range(12):

    pen.goto(0,0)
    c1="white"
    fillshape(2,130,c1,c2)
    pen.right(30)

for i in range(12):

    pen.goto(0,0)
    c1="orange"
    fillshape(2,120,c1,c2)
    pen.right(30)

for i in range(12):

    pen.goto(0,0)
    c1="orangered"
    fillshape(2,110,c1,c2)
    pen.right(30)

for i in range(12):

    pen.goto(0,0)
    c1="darkred"
    fillshape(2,100,c1,c2)
    pen.right(30)

pen.left(15)
pen.width(1)
for i in range(no*3):
        
    if(i<no):
        pen.goto(0,0)
        c1="mediumpurple"
        fillshape(4,90,c1,c2)
        pen.right(30)

    elif(i<no*2):
        pen.goto(0,0)
        c1="darkgreen"
        fillshape(4,90,c1,c2)
        pen.right(30)

    elif(i<no*3):
        pen.goto(0,0)
        c1="mediumslateblue"
        fillshape(4,90,c1,c2)
        pen.right(30)

    if(i%no==11):
        pen.right(12)

size2 = 150
pen.goto(0,-size2)
pen.left(35)
c1="black"
fillshape(0,size2,c1,c2)

bob.speed(1000)

#headacc
pen.width(4)
pen.down()
pen.goto(54,24)
pen.color('darkslateblue')
pen.fillcolor('darkgreen')
pen.begin_fill()
pen.left(45)
pen.circle(80,270)
pen.up()
pen.end_fill()

p = Turtle()
p.speed(20)
x=18

p.speed(3)
p.color('maroon')

for i in range(12):
    if(i>5):
        x+=7
        y=12-i
    else:
        x+=6
        y=i

    p.up()
    p.goto(1,x)
    p.down()
    p.write("*"*y,align='center',font=("Arial", 50, "normal"))

p.color('teal')
x=18

for i in range(8):
    if(i>5):
        x+=7
        y=12-i
    else:
        x+=6
        y=i

    p.up()
    p.goto(1,x)
    p.down()
    p.write("*"*y,align='center',font=("Arial", 50, "normal"))

petal(150,12,'crimson')
petal(110,12,'black')
petal(70,12,'teal')

p.width(4)
p.speed(2000)

flag=1
#greenstruct
p.up()
p.goto(0,5)
p.down()
p.color('seagreen')
p.fillcolor('seagreen')
p.begin_fill()
p.goto(0,5)
p.goto(-50,5)
p.goto(-70,15)
p.goto(-70,-40)
p.goto(-30,-70)
p.goto(30,-70)
p.goto(70,-40)
p.goto(70,15)
p.goto(50,5)
p.goto(0,5)
p.end_fill()
p.up()

#cheek semicircles
p.color("black")
p.fillcolor('limegreen')
p.goto(-45,-60)
p.down()
p.left(60)
p.begin_fill()
p.circle(30,120)
p.goto(-71,-41)
p.end_fill()
p.up()
p.goto(70,-18)
p.down()
p.begin_fill()
p.circle(30,120)
p.goto(71,-41)
p.end_fill()
p.up()
p.goto(25,-71)
p.down()
p.left(160)
p.begin_fill()
p.circle(25,160)
p.up()
p.goto(0,-71)
p.end_fill()
p.up()

#eyebrows
p.up()
p.goto(-20,30)
p.color("forestgreen")
p.down()
p.goto(-4,18)
p.goto(4,18)
p.goto(20,30)
p.goto(40,30)
p.goto(70,55)
p.color('tomato')
p.goto(35,60)
p.color('forestgreen')
p.goto(0,21)
p.goto(-35,60)
p.color('tomato')
p.goto(-70,55)
p.color('forestgreen')
p.goto(-40,30)
p.goto(-20,30)
p.up()

p.goto(30,60)
p.down()
p.begin_fill()
p.goto(35,42)
p.goto(18,42)
p.end_fill()
p.up()
p.goto(-30,60)
p.down()
p.begin_fill()
p.goto(-35,42)
p.goto(-18,42)
p.end_fill()

p.width(3)
#nose
p.goto(0,18)
p.down()
p.color('black')
p.fillcolor('forestgreen')
p.begin_fill()
p.goto(-15,-5)
p.goto(15,-5)
p.goto(0,18)
p.end_fill()

#mouth
p.up()
p.goto(-15,-25)
p.fillcolor('firebrick')
p.begin_fill()
p.down()
p.goto(18,-25)
p.goto(7.5,-14)
p.goto(0,-25)
p.goto(-7.5,-14)
p.goto(-18,-25)
p.end_fill()
p.fillcolor('crimson')
p.begin_fill()
p.goto(0,-35)
p.goto(18,-25)
p.goto(-18,-25)
p.end_fill()
p.goto(18,-25)
p.left(20)
p.begin_fill()
p.circle(5)
p.end_fill()
p.goto(-18,-25)
p.left(180)
p.begin_fill()
p.circle(5)
p.end_fill()

p.speed(1000)
#eyes
p.up()
p.goto(12,16)
p.color('khaki')
p.fillcolor('khaki')
p.down()
p.begin_fill()
p.goto(22,24)
p.goto(40,24)
p.goto(34,18)
p.goto(12,16)
p.end_fill()
p.up()
p.goto(-12,16)
p.down()
p.begin_fill()
p.goto(-22,24)
p.goto(-40,24)
p.goto(-34,18)
p.goto(-12,16)
p.end_fill()
p.color('black')
p.fillcolor('black')
p.up()
p.goto(-22,24)
p.left(30)
p.down()
p.begin_fill()
p.circle(5)
p.end_fill()
p.up()
p.goto(22,24)
p.left(110)
p.down()
p.begin_fill()
p.circle(5)
p.end_fill()

#forehead
p.up()
p.goto(0,22)
p.color("goldenrod")
p.fillcolor("goldenrod")
p.begin_fill()
p.down()
p.goto(-35,60)
p.color('tomato')
p.goto(35,60)
p.color('goldenrod')
p.goto(0,22)
p.end_fill()

p.width(2)
p.up()
p.fillcolor('crimson')
p.goto(20,60)
p.down()
p.begin_fill()
p.goto(0,60)
p.goto(12,40)
p.end_fill()
p.up()
p.goto(-20,60)
p.down()
p.begin_fill()
p.goto(0,60)
p.goto(-12,40)
p.end_fill()
p.up()
p.fillcolor('maroon')
p.begin_fill()
p.goto(0,57)
p.down()
p.goto(10,43)
p.goto(0,30)
p.goto(-6,40)
p.end_fill()

#headband
p.up()
p.fillcolor('crimson')
p.goto(-70,55)
p.down()
p.begin_fill()
p.goto(-35,60)
p.goto(35,60)
p.goto(70,55)
p.goto(60,70)
p.goto(-60,70)
p.goto(-70,55)
p.end_fill()
p.width(3)
p.up()
p.goto(60,72)
p.down()
p.color('darkgreen')
p.goto(-60,72)
p.up()
p.goto(60,75)
p.down()
p.color('white')
p.goto(-60,75)
p.up()
p.goto(60,78)
p.down()
p.color('darkgreen')
p.goto(-60,78)
p.up()
p.goto(60,81)
p.down()
p.color('white')
p.goto(-60,81)
p.up()
p.goto(60,84)
p.down()
p.color('crimson')
p.goto(-60,84)
p.up()
p.goto(60,87)
p.down()
p.color('maroon')
p.goto(-60,87)

p.speed(1000)
#circle
p.up()
p.width(15)
p.color('darkgreen')
p.fillcolor('orange')
p.goto(-60,70)
p.down()
p.begin_fill()
p.left(180)
p.circle(20)
p.end_fill()
p.width(3)
p.color('teal')
p.circle(20)
p.up()
pen.width(2)
for i in range (9):
    pen.goto(-78,80)
    c1="forestgreen"
    fillshape(2,14,c1,c2)
    pen.right(40)
p.up()
p.width(15)
p.color('darkgreen')
p.fillcolor('orange')
p.goto(60,70)
p.down()
p.begin_fill()
p.right(100)
p.circle(20)
p.end_fill()
p.width(3)
p.color('teal')
p.circle(20)
p.up()
pen.width(2)
for i in range (9):
    pen.goto(72,86)
    c1="forestgreen"
    fillshape(2,14,c1,c2)
    pen.right(40)

p.color('black')
p.up()
p.goto(1,40)
p.down()
p.write("*",align='center',font=("Arial", 55, "normal"))

bob.hideturtle()
pen.hideturtle()
p.hideturtle()
