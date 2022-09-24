# Write a function, is_prime, that takes a single integer argument and returns True
# when the argument is a prime number and False otherwise.
# Steven Sousa - Exercise 3 - 10/26/2020

def is_prime(n):
    """This function checks if a number n is prime or not"""
    for a in range(2, n):  # hence why range starts at 2 and ends at n
        if n % a == 0:     # if the remaining of n / a == 0, then n has a factor
            return False
    return True            # Keeping return True outside the for allows 2 to return as True.


n = int(input("What number do you want to check if it's prime? "))
print(is_prime(n))
