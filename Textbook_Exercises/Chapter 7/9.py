# Write a odd function that calls even function to determine if x is odd
# Steven Sousa - Exercise 9 - 10/20/2020

# Create function
def is_even(x):
    if x % 2 == 0:  # Checks to see if the number is divisible by 2
        return False

    else:
        return True

def is_odd(x):
    x = is_even(x)
    return x


# Ask user for a number
x = int(input("What number do you want to check to see if it's odd? "))
x = is_odd(x)  # Call function
print(x)    # Print the return value
