import turtle
import time


def draw_rectangle_slow(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(2)
    turtle.speed(5)

    # Draw rectangle gradually
    for _ in range(2):
        for _ in range(width // 10):
            turtle.forward(10)
            time.sleep(0.005)
        turtle.right(90)
        for _ in range(height // 10):
            turtle.forward(10)
            time.sleep(0.005)
        turtle.right(90)

    # Fill the rectangle at the end
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()


def draw_circle_slow(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(2)
    turtle.speed(5)

    # Draw circle gradually
    turtle.begin_fill()
    for _ in range(360):
        turtle.forward(2 * 3.14 * radius / 360)
        turtle.left(1)
        time.sleep(0.002)
    turtle.end_fill()


# Make the turtle visible
turtle.showturtle()
turtle.shape("classic")  # arrow-like pen
turtle.speed(5)

# Flag dimensions
flag_length = 600
flag_width = 360
circle_radius = flag_length * 1 / 5
circle_center_x = -flag_length * 1 / 20

# Draw flag
draw_rectangle_slow(-flag_length / 2, flag_width / 2, flag_length, flag_width, "#006a4e")
draw_circle_slow(circle_center_x, 0, circle_radius, "#f42a41")

# Add developer text below the flag
turtle.penup()
turtle.goto(0, -flag_width / 2 - 40)  # 40 pixels below flag
turtle.color("black")
turtle.write('Developed by "Atik Hasan", Secretary Of Graphics Design, NUBCC',
             align="center", font=("Arial", 16, "bold"))

turtle.hideturtle()
turtle.done()