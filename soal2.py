
import turtle
s = turtle.Screen().bgcolor('pink')
pen = turtle.Turtle()
pen.pensize(3)
#tongkat coklat
pen.down()
pen.fillcolor('brown')
pen.begin_fill()
pen.forward(20)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(50)
pen.end_fill()
pen.up()

#papan kuning

pen.goto(0,50)
pen.down()
pen.fillcolor('yellow')
pen.begin_fill()
pen.left(90)
pen.forward(120)
pen.left(45)
pen.forward(50)
pen.left(45)
pen.forward(125)
pen.left(45)
pen.forward(50)
pen.left(45)
pen.forward(220)
pen.left(45)
pen.forward(50)
pen.left(45)
pen.forward(125)
pen.left(45)
pen.forward(50)
pen.left(45)
pen.forward(100)
pen.end_fill()
pen.up()

#membuat HI!
pen.pencolor('red')
pen.goto(-25,65)
pen.down()
pen.left(90)
pen.forward(30)
pen.backward(15)
pen.right(90)
pen.forward(30)
pen.left(90)
pen.forward(15)
pen.backward(30)

pen.up()
pen.goto(15, 65)
pen.down()
pen.forward(30)

pen.up()
pen.goto(35, 65)
pen.down()
pen.forward(1)
pen.up()
pen.goto(35,75)
pen.down()
pen.forward(19)
pen.up()
pen.pencolor('black')

#membuat lingkaran
pen.goto(20, 115)
pen.down()
pen.pencolor('blue')
pen.right(90)
pen.circle(55, 360)


#membuat bintang banyak
pen.pencolor('red')
pen.goto (5,115)
for i in range(12):
    pen.left(45)
    pen.forward(50)
    pen.left(95)


turtle.done()