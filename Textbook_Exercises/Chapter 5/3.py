# Create a program that will use the Pythagorean Theorem using math module
# Steven Sousa - Exercise 3 - 10/4/2020

# Import random module
import math

# Ask user for width and length of triangle
width = int(input("What is the width of the triangle? "))
length = int(input("What is the length of the triangle? "))
hypotenuse = math.hypot(width, length)  # math.hypot is the math function that calculates the hypotenuse.

# Print the hypotenuse
print("The hypotenuse is: ", hypotenuse)

# End program
print()
print("Goodbye")
