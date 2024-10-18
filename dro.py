import turtle
 
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#000000')

t.speed(10)

for i in range(36):
    t.pencolor('#ffffff')
    t.circle(100)
    t.right(10)

turtle.done()