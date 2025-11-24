import turtle


def draw_square(pen, length):
    # Draw a square
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(pen, length):
    for i in range(3):
        pen.left(120)
        pen.forward(length)

def draw_rectangle(pen, length_a, length_b):
    pen.forward(length_a)
    pen.left(90)

    pen.forward(length_b)
    pen.left(90)

    pen.forward(length_a)
    pen.left(90)

    pen.forward(length_b)
    pen.left(90)

