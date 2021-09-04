# Rocket science:
# Write a program that asks the user for an initial launch angle in degrees, the initial velocity in m/sec.
# Calculate the x and y coordinates for the path using the initial angle,
# velocity and a value for elapsed time between points.
# Store the results in one or more lists and print out the results.   Use the stored data to plot a curve using Turtle.
# Alogrithms:       Xcoord = initialVelocity x cos(initialAngle) x time
#                   Ycoord = initialVelocity x sin(initialAngle) x time – ½ x 9.8 x time2
# (Hint: you may want to use some factor against the coordinate values to get a visible plot
# and don’t forget to make the dot big enough to see!)
# Steven Sousa - Rocket Science - 11/21/2020

import math
import time

# A) Ask user for initial launch angle and initial velocity
initial_angle = float(input("What is the initial launch angle in degrees of the rocket? "))
initial_velocity = float(input("What is the initial velocity in m/s of the rocket? "))

# B) Calculate the x and y coordinates for the path using initial angle, velocity, and a value for elapsed time.
x_coor = initial_velocity * math.cos(initial_angle) *
y_coor = initial_velocity * math.sin(initial_angle) *

# C) Store results in a one or more lists and print the results
results = []
