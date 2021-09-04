# Create a function that will receive 2 sides of a triangle and return the hypotenuse
# Steven Sousa - Exercise 6 - 10/20/2020

import math


# Create function that will calculate hypotenuse
def findHypot(side1, side2):
    hypot = math.sqrt(side1 ** 2 + side2 ** 2)
    return hypot


# Get 2 sides of the triangle
side1 = int(input("What is the length of side 1? "))
side2 = int(input("What is the length of side 2? "))

hypotenuse = findHypot(side1, side2)    # Call function
print("The hypotenuse is: ", hypotenuse)    # print hypotenuse
