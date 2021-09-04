# Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.
# Steven Sousa - Exercise 12 - 10/28/2020

def isLeap(x):
    """This function determines if year is leap or not."""
    isLeap = False

    if x % 4 == 0:                      # Check to see is divisible by 4
        if x % 100 == 0:                # If it is, check for 100
            if x % 400 == 0:            # It it is too, check for 400
                return True             # if yes to all, return true
            else:
                return isLeap           # if not by 400, return false
        return True                     # if not by 100, return true
    return isLeap                       # if not by 4, return false


year = int(input("What year would you like to check if its leap or not? "))
result = isLeap(year)
print(result)
