import turtle

screen = turtle.getscreen()

t = turtle.Turtle()

t.right(90)  # rotate 90 degrees
t.forward(100)  # forward 100 pixels
t.left(90)  # roate 90 degrees
t.backward(100)  # backwards 100 pixels

# moves from current postion to a point in the quadrant plane cneter is (0,0)
t.goto(100, 100)

t.home()  # returns to (0,0)

# this draws a square
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

# cirlce
t.circle(60)
# creates a dot where the turtle is at input is how big the dot is
t.dot(20)

# change back ground color
turtle.bgcolor("blue")
turtle.bgcolor("black")
turtle.bgcolor("white")
turtle.bgcolor("green")
turtle.bgcolor("white")
# goest to white since its the last one

# changes the size of the turtle
#
#    Stretch length
#    Stretch width
#    Outline width

t.shapesize(1, 5, 10)
t.shapesize(10, 5, 1)
t.shapesize(1, 10, 5)
t.shapesize(10, 1, 5)
t.shapesize(1, 1, 1)

# pensize
t.pensize(5)
t.forward(100)

# draws a tringle then fills it
t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()


# draw speeds
t.speed(1)
t.forward(100)
t.speed(10)
t.forward(100)

# clears screen
t.clear()
# resets the turtle postion
t.reset()
# clears and resets everthing
turtle.Screen().clear()

# fuin example
t.pen(pencolor="purple", fillcolor="orange", pensize=100, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()

turtle.getscreen()._root.mainloop()  # <-- run the Tkinter main loop keeps screen open
