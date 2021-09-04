# This program will give the perimeter, area, and angles of a triangle created through user input
# Steven Sousa / 4Cs / Python / 10-12-2020 / End date: 10/21/2020
# ***IMPORTANT***: I noticed that sometimes the program will fail depending on the values of the triangle
# prompting me a ValueError: math domain error. For example, if you use the values 5, 3, and 12
# for the lines, the code won't be able to calculate any angle. How can I overcome these errors?
# I hope I covered every mathematical information that you needed. This code took me a lot to figure out
# and to remember how to find angles. All in all, I did enjoy it as it really taught me how to research
# and insist in fixing my issues.

import math


# Create function that will determine if triangle is right-angled or not
def is_rightangled(base, side2, side3):
    """This function will check to see if the triangle is right-angled or not."""
    if side3 ** 2 == base ** 2 + side2 ** 2:
        return True
    else:
        return False


# ----------------------------------------------------------------------------------------------------------------------

# Declare variables that will create the triangle sides
base = float(input("What is the length of the base? "))
b = float(input("What is the length of the first side? "))
c = float(input("What is the length of the second side? "))

# ----------------------------------------------------------------------------------------------------------------------

# Check to see if inputs create a triangle and to see if it's right-angled
if base + b <= c or base + c <= b or b + c <= base:
    print("Sorry, that is an invalid triangle. ")
else:
    right_angled = is_rightangled(base, b, c)  # Calls function is inputs are valid
    print("Is the triangle right-angled? ", right_angled)  # Print results

# ----------------------------------------------------------------------------------------------------------------------

# Calculate perimeter of triangle
perimeter = base + b + c
perimeter = round(perimeter, 2)
print("The perimeter of this triangle is: ", perimeter)

# ----------------------------------------------------------------------------------------------------------------------

# Calculate the area of the triangle
s = 1/2 * (base + b + c)    # This will calculate the area of the triangle without the height.
area_of_triangle = math.sqrt(s * (s - base) * (s - b) * (s - c))
area_of_triangle = round(area_of_triangle, 2)
print("The area of the triangle is: ", area_of_triangle)

# ----------------------------------------------------------------------------------------------------------------------

# Calculate the height of the triangle
height = 2 * (area_of_triangle/base)
height = round(height, 2)
print("The height of the triangle is: ", height)

# ----------------------------------------------------------------------------------------------------------------------

# Determine the angles of the triangle using Law of Cosines
base1 = math.degrees(math.acos((base**2 + b**2 - c**2) / (2.0 * base * b)))
base1 = round(base1, 2)
print("Angle 1 is:", base1, "degrees.")

b = math.degrees(math.acos((b**2 + c**2 - base**2) / (2.0 * b * c)))
b = round(b, 2)
print("Angle 2 is:", b, "degrees.")

d = 180 - (base1 + b)    # Created variable d to differ from side c of the triangle
d = round(d, 2)
print("Angle 3 is: ", d, "degrees.")

# ----------------------------------------------------------------------------------------------------------------------

# Calculate the sum of angles. It should be equal to 180
sum_of_angles = base1 + b + d
print("The sum of angles is: ", sum_of_angles, "degrees.")

print()
print("Goodbye!")
