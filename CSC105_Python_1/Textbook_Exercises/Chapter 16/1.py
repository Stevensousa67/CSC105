# Write a recursive function to compute the factorial of a number.
# Steven Sousa - Exercise 1 - 10/29/2020

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("What number would you like to find the factorial? "))
if n < 0:
    print("Please choose a positive number.")
else:
    factorial(n)
    print(factorial(n))