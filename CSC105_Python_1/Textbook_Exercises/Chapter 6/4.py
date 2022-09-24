# Exercise 4 - Steven Sousa 10-15-2020

import turtle

breski = turtle.Turtle()
wn = turtle.Screen()
breski.pensize(4)
breski.speed(0)


def drawsquare(turtle, size):
    for a in range(4):
        breski.forward(size)
        breski.left(90)


for b in range(20):
    drawsquare(breski, 90)
    breski.left(18)     # 360/20 gives an angle of 18.
    breski.pendown()

wn.exitonclick()
