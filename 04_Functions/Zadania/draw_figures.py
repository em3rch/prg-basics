import turtle
import figures as fg


# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

fg.draw_rectangle(pen, 300, 200)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()


