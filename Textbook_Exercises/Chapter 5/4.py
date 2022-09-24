# Create a program that will print pi using arithmetic and print the math module pi to see difference
# Steven Sousa - Exercise 4 - 10/4/2020

# Professor: My thinking was creating a "dummy pie" so that I could find the circumference of the circle.
# Because of the formula = circumference = 2 * pi * radius
# I created a dummy pi for that formula and created the "real pi" to be found using arithmetic.
# My trouble is that the arithmetic pi has the same number of decimal points as I define in the dummy pi.
# Is there something wrong with my code or is that expected?

# import math function
import math

# Define a dummy pi for the calculation of the circumference
dummy_pi = 3.1415

# Ask user for circumference of circle
radius = int(input("What is the radius of the circle? "))
circumference = 2 * dummy_pi * radius
diameter = radius * 2

# Calculate pi based on above values
pi = circumference/diameter
print("Arithmetic pi: ", pi)

# print the math.pi value
math_pi = math.pi
print("Pi from math module is: ", math_pi)

# End program
print()
print("Goodbye")
