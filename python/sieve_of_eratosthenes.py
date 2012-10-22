"""Sieve of Eratosthenes: A Python implementation of an ancient algorithm"""

import unittest

def sieve(n):
    """Return a list of all primes less than n"""
    #All even numbers except 2 are not primes
    primes = [False, False, True] + [True, False] * (n / 2)

    #Start with 3
    p = 3

    while p*p <= n:
        if primes[p]:
            #p is prime, cross off all multiples of p, starting at the square 
            #of p since all smaller multiples have already been crossed off
            d = p*p
            while d <= n:
                primes[d] = False
                d += p
        p += 2

    #Build a list of the primes we've found
    return [i for i in range(n) if primes[i]]

class TestSieve(unittest.TestCase):
    """Test the sieve of eratosthenes

    Perform two tests: one against lists of primes less than a number; one
    against the number of primes less than a number.
    """
    def test_primes_under_10(self):
        """Test the primes under 10 and 100"""
        self.assertEqual(sieve(10), [2, 3, 5, 7])
        self.assertEqual(sieve(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
        37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_primes_under_1000000(self):
        """Check the lengths of the list of primes up to 1000000"""
        self.assertEqual(len(sieve(100)), 25)
        self.assertEqual(len(sieve(1000)), 168)
        self.assertEqual(len(sieve(10000)), 1229)
        self.assertEqual(len(sieve(100000)), 9592)
        self.assertEqual(len(sieve(1000000)), 78498)

if __name__ == "__main__":
    unittest.main()
