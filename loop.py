import turtle

def draw_square(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    
    turtle.end_fill()

def draw_triangle(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    
    turtle.end_fill()

# Set up the turtle
turtle.speed(1)
turtle.title("Turtle House")
turtle.bgcolor("lightblue")

# Draw the house square base
draw_square("yellow", -50, -50, 100)

# Draw the roof
draw_triangle("brown", -60, 50, 120)

# Draw windows
draw_square("blue", -40, -30, 30)  # left window
draw_square("blue", 10, -30, 30)   # right window

# Draw the door
draw_square("red", -20, -50, 40)

# Finish up
turtle.hideturtle()
turtle.done()