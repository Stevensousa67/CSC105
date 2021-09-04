# Draws pirate path

import turtle

window = turtle.Screen()
breski = turtle.Turtle()
breski.shape("turtle")
breski.speed(1)     # this sets breski speed to the slowest to check if he's rotating correctly.

for pirate_path in (160, -43, 270, -97, -43, 200, -940, 17, -86):
    breski.forward(100)
    breski.left(pirate_path)

window.exitonclick()
