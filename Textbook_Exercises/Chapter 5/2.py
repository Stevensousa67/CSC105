# Print 10 random numbers between 25 and 35 using a for statement
# Steven Sousa - Exercise 2 - 10/4/2020

# Import random module
import random

# Create the for loop
for repetition in range(10):
    random_number = random.randrange(25, 36)    # random number between 25 and 35. Always has to go 1 above the limit.
    print(random_number)

# End program
print("Goodbye")
