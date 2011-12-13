import random

def miller_rabin(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    m = n - 1

    r, s = 0, 1
    while m % 2 == 0:
        m /= 2
        r += 1

    for q in range(k):
        a = random.randrange(2, n-1)

        if pow(a, s, n) == 1:
            return False

        for i in range(r):
            if pow(a, (2**i) * s, n) == n - 1:
                return False

    return True
