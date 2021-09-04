# Write a function that returns True for even number and False for odd number
# Steven Sousa - Exercise 7 - 10/20/2020

# Create function
def is_even(x):
    if x % 2 == 0:  # Checks to see if the number is divisible by 2
        return True

    else:
        return False


# Ask user for a number
x = int(input("What number do you want to check to see if it's even? "))
x = is_even(x)  # Call function
print(x)    # Print the return value
