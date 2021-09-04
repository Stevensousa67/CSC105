# Write a recursive function to compute the Fibonacci sequence.
# How does the performance of the recursive function compare to that of an iterative version?
# Steven Sousa - Exercise 5 - 10/31/2020

def fibonacci(n):
    """This function will give a Fibonacci sequence recursively."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n = int(input("How many times will the fibonacci sequence occur? "))

# Test for valid input
if n < 0:
    print("Please enter a positive number. ")

else:
    print("Fibonacci sequence with", n, "terms:")
    for a in range(n):
        print(fibonacci(a))

# Code explanation: by doing a for loop to call the function, the value of a will always start with 0 and
# go up every time the function is called. By starting with 0, the function will return a (0).
# A then goes to 1, and the function returns 1. A then goes to 2 and the function will execute the else
# statement. it will call the function again send (a-1) + (a-2) which means, 2-1 (1) + 2-2 (0) = 1 and prints 1.
# A then is equal to 3. Function does 3-1 (2) + 3-2 (1) and prints 3.

