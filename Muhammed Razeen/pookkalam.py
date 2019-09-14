import turtle
import math

raz = turtle.Turtle()
raz.hideturtle()
raz.speed(0)

# set bg color
raz.getscreen().bgcolor("grey")

# outer circle
raz.color("maroon")
raz.begin_fill()
raz.penup()
raz.right(90)
raz.forward(280)
raz.left(90)
raz.pendown()
raz.circle(290)
raz.penup()
raz.left(90)
raz.forward(290)
raz.right(90)
raz.pendown()
raz.end_fill()
# base design
raz.color("bisque")
for i in range(10) :
    raz.begin_fill()
    raz.circle(140)
    raz.circle(-140)
    raz.left(45)
    raz.end_fill()

# design 2
def shape(size,side):
    for i in range(side):
        raz.forward(size)
        raz.left(360/side)

#for square
for j in range(13) :
  raz.color("orangered")
  raz.begin_fill()
  shape(185,4)
  raz.left(30)
  raz.end_fill()

        #for pentagon
for j in range(13) :
  raz.color("black")
  raz.begin_fill()
  shape(135,5)
  raz.left(30)
  raz.end_fill()


  # design three --petals
  def draw_petal(turtle, radius):
      heading=turtle.heading()
      turtle.circle(radius,60)
      turtle.left(120)
      turtle.circle(radius,60)
      turtle.setheading(heading)
  def petal(my_petals,my_radius,c):
      for i in range(my_petals):
          raz.color(c)
          raz.fillcolor(c)
          raz.begin_fill()
          draw_petal(raz,my_radius)
          raz.left(360/my_petals)
          raz.end_fill()
raz.speed(0)
petal(150,200,"tomato")

# base before petal
raz.color("sandy brown")
raz.begin_fill()
for i in range(18):

    raz.circle(90)
    raz.circle(-90)
    raz.left(30)
raz.end_fill()


# petal 2
petal(30,190,"darkgreen")

# second set of squares
for j in range(21):
  raz.color("gold")
  raz.begin_fill()
  shape(110, 4)
  raz.left(35)
  raz.end_fill()

# circle border

raz.color("maroon")
for i in range(20):
    raz.begin_fill()
    raz.circle(60)
    raz.circle(-60)
    raz.left(10)
    raz.end_fill()

raz.color("midnight blue")
for i in range(20):
    raz.begin_fill()
    raz.circle(55)
    raz.circle(-55)
    raz.left(10)
    raz.end_fill()

raz.color("orange red")
for i in range(20):
    raz.begin_fill()
    raz.circle(50)
    raz.circle(-50)
    raz.left(10)
    raz.end_fill()
#third set of shapes
  #hexagon
raz.color("dark red")
raz.begin_fill()
for j in range(20):

  shape(50, 6)
  raz.left(35)
raz.end_fill()
  #pentagon
raz.color("salmon")
raz.begin_fill()
for j in range(9) :

  shape(48, 5)
  raz.left(45)
raz.end_fill()

  #squares
raz.color("brown")
raz.begin_fill()
for j in range(10):

  shape(45, 4)
  raz.left(35)
raz.end_fill()
raz.color("chocolate")
raz.begin_fill()
for j in range(10):

      shape(41, 4)
      raz.left(35)
raz.end_fill()
raz.color("orange")
raz.begin_fill()
for j in range(10):

  shape(38, 4)
  raz.left(35)
raz.end_fill()

raz.color("gold")
raz.begin_fill()
for j in range(10):

  shape(34, 4)
  raz.left(35)
raz.end_fill()
raz.color("yellow")
raz.begin_fill()
for j in range(10):

  shape(30, 4)
  raz.left(35)
raz.end_fill()

raz.color("green yellow")
raz.begin_fill()
for j in range(10):

  shape(26, 4)
  raz.left(35)
raz.end_fill()

raz.color("lime")
raz.begin_fill()
for j in range(10):
  shape(21, 4)
  raz.left(35)
raz.end_fill()

raz.color("lime green")
raz.begin_fill()
for j in range(10):
  shape(17, 4)
  raz.left(35)
raz.end_fill()

raz.color("forest green")
raz.begin_fill()
for j in range(10):
  shape(13, 4)
  raz.left(35)
raz.end_fill()

raz.color("green")
raz.begin_fill()
for j in range(10):

  shape(9, 4)
  raz.left(35)
raz.end_fill()


turtle.done()