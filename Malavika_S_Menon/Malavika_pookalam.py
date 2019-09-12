import turtle             
my_window = turtle.Screen() 
my_window.bgcolor("black")
       # creates a graphics window
my_pen = turtle.Turtle()
my_pen.speed()      
my_pen.up()
my_pen.goto(0,-250)
my_pen.down()
my_pen.color('darkgreen')
my_pen.begin_fill()
my_pen.circle(250)
my_pen.end_fill()

my_pen.goto(0,-220)
my_pen.color('yellow')
my_pen.begin_fill()
my_pen.circle(220)
my_pen.end_fill()
side=8
length=50
angle=360/8
my_pen.goto(0,0)

for j in range(8):
 my_pen.begin_fill()  
 my_pen.right(360/8)
 my_pen.color('orangered')
 for i in range(side):
	 
	my_pen.forward(length)
	my_pen.left(angle)
 my_pen.end_fill()

for j in range(8):
 my_pen.begin_fill()  
 my_pen.right(360/8)
 my_pen.color('orange')
 for i in range(side):
	 
	my_pen.forward(30)
	my_pen.left(angle)
 my_pen.end_fill()



my_pen.up()
my_pen.left(90)
#my_pen.left(90)
my_pen.forward(120)
my_pen.left(90)
my_pen.forward(50)
my_pen.left(360/8)
my_pen.down()
my_pen.color('brown')
my_pen.begin_fill()
my_pen.forward(100)
my_pen.right(120)
my_pen.forward(100)
my_pen.right(120)
my_pen.forward(100)
my_pen.end_fill()
for i in range(7):
	my_pen.begin_fill()
	my_pen.left(75)
	my_pen.forward(100)
	my_pen.right(120)
	my_pen.forward(100)
	my_pen.end_fill()
my_pen.up()
my_pen.goto(0,0)
my_pen.down()
my_pen.left(60)

print my_pen.xcor()
print my_pen.ycor()
my_pen.color('white')
my_pen.shape('circle')
turtle.exitonclick()

