# Modify program from 10 so that the sides can be given to the function in any order
# Steven Sousa - Exercise 11 - 10/28/2020

# Create function
def is_rightangled(a, b, c):
    is_rightangled = False

    if a > b and a > c:
        is_rightangled = abs(b**2 + c**2 - a**2) < 0.001
    elif b > a and b > c:
        is_rightangled = abs(a**2 + c**2 - b**2) < 0.001
    else:
        is_rightangled = abs(a**2 + b**2 - c**2) < 0.001
    return is_rightangled


# Ask user for length of all 3 sides of the triangle
base = float(input("What is the length of the base? "))
side2 = float(input("What is the second length? "))
side3 = float(input("What is the third length (It should be the largest side? "))

# Check to see if the inputs are valid
if side3 > base and side3 > side2:
    rightangled = is_rightangled(side2, base, side3)    # Calls function if inputs are valid
    print("Is the triangle right-angled? ", rightangled)    # Print results
else:
    print("Sorry, but the third side has to be larger than the other 2 sides.")  # If results are invalid
