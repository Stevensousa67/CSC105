# Write a function that returns True for odd number and False for even number
# Steven Sousa - Exercise 8 - 10/20/2020

# Create function
def is_odd(x):
    if x % 2 != 0:  # If x doesn't divide by 2, then it's odd
        return True

    else:
        return False


# Ask user for a number
x = int(input("What number do you want to check to see if it's odd? "))
x = is_odd(x)  # Call function
print(x)    # Print the return value
