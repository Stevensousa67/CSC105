import turtle

window = turtle.Screen()
breski = turtle.Turtle()
breski.shape("turtle")

# Ask user for number of sides from polygon
sides = int(input("How many sides will the polygon have? "))
angle = 360/sides

# Ask user for length of side
length = int(input("How long each side going to be? "))

# Ask user what color the outline of the polygon will be
ol = input("What color will be the outline of the polygon? ")
breski.pencolor(ol)

# Ask user what color will fill the polygon
fc = input("What color will be the polygon? ")
breski.fillcolor(fc)
breski.begin_fill()

# Draw polygon
for polygon in range(sides):
    breski.forward(length)
    breski.left(angle)

breski.end_fill()

window.exitonclick()
