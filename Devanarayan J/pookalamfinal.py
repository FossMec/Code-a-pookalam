import turtle
import math

qw=turtle.Turtle()
qw.speed(10000)


def turtpos(x,y):
  qw.penup()
  qw.setpos(x,y)
  qw.pendown()

def turtsquare(length):
	for i in range(4):
		qw.forward(length)
		qw.left(90)

def turtpattern1(length):
	turtpos(0,0)
	for i in range(19):
		turtsquare(length)
		qw.left(20)

def turtpattern2(radius):
	turtpos(0,0)
	for i in range(19):
		qw.circle(radius)
		qw.left(30)



qw.getscreen().bgcolor("grey")#background colour is set





qw.color("#000000","#000000")
turtpos(0,-300)                                   #outline
qw.begin_fill()
qw.circle(300)
qw.end_fill()

qw.color("#330033","#660066")#thesquarestuff
qw.begin_fill()
turtpattern1(200)
qw.end_fill()

qw.color("#ff6600","#993399")#the circle thing
qw.begin_fill()
turtpattern2(90)
qw.end_fill()

qw.color("#004d99","#cc00ff")#the weird star spam thing
turtpos(0,0)
qw.begin_fill()
for j in range(20):
	for i in range(10):
		qw.forward(150)
		qw.left(216)
	qw.left(20)
qw.end_fill()

turtpos(0,-90)#circle inside the star spam
qw.left(90)
qw.color("#fc0303","#ff00ff")
qw.begin_fill()
qw.circle(90)
qw.end_fill()

turtpos(0,0)#the innermost pattern
qw.color("#993399","#ff99ff")
qw.begin_fill()
for j in range(15):
	for i in range(6):
		qw.forward(30)
		qw.left(300)
	qw.left(50)
qw.end_fill()






turtle.done()
