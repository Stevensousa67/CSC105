# Exercise 1 - Steven Sousa 10-15-2020

import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()          # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()        # create alex

for a in range(5):
    drawSquare(alex, 20)
    alex.penup()
    alex.forward(30)
    alex.pendown()
    
wn.exitonclick()

