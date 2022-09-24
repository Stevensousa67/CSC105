# Write a function that will return the number of digits in an integer.
# Steven Sousa - Exercise 5 - 11/14/2020

def count_int_digits(x):
    """ This function will count how many digits an integer has."""
    number_string = str(x)              # Converts int variable to string
    return print(len(number_string))    # Use len function to see how many character in string


number = int(input("What is the integer? "))
count_int_digits(number)
