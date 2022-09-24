# Draw David Star

import turtle

window = turtle.Screen()
breski = turtle.Turtle()
breski.shape("turtle")

for star_points in range(5):
    breski.forward(100)
    breski.right(144)

window.exitonclick()
