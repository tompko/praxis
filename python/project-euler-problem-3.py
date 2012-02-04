def factor(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n /= 2

    f = 3

    while n > f*f:
        while n % f == 0:
            factors.append(f)
            n /= f
        f += 2
    if n > 1:
        factors.append(n)

    return factors
