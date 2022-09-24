# Add a print statement to Newton’s sqrt function that prints out better each time it is calculated.
# Call your modified function with 25 as an argument and record the results.
# Steven Sousa - Exercise 1 - 10/25/2020

def newtonSqrt(n):
    approx = 0.5 * n
    better = 0.5 * (approx + n / approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + n / approx)
        print("Better: ", better)
    return approx


print("Best approximation: ", newtonSqrt(25))
