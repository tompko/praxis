"""Happy Numbers: Iterating the sum of the squares of the digits terminates
with one"""

def sum_of_squares(n):
    """Return the sum of the squares of the digits of n"""
    ret = 0
    while n:
        ret += (n % 10) ** 2
        n = n // 10
    return ret

def happy(n):
    """Return True when n is a happy number, False otherwise

    A happy number is defined by the following process. Starting with any
    positive integer, replace the number by the sum of the squares of its
    digits, and repeat the process until the number equals 1 (where it will
    stay), or it loops endlessly in a cycle which does not include 1. Those
    numbers for which this process ends in 1 are happy numbers, while those
    that do not end in 1 are unhappy numbers (or sad numbers).
    [http://en.wikipedia.org/wiki/Happy_number]
    """
    encountered = set()

    while n != 1:
        encountered.add(n)
        n = sum_of_squares(n)
        if n in encountered:
            return False
    return True
