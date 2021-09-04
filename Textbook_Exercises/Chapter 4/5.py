import turtle

window = turtle.Screen()
breski = turtle.Turtle()
breski.shape("turtle")
breski.color("red")
breski.penup()

# Draw triangle
for triangle in range(3):
    breski.forward(50)
    breski.left(120)

# Draw square
for square in range(4):
    breski.forward(90)
    breski.left(90)

# Draw hexagon
for hexagon in range(6):
    breski.forward(90)
    breski.left(60)

# Draw octagon
for octagon in range(8):
    breski.forward(90)
    breski.left(45)

window.exitonclick()
