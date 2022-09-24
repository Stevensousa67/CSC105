# Draw a clock face using turtle
# Gabriele Narmontaite collaborated with me on this code.
# She taught to me an easier way of stamping breski in a clock formation.

import turtle

window = turtle.Screen()
breski = turtle.Turtle()
breski.shape("turtle")

# Stamp clock figure (Gabriele's collaboration)
for clock in range(12):
    breski.penup()
    breski.forward(100)
    breski.pendown()
    breski.forward(10)
    breski.penup()
    breski.forward(15)
    breski.stamp()
    breski.forward(-125)
    breski.right(30)

window.exitonclick()
