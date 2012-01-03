import random

def e(n):
    sumf = 0.0
    count = 1.0

    for i in range(n):
        sumf += random.random()
        if sumf > 1.0:
            count += 1.0
            sumf = 0.0

    return  n / count
