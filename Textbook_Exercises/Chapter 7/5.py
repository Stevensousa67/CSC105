# Add a negative number to the turtle bar chart.
# Steven Sousa - Exercise 4 - 10/20/2020

import turtle


def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()  # start filling this shape
    if height >= 200:
        tess.fillcolor("red")
    elif height >= 100:
        tess.fillcolor("yellow")
    else:
        tess.fillcolor("green")
    if height < 0:
        t.write(str(height))
        t.left(90)
        t.forward(height)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()    # stop filling this shape
    else:
        t.left(90)
        t.forward(height)
        t.write(str(height))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()


xs = [-10, 48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()  # Set up the window and its attributes
wn.setworldcoordinates(0 - border, 0 - border, 40 * numbars + border, maxheight + border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  # create tess and set some attributes
tess.color("blue")
tess.pensize(3)

for a in xs:
    drawBar(tess, a)

wn.exitonclick()
