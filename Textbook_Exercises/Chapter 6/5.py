# Exercise 4 - Steven Sousa 10-15-2020

import turtle

breski = turtle.Turtle()
wn = turtle.Screen()
breski.speed(0)


def drawsquare(turtle, angle):
    length = 1  # Start length at 1
    for a in range(84):
        breski.forward(length)  # Breski will move forward by the length
        breski.right(angle)     # Breski will turn right by the angle
        length = length + 2     # Length will increase by 2 in each interation to make a larger square.


# Draw square spiral
breski.penup()
breski.backward(110)
breski.pendown()
drawsquare(breski, 90)

# Lift pen, move breski to the right by 200 units, and lower pen again
breski.penup()
breski.goto(200, 0)
breski.pendown()

# Draw angled spiral (Repeat of square spiral, but with an 89 angle instead of 90.
breski.penup()
breski.backward(110)
breski.pendown()
drawsquare(breski, 89)

wn.exitonclick()
