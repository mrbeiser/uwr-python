import turtle

def resetPosition():
    t.penup()
    t.goto(0,0)
    t.pendown()

t = turtle.Turtle()
t.pencolor('black')
t.pendown()
turtle.tracer(0)

for j in range(9):
    for i in range(0, 360//9, 2):
        t.right(2)
        t.forward(50+i)
        resetPosition()
turtle.update()
turtle.done()