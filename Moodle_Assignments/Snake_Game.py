# Snake Game in a Spooky Halloween Ghost buster theme!
# By Christopher Kulpa, Christopher Thurston, Kathleen Clark,and Steven Sousa

# with instruction to import sound by https://youtu.be/8v6xkT0lLaQ
# to also show potential errors with https://gist.github.com/MrDMurray/fc11585c2072f0dff04b3d0f7c988b72

# music converted from https://youtu.be/e5lcETwAItA

# With reference to https://www.geeksforgeeks.org/turtle-onkey-function-in-python/
# and https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900

import turtle  # importing the module to get the turtle
import time  # importing time to allow us to set delays in the program so everything doesn't happen all at once
import random  # importing random to allow the use of random integers specifically for the foods
import winsound  # by importing winsound we are able to add music to our game!

delay = 0.1  # here's the delay function starting to give the code a second to process

# Setting up the score
score = 0  # by  setting the score value to be 0 it starts the game off with a 0 score and a 0 high score
high_score = 0  # see above comment

# Setting up the play field for the game!
wn = turtle.Screen()
wn.title("SnakeBusters")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)  # Turns off the screen updates

# Setting up the head of the snake
snakehead = turtle.Turtle()
snakehead.speed(0)
snakehead.shape("square")
snakehead.color("white")
snakehead.penup()
snakehead.goto(0, 0)
snakehead.direction = "stop"

# Making the snake food and coloring it orange to fit in the theme of the holidays and naming it pumpkin
pumpkin = turtle.Turtle()
pumpkin.speed(0)
pumpkin.shape("circle")
pumpkin.color("orange")
pumpkin.penup()
pumpkin.goto(0, 100)

segments = []  # establishing the "segments" to be an array

# The pen function enables the ability to write things out in the turtle window without making a new turtle
pen = turtle.Turtle()  # still need to make a turtle however and set the characteristics you want the turtle to have
pen.speed(0)
pen.shape("square")
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)  # where you want the writing to be
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 20, "normal"))


# using pen.write makes it so that it writes out what could also be a print statement
# by setting the fonts location and font size

# The controls of the game are listed below with the use of def statements
# and naming them the direction we want the snake to go
def go_up():
    if snakehead.direction != "down":  # the if statement makes it so if the snake is going down,
        # it cant double back on itself and go up
        snakehead.direction = "up"


def go_down():
    if snakehead.direction != "up":  # making sure the snake cant go up if its already going down
        snakehead.direction = "down"


def go_left():
    if snakehead.direction != "right":  # same with right to left
        snakehead.direction = "left"


def go_right():
    if snakehead.direction != "left":  # and left to right
        snakehead.direction = "right"


def move():  # now that we have set up the definitions need to set up the constant movement
    if snakehead.direction == "up":
        y = snakehead.ycor()
        snakehead.sety(y + 20)

    if snakehead.direction == "down":
        y = snakehead.ycor()
        snakehead.sety(y - 20)

    if snakehead.direction == "left":
        x = snakehead.xcor()
        snakehead.setx(x - 20)

    if snakehead.direction == "right":
        x = snakehead.xcor()
        snakehead.setx(x + 20)


# Binding the definitions to key presses! aka Making the controls for the game!
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# this will put in the music for the game! which Steven converted to a .wav format
winsound.PlaySound('Ghostbusters.wav', winsound.SND_ASYNC)

# This is where the individual pieces of the game meet together by making a game loop!
while True:  # this sets up all of the pieces to function together. while setting it to always be false
    wn.update()

    # We dont want the turtle (snake in the game) to leave the surrounding window so we set up walls for the snake
    if snakehead.xcor() > 390 or snakehead.xcor() < -390 or snakehead.ycor() > 390 or snakehead.ycor() < -390:
        # if 0,0 is the dead center it can not move  beyond the four coordinates listed in this line
        time.sleep(1)
        snakehead.goto(0, 0)
        snakehead.direction = "stop"
        # have to make the snake stop when it hits those coordinates
        # and give the player a moment to realize "oh I died because I hit the wall"

        # Hide the segments this makes it so that segments can be loaded into the game without the player seeing them
        for segment in segments:
            segment.goto(1000, 1000)  # hiding them way over in x 1000 and y 1000

        # Clear the segments list
        segments.clear()  # this makes it so that the snake length  cant be carried over from game to game

        # Reset the score back to 0 on death
        score = 0

        # Reset the delay to 0.1 to give a moment to reset everything so the player can see whats happening
        delay = 0.1

        # This section sets the score to be saved when you've reached your high score!
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))

        # Now we need to make the snake eat the food!
        # and not just eat the food but make it move around the field randomly
    if snakehead.distance(pumpkin) < 20:
        # Move the food to a random spot
        x = random.randint(-380, 380)
        y = random.randint(-380, 380)
        pumpkin.goto(x, y)

        # When the snake eats we need to make the snake grow in length
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)  # by appending this, the append function adds to the end of the list.
        # aka adding the body length to the end of the snake after it eats a food

        # Shorten the delay, makes adding to the snake body happen without a delay too the game state
        delay -= 0.001

        # We have to show how good we are at this game! Do this by adding 10 points to the score for each food consumed
        score += 10

        if score > high_score:
            high_score = score
            # if our current score is higher than high score it should save for when the window is open!
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))
        # this updates the score fields.

        # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):  # len statements dictate the length of an array
        x = segments[index - 1].xcor()  # these index commands establish the x field
        y = segments[index - 1].ycor()  # these index commands establish the y fields
        segments[index].goto(x, y)  # this will attach the segments head of the snake

    # Move segment 0 to where the head is making the body meet the head of the snake
    if len(segments) > 0:  # this makes sure that there is no gap in the body of the snake
        x = snakehead.xcor()  # cant have a snake without its body attached!
        y = snakehead.ycor()
        segments[0].goto(x, y)  # this establishes that it moves with the snake body

    distance_entry()  # make the body move! so we have a snake and not a slug trail

    # Check for head collision with the body segments because if a snake eats itself it would die!
    for segment in segments:
        if segment.distance(snakehead) < 20:
            time.sleep(1)
            snakehead.goto(0, 0)
            snakehead.direction = "stop"

            # Hide the segments because it needs to have the same kill conditions
            # as if it hit the wall of the play field
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 20, "normal"))

    time.sleep(delay)
