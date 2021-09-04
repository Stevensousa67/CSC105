# Modify the walking turtle program so that rather than a 90 degree left or right turn
# the angle of the turn is determined randomly at each step.
# Steven Sousa - Exercise 4 - 10/26/2020

import random
import turtle


def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn


t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
x = 0   # Initiate x variable that will hold the random left turn angle
y = 0   # Initiate y variable that will hold the random right turn angle
while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:
        x = random.randint(1, 360)
        t.left(x)
    else:
        y = random.randint(1, 360)
        t.right(y)

    t.forward(50)

wn.exitonclick()
