# Write a function that reverses its string argument.
# Steven Sousa - Exercise 6 - 11/14/2020

def reverse_string(string):
    """ This function will reverse a string"""
    reversed = ""                                   # Create empty string
    for index in range(len(string)-1, -1, -1):      # Iterate through each char using len
        reversed = reversed + string[index]         # reversed acquires each letter from string

    return reversed


word = str(input("What is the word? "))
print("Reversed string: ", reverse_string(word))
