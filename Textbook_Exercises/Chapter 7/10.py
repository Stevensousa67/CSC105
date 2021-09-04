# Write a function that will tell if a triangle is right_angled.
# Steven Sousa - Exercise 10 - 10/20/2020

# Create function
def is_rightangled(base, side2, side3):
    if side3 ** 2 == base ** 2 + side2 ** 2:
        return True
    else:
        return False


# Ask user for length of all 3 sides of the triangle
base = float(input("What is the length of the base? "))
side2 = float(input("What is the second length? "))
side3 = float(input("What is the third length (It should be the largest side? "))

# Check to see if the inputs are valid
if side3 > base and side3 > side2:
    rightangled = is_rightangled(base, side2, side3)    # Calls function is inputs are valid
    print("Is the triangle right-angled? ", rightangled)    # Print results
else:
    print("Sorry, but the third side has to be larger than the other 2 sides.")  # If results are invalid
