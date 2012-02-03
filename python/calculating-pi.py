import random
import math

def monte_carlo(n):
    hits = 0

    for i in range(n):
        a, b = random.random(), random.random()
        if a**2 + b ** 2 < 1:
            hits += 1

    return (float(hits) * 4) / float(n)

def archimedes(n):
    a, b = 3 * math.sqrt(3), 3 * math.sqrt(3.0)  / 2.0

    for i in range(2, n):
        a = (2 * a * b) / (a + b)
        b = math.sqrt(b * a)

    return b, a
