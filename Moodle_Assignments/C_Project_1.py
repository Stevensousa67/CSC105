"""
This program is for Procedural Programming Project 1 assignment. This assignment has the purpose of comparing the
Python version against the C version of the same program, including code, writing process, and runtime.

This program will calculate the gross and net paycheck from a worker based on hourly wage of $20 and working 40h.
The tax rates are: State Tax: 5%, Federal Tax: 10%, and Social Security Tax: 7.5%

Steven Sousa / Procedural Programming / 4Cs / 04-12-21
"""

# Import necessary dependencies
import time

# Program introduces itself to the user
print("Welcome to the paycheck calculator. The compensation is $20/h.")

# Program asks for how many times it will execute this program for runtime study purpose
number_of_times_program_repeats = int(input("How many times do you want this program to repeat itself? "))

# Start time count
# **ATTENTION**: Comment line 22 and uncomment line 23. Unix uses time.clock() instead of time.time(). See line 54.
clock_start = time.time()
# clock_start = time.clock()

while number_of_times_program_repeats > 0:

    # Program prints which iteration it is at
    print("Program is at iteration ", number_of_times_program_repeats)

    # Program calculates and prints the gross pay (40h work week and $20/h compensation).
    gross_pay = (40 * 20)
    print(f"Gross income: ${gross_pay}")

    # Program calculates and prints each taxes
    state_tax = (gross_pay * .05)
    print(f"State tax: ${state_tax}")

    federal_tax = (gross_pay * .10)
    print(f"Federal tax: ${federal_tax}")

    social_security_tax = (gross_pay * .075)
    print(f"Social Security tax: ${social_security_tax}")

    # Program prints total amount of taxes withheld
    total_taxes = (state_tax + federal_tax + social_security_tax)
    print(f"Total taxes: ${total_taxes}")

    # Program prints net pay and ends
    print(f"Net pay: ${gross_pay - total_taxes}\n")

    # Reduce loop count by 1
    number_of_times_program_repeats = number_of_times_program_repeats - 1

# **ATTENTION**: Comment line 55 and uncomment line 56. Same reasons as above.
clock_end = time.time()
# clock_end = time.clock()
time_spent = clock_end - clock_start
print(f"Time spent to run the program: {time_spent :.3f} seconds")
