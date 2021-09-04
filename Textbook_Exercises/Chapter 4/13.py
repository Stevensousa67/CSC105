# Draw a sprite using turtle

import turtle

window = turtle.Screen()
breski = turtle.Turtle()

num_legs = int(input("How many legs will the sprite have? "))
angle = 360/num_legs

for clock in range(num_legs):
    breski.forward(125)
    breski.stamp()
    breski.forward(-125)
    breski.right(angle)

window.exitonclick()
