import random
import turtle

screen = turtle.getscreen()
t = turtle.Turtle()


def triangle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(3):
        t.forward(100)
        t.left(120)
        t.forward(100)


for index in range(0, 10):
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    triangle(x, y)
    print(x, y)

turtle.getscreen()._root.mainloop()  # <-- run the Tkinter main loop keeps screen open
