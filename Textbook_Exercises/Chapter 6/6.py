# Exercise 6 - Steven Sousa 10-15-2020

import turtle

breski = turtle.Turtle()
wn = turtle.Screen()


def drawpoly(turtle, sides, size):
    for a in range(sides):
        breski.forward(40)
        breski.left(45)


def drawequitriangle(turtle, size):
    drawpoly(breski, sides, size)


sides = 3
size = 50
drawequitriangle(breski, size)

wn.exitonclick()
