# Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.
# A call to print_triangular_numbers(5) would produce the following output:
# Steven Sousa - Exercise 2 - 10/25/2020

def print_triangular_numbers(n):
    """Prints a table with triangle number to the left and number of dots to the right"""
    x = 1   # Set accumulator to 1 so that the first triangle will have 1 dot
    while x <= n:
        for triangle_number in range(1, n + 1):     # range 1 through user input
            number_of_dots = (x * (x + 1)) / 2      # formula for the triangular number
            number_of_dots = int(number_of_dots)
            x = x + 1                               # add 1 to the accumulator
            print(triangle_number, '\t', number_of_dots)    # print results in table format


n = int(input("How many triangles? "))
print_triangular_numbers(n)
