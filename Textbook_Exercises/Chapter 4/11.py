# Draw the deck shapes figure

import turtle

window = turtle.Screen()
window.setup(1920, 1080)
breski = turtle.Turtle()

# Draw the Spades
breski.penup()
breski.goto(-700, 0)
breski.pendown()
breski.fillcolor("black")
breski.begin_fill()

breski.backward(-17)
breski.forward(100)
breski.left(90)
breski.forward(5)
breski.left(90)
for a in range(100):
    breski.forward(1)
    breski.right(1)

breski.right(140)


def heart_curve_upside_down():
    for b in range(200):
        breski.forward(1)
        breski.left(1)


heart_curve_upside_down()
breski.forward(111.65)
breski.left(80)
breski.forward(111.65)
heart_curve_upside_down()

breski.right(144)
for c in range(100):
    breski.forward(1)
    breski.right(1)

breski.left(90)
breski.forward(4)
breski.left(90)
breski.end_fill()

# Draw Hearts
breski.penup()
breski.goto(-200, 0)
breski.pendown()
breski.fillcolor("red")
breski.begin_fill()


# Create function for the top curves of a heart
def heart_curve():
    for d in range(200):  # 200 is a good number for the amount of repeats needed
        breski.right(1)  # 1 is ideal in order for the turtle not to turn right too much
        breski.forward(1)  # 1 is ideal for the turtle not move forward too much
        # This will generate a symmetrical double curve of the heart when called twice.


breski.left(145)  # This turns breski left 145 degrees to make the straight diagonal line
breski.forward(120)  # This will make the left diagonal line of the heart
heart_curve()  # Call the function to do the left curve of the heart

breski.left(120)  # turns breski 120 degrees to start the right curve of the heart
heart_curve()  # Calls the function to do the right curve
breski.forward(120)
breski.up()
breski.end_fill()  # Stops coloring the heart

# Draw Diamonds
breski.home()
breski.goto(200, 0)
breski.pendown()
breski.fillcolor("red")
breski.begin_fill()

breski.left(60)
breski.forward(120)
breski.left(60)
breski.forward(120)
breski.left(120)
breski.forward(120)
breski.left(60)
breski.forward(120)
breski.penup()
breski.end_fill()

# Draw Clubs
breski.home()
breski.penup()
breski.goto(600, 0)
breski.pendown()
breski.fillcolor("Black")
breski.begin_fill()
breski.backward(-17)
breski.forward(100)
breski.left(90)
breski.forward(5)
breski.left(90)

for e in range(100):
    breski.forward(1)
    breski.right(1)

breski.right(140)

# Draw left curve
for f in range(260):
    breski.forward(1)
    breski.left(1)

breski.right(140)

# Draw top curve
for g in range(240):
    breski.forward(1)
    breski.left(1)

breski.right(140)

# Draw right curve
for h in range(260):
    breski.forward(1)
    breski.left(1)

breski.right(140)

for i in range(100):
    breski.forward(1)
    breski.right(1)

breski.left(90)
breski.forward(5)
breski.left(90)
breski.forward(100)
breski.end_fill()

window.exitonclick()
