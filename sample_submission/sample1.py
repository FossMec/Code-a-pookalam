from turtle import *
speed(0)
pencolor('yellow')
bgcolor('white')
up()
for i in range(200,24,-25):
    pen(pencolor="black",pensize="0")
    rt(90)
    fd(i)
    rt(270)
    down()
    begin_fill()
    if (i==25):
        pen(fillcolor="red",pencolor="white",pensize=1)
        circle(i)
        up()
        home()
        down()
        for j in range(1,37):
            for k in range(1,5):
                fd(30)
                rt(90)
            rt(10)
    elif (i==50 or i==175):
        pen(fillcolor="orange")
        circle(i)
    elif (i==75):
        pen(fillcolor="green",pencolor="gold",pensize=3)
        circle(i)
        up()
        home()
        down()
        for j in range(1,37):
            for k in range(1,5):
                fd(60)
                rt(90)
            rt(10)
    elif (i==100):
        pen(fillcolor="turquoise")
        circle(i)
    elif (i==125):
        pen(fillcolor="royalblue",pencolor="pink",pensize=2)
        circle(i)
    elif (i==150):
        pen(fillcolor="gold",pencolor="white",pensize=3)
        circle(i)
        up()
        home()
        down()
        for j in range(1,9):
            for k in range(1,5):
                fd(125)
                rt(90)
            rt(45)
    else:
        pen(fillcolor="firebrick",pencolor="green",pensize=3)
        circle(i)
        up()
        home()
        down()
        for j in range(1,37):
            for k in range(1,5):
                fd(150)
                rt(90)
            rt(10)
    end_fill()
    up()
    home()
ht()
exitonclick()

