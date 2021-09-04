# Implement the calculator for the date of Easter. The following algorithm computes the date for Easter Sunday for any
# year between 1900 to 2099. Ask the user to enter a year. Compute the following:
# a = year % 19
# b = year % 4
# c = year % 7
# d = (19 * a + 24) % 30
# e = (2 * b + 4 * c + 6 * d + 5) % 7
# dateofeaster = 22 + d + e
# Special note: The algorithm can give a date in April. Also, if the year is one of four special years
# (1954, 1981, 2049, or 2076) then subtract 7 from the date. Your program should print an error message if the user
# provides a date that is out of range.
# Steven Sousa - Exercise 13 - 10/28/2020

year = int(input("Please provide a year between 1900 and 2099: "))

# Check if year is in range
if not 1900 <= year <= 2099:
    print("Please provide a year within the stated range. ")
else:
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    easter = 22 + d + e

    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        easter = easter - 7

    if easter > 31:                     # if easter day is over 31
        print("April", easter - 31)     # subtract 31 from easter so that it will be a valid April date
    else:
        print("March", easter)          # if not over 31, easter will be in March
