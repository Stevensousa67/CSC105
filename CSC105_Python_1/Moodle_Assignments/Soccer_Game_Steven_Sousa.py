# Soccer game using turtle
# Steven Sousa / Python / 4Cs / 10-29-2020

# Notes: The only thing I couldn't fix was the boundaries if the kick was too "strong" and sent the ball outside.
# I couldn't figure out a way to avoid letting the ball go outside if the kick was too strong. Could you implement it
# in the code for me to see? I thought about doing something like this (pseudo code): if kick would place ball outside
# of boundaries, make the ball hit edge of screen and go back to 0,0.

# Import necessary modules ---------------------------------------------------------------------------------------------

import turtle
import random
import time

# Create necessary variables -------------------------------------------------------------------------------------------

player1_score = 0
player2_score = 0


# Create necessary functions -------------------------------------------------------------------------------------------

# Create random xy coordinates
def random_movement(x, y):
    """This function will generate a random xy coordinate for the ball to go."""
    global ball, player1_score, player2_score
    ball1 = random.randint(1, 200)
    ball2 = random.randint(1, 360)  # ball2 variable is used to store the random ycor in degrees

    # Create field boundaries ------------------------------------------------------------------------------------------

    if ball.xcor() <= -910 or ball.xcor() >= 910 or ball.ycor() <= -510 or ball.ycor() >= 510:
        ball.direction = "stop"
        time.sleep(1)
        ball.goto(0, 0)

    # Create the scoring mechanism -------------------------------------------------------------------------------------

    # Scoring mechanism for player 1
    if ball.xcor() >= 900 and -200 <= ball.ycor() <= 200:
        ball.direction = "stop"
        player1_score += 1
        time.sleep(1)
        scoreboard.clear()
        scoreboard.write("Player 1 Score: {}  Player 2 Score: {}".format(player1_score, player2_score),
                         align="center", font=("Courier", 20, "normal"))
        ball.goto(0, 0)

    # Scoring mechanism for player 2
    if ball.xcor() <= -910 and -200 <= ball.ycor() <= 200:
        ball.direction = "stop"
        player2_score += 1
        time.sleep(1)
        scoreboard.clear()
        scoreboard.write("Player 1 Score: {}  Player 2 Score: {}".format(player1_score, player2_score),
                         align="center", font=("Courier", 20, "normal"))
        ball.goto(0, 0)

    # Make the game stop is player 1 reaches 5 points
    if player1_score == 5:
        time.sleep(1)
        ball.home()
        ball.direction = "stop"
        scoreboard.home()
        scoreboard.write("Victory to Player 1!", align="center", font=("Courier", 20, "normal"))

    # Make the game stop is player 2 reaches 5 points
    if player2_score == 5:
        time.sleep(1)
        ball.home()
        ball.direction = "stop"
        scoreboard.home()
        scoreboard.write("Victory to Player 2!", align="center", font=("Courier", 20, "normal"))

    # Make ball turn in random angle and move a random distance
    ball.setheading(ball2)
    ball.forward(ball1)

    window.listen()
    window.onkeypress(reset_game, "r")
    window.onkeypress(quit_game, "q")


# Create keybinding
def reset_game():
    """This function will make sure that upon pressing r, the game resets."""
    global ball, scoreboard, player1_score, player2_score
    time.sleep(1)
    ball.direction = "stop"
    ball.home()
    scoreboard.clear()
    player1_score = 0
    player2_score = 0
    scoreboard.write("Player 1 Score: {}  Player 2 Score: {}".format(player1_score, player2_score),
                     align="center", font=("Courier", 20, "normal"))


def quit_game():
    """This function will make the game stop and exit upon pressing q"""
    quit()


# Create Window --------------------------------------------------------------------------------------------------------

window = turtle.Screen()
window.setup(1920, 1080)
window.bgcolor("green")
window.title("Soccer Game")

# Create turtle that will draw the field -------------------------------------------------------------------------------

breski = turtle.Turtle()
breski.pensize(5)
breski.color("white")
breski.hideturtle()
breski.speed(0)

# Drawing the field ----------------------------------------------------------------------------------------------------

# Creating the half field line and center circle
breski.circle(30)
breski.penup()
breski.goto(0, -500)
breski.left(90)
breski.pendown()
breski.forward(1060)
breski.penup()
breski.home()

# Create left side goal
breski.goto(-960, 200)
breski.pendown()
breski.forward(60)
breski.right(90)
breski.forward(400)
breski.right(90)
breski.forward(60)
breski.penup()

# Create right side goal
breski.goto(960, 200)
breski.pendown()
breski.forward(60)
breski.left(90)
breski.forward(400)
breski.left(90)
breski.forward(60)

# Create ball turtle
ball = turtle.Turtle()
ball.home()
ball.shape("circle")
ball.color("blue")
ball.penup()

# Create scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("black")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 500)
scoreboard.write("Player 1 Score: 0  Player 2 Score: 0", align="center", font=("Courier", 20, "normal"))

# Make screen listen for key presses -----------------------------------------------------------------------------------
window.listen()
window.onkeypress(reset_game, "r")
window.onkeypress(quit_game, "q")

# Create main game loop
# Make ball move upon click
ball.onclick(random_movement)
window.mainloop()
