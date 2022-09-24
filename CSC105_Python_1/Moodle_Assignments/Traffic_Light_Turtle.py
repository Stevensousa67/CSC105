# This program will use turtle to draw a traffic light
# Steven Sousa / Python / 4Cs / 09-18-2020

# Import the turtle module
import turtle

# Program presents itself to user
print("This program will draw a traffic light using turtle.")

# Create and setup the window for turtle. Background is white by default
window = turtle.Screen()

# Create and setup turtle
breski = turtle.Turtle()
breski.shape("turtle")

# Set up basics before drawing rectangle
breski.penup()  # Pen up so that breski won't leave a trail behind when going to bottom left corner
breski.goto(-200, -300)     # Sets breski at the bottom left corner of rectangle
breski.pendown()    # pen down so that breski can leave a trail wherever he goes

# Draw the rectangle shape of traffic light
breski.fillcolor("black")  # Selects the color that the rectangle will be
breski.begin_fill()     # Tells breski to start coloring the rectangle
breski.forward(350)     # Draws the bottom width of rectangle
breski.left(90)     # Tells breski to turn to his left 90 degrees
breski.forward(610)     # Tells breski draw right side height of rectangle
breski.left(90)     # Tells breski to turn to his left 90 degrees
breski.forward(350)     # Tells breski to draw top width of rectangle
breski.left(90)     # Tells breski to turn to his left 90 degrees
breski.forward(610)     # Tells breski to draw left side height of rectangle
breski.left(90)     # Tells turtle to face east at the end of rectangle (convention)
breski.end_fill()   # Tells breski to stop coloring

# Draw the first circle from the traffic light
breski.penup()  # Pen up so that breski won't leave a trail behind when going to bottom left corner
breski.goto(-30, -290)  # Sets breski at the bottom middle of rectangle
breski.pendown()    # Tells breski to lower pen so that he'll leave a trail behind
breski.fillcolor("green")   # Selects color to fill the circle that will be drawn
breski.begin_fill()     # Start coloring the circle
breski.circle(95)   # Draws the circle. Radius is 80
breski.end_fill()   # Stop coloring the circle

# Draw the second circle from the traffic light
# This code is a repeat of first circle, but changes the y coordinate and color of circle
breski.penup()
breski.goto(-30, -90)
breski.pendown()
breski.fillcolor("yellow")
breski.begin_fill()
breski.circle(95)
breski.end_fill()

# Draw the third circle from the traffic light
# This code is a repeat of first circle, but changes the y coordinate and color of circle
breski.penup()
breski.goto(-30, 110)
breski.pendown()
breski.fillcolor("red")
breski.begin_fill()
breski.circle(95)
breski.end_fill()

# Make window remain open after code execution until user clicks with mouse
window.exitonclick()
