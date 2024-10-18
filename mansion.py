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

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
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

# Setup the turtle
turtle.speed(5)
turtle.title("Turtle Mansion")
turtle.bgcolor("lightblue")

# Draw the main building
draw_rectangle("lightgray", -150, -100, 300, 200)  # Main body

# Draw the roof
draw_triangle("brown", -160, 100, 320)  # Roof

# Draw windows
draw_square("white", -130, -50, 50)   # Left window
draw_square("white", 80, -50, 50)     # Right window
draw_square("white", -130, -90, 50)   # Left bottom window
draw_square("white", 80, -90, 50)     # Right bottom window

# Draw a large door
draw_rectangle("red", -40, -100, 80, 100)  # Main door

# Draw additional parts (like a balcony)
draw_rectangle("lightgray", -80, 0, 160, 20)  # Balcony

# Draw a few plants around the mansion
turtle.penup()
turtle.goto(-160, -120)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(140, -120)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# Finish up
turtle.hideturtle()
turtle.done()