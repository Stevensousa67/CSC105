# This program will use turtle to draw the Olympic rings
# Steven Sousa / Python / 4Cs / 09-19-2020

# Import the turtle module
import turtle

# Program presents itself to user
print("This program will draw the Olympic rings using turtle")

# Create and setup window for turtle. Background is white by default
window = turtle.Screen()
window.setup(1920, 1080)   # 1920, 1080 is the resolution of the window (Full HD)

# Create and setup turtle
breski = turtle.Turtle()    # Creates the cursor and sets it's name to breski
breski.shape("turtle")      # Defines the cursor's shape that will be used: Turtle

# Create blue ring of the Olympics
breski.penup()          # This will lift the turtle's pen so that he won't leave a trail when moving
breski.goto(-500, -50)  # Tells breski to go to this (x,y) coordinates
breski.color("blue")    # Sets color breski will use
breski.pensize(50)      # Sets the width of line breski leaves behind while moving to 50
breski.pendown()        # Lower pen so that breski will leave a trail behind while moving
breski.circle(200)      # Breski will draw a circle with a 200 radius

# Create black ring of the Olympics
# This code is a repeat of the 1st ring, but with different (x,y) coordinates and color
breski.penup()
breski.goto(0, -50)
breski.color("black")
breski.pensize(50)
breski.pendown()
breski.circle(200)

# Create red ring of the Olympics
# This code is a repeat of the 1st ring, but with different (x,y) coordinates and color
breski.penup()
breski.goto(500, -50)
breski.color("red")
breski.pensize(50)
breski.pendown()
breski.circle(200)

# Create yellow ring of the Olympics
# This code is a repeat of the 1st ring, but with different (x,y) coordinates and color
breski.penup()
breski.goto(-250, -250)
breski.color("gold")
breski.pensize(50)
breski.pendown()
breski.circle(200)

# Create green ring of the Olympics
# This code is a repeat of the 1st ring, but with different (x,y) coordinates and color
breski.penup()
breski.goto(250, -250)
breski.color("green")
breski.pensize(50)
breski.pendown()
breski.circle(200)

# Make window remain open after code execution until user clicks with mouse
window.exitonclick()
