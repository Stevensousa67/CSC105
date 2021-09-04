# Exercise 3 - Steven Sousa 10-15-2020

import turtle

breski = turtle.Turtle()
wn = turtle.Screen()
breski.pensize(4)

def drawpoly(turtle, sides, size):
    for a in range(sides):
        breski.forward(40)
        breski.left(45)

sides = 8
size = 50
drawpoly(breski, sides, size)

wn.exitonclick()
