import turtle

print("Happy Onam")
tim = turtle.Turtle()
tim.speed(5000)

def petal(length=200,x1=0,x2=0,x3=0):
  tim.color(x1,x2,x3)
  tim.begin_fill()
  for i in range(9):
    tim.forward(length)
    tim.circle(length/4,208)
    tim.forward(length)
    tim.right(180)
    tim.right(-17)
  tim.end_fill()

def circ(rad=100,x1=0,x2=0,x3=0):
  tim.penup()
  tim.right(-90)
  tim.backward(rad)
  tim.pendown()
  tim.right(90)
  tim.color(x1,x2,x3)
  tim.begin_fill()
  tim.circle(rad)
  tim.end_fill()
  tim.penup()
  tim.right(-90)
  tim.forward(rad)
  tim.pendown()
  tim.right(90)

def sq(x=50,x1=0,x2=0,x3=0):
  tim.color(x1,x2,x3)
  tim.begin_fill()
  for i in range(4):
    tim.forward(x)
    tim.right(90)
  tim.end_fill()

def sqdes(siz=20,x1=0,x2=0,x3=0,delta=20):
  tim.color(x1,x2,x3)
  for i in range(360/delta):
    sq(siz*0.707,x1,x2,x3)
    tim.right(delta)

#orange 255,166,0

circ(300, 17, 110, 0) #green
circ(280, 251,255,41) #yellow
tim.right(90)
tim.forward(201)
tim.right(-90)
tim.right(22.5)
for i in range(8):
  circ(78.95,227,38,54) #crimson
  tim.right(-45)
  tim.forward(154)

tim.right(67.5)
tim.backward(201)
#sqdes(280,255, 253, 184,30)
tim.pensize('5')
circ(225,255,255,230) #cream
circ(206,17,110,0) #green
#red 255,75,20'''
tim.right(-90)
tim.right(11.25)
petal(160,255,166,0) #orange
petal(140,251,255,41) #yellow
petal(110,255,255,230) #jasmine
circ(75,17,110,0) #green
circ(60,255,255,230) #jasmine
circ(45,166,77,255) #violet
circ(20,251,255,41) #yellow