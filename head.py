import turtle

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_eye(x, y):
    draw_circle("white", x, y, 10)  # white part of eye
    draw_circle("black", x, y, 5)   # pupil

def draw_head():
    # Draw head
    draw_circle("peachpuff", 0, -50, 70)  # head

    # Draw eyes
    draw_eye(-35, -30)  # left eye
    draw_eye(35, -30)   # right eye
    
    # Draw mouth
    turtle.penup()
    turtle.goto(-30, -70)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(30, 180)  # half-circle for mouth

# Setup the turtle
turtle.speed(1)
turtle.title("Turtle Human Head Sketch")
turtle.bgcolor("lightblue")

# Draw the human head
draw_head()

# Finish up
turtle.hideturtle()
turtle.done()