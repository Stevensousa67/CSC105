# Exercise 2 - Steven Sousa 10-15-2020

import turtle

breski = turtle.Turtle()
wn = turtle.Screen()
breski.pensize(4)
sz = 20

def drawsquare(t, sz):
    for a in range(4):
        breski.forward(sz)
        breski.left(90)


for b in range(5):
    drawsquare(breski, sz)  # Calls function
    breski.penup()  # lifts pen
    breski.setx(breski.xcor()-10)   # moves breski back in the xy plane by -10 units
    breski.sety(breski.ycor()-10)   # moves breski down in the xy plane by -10 units
    breski.pendown()    # lowers pen
    sz = sz + 20    # increases size the size of the square in each iteration

wn.exitonclick()
