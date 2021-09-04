# The lines of this file contain either the word UP or DOWN or a pair of numbers. UP and DOWN are instructions for a
# turtle to lift up or put down its tail. The pairs of numbers are some x,y coordinates. Write a program that reads the
# file mystery.txt and uses the turtle to draw the picture described by the commands and the set of points.
# Steven Sousa - Exercise 5 - 11/26/2020

import turtle
breski = turtle.Turtle()
window = turtle.Screen()

file = open("mystery.txt", "r")             # open text file

for line in file:                           # Iterate over each line of file
    index = line.split()                    # Make each line a list
    if index[0] == 'UP':                    # Search for word UP in list
        breski.penup()                      # lift pen is word is UP
    elif index[0] == 'DOWN':              # Search for word DOWN in list
        breski.pendown()                # Lower the pen if word is DOWN
    else:
        breski.goto(int(index[0]), int(index[1]))   # Otherwise just go to xy coodinates

file.close()                                # Close file
window.exitonclick()
