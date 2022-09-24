# Modify the turtle walk program so that you have two turtles each with a random starting location.
# Keep the turtles moving until one of them leaves the screen.
# Steven Sousa - Exercise 5 - 10/26/2020

import random
import turtle


def isInScreen(w, t1, t2):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t1.xcor()
    turtleY = t1.ycor()

    turtleX1 = t2.xcor()
    turtleY1 = t2.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    if turtleX1 > rightBound or turtleX1 < leftBound:
        stillIn = False
    if turtleY1 > topBound or turtleY1 < bottomBound:
        stillIn = False

    return stillIn


t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

t1.shape('turtle')
t2.shape('turtle')

# Create random starting location for t1
rand_x_start_t1 = random.randint(-430, 430)
rand_y_start_t1 = random.randint(-355, 355)
t1.penup()
t1.goto(rand_x_start_t1, rand_y_start_t1)
t1.pendown()

# Create random starting location for 2
rand_x_start_t2 = random.randint(-430, 430)
rand_y_start_t2 = random.randint(-355, 355)
t2.penup()
t2.goto(rand_x_start_t2, rand_y_start_t2)
t2.pendown()

x = 0   # x will hold the random left turn angle for t1
y = 0   # y will hold the random right turn angle for t1

a = 0   # a will hold the random left turn angle for t2
b = 0   # b will hold the random right turn angle for t2

while isInScreen(wn, t1, t2):
    coin = random.randrange(0, 2)
    if coin == 0:
        x = random.randint(1, 360)
        a = random.randint(1, 360)
        t1.left(x)
        t2.left(a)
    else:
        y = random.randint(1, 360)
        b = random.randint(1, 360)
        t1.right(y)
        t2.right(b)

    t1.forward(50)
    t2.forward(50)

wn.exitonclick()
