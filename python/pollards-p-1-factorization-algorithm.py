import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def pollard(n):
    b = 10
    a = random.randrange(2, n - 1)

    while b <= 10**6:
        k = reduce(lcm, range(1, b+1))
        g = gcd(a, n)

        if g > 1:
            return g
        d = gcd(a**k - 1, n)

        if 1 < d < n:
            return d
        if d == 1:
            b *= 10
        if d == n:
            a = random.randrange(2, n-1)

    return -1
