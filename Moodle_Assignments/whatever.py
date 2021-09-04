# count number of prime numbers.

class Solution:
    def countPrimes(self, n: int) -> int:
        """This function will count how many prime numbers"""
        counter = 0
        for a in range(2, n):
            if self.is_prime(a):
                counter += 1
        return counter

    def is_prime(self, b):
        """This function will check if a number is prime."""
        for c in range(2, b):
            if c <= b/c:
                if b % c == 0:
                    return False
            else:
                return True
        return True

s = Solution()
print(s.countPrimes(1000000))
