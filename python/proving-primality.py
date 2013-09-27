def factorise(n):
    factors = set()

    while n % 2 == 0:
        factors.add(2)
        n /= 2

    d = 3
    while d*d <= n:
        while n % d == 0:
            factors.add(d)
            n /= d
        d += 2

    if n > 1:
        factors.add(n)

    ret = list(factors)
    ret.sort()
    return ret

def LucasTest(n):
    qs = factorise(n - 1)

    if n % 2 == 0:
        return n == 2

    b = 2
    while b < n:
        if pow(b, n - 1, n) == 1:
            prime = all([pow(b, (n-1)/q, n) != 1 for q in qs])
            if prime:
                return True
        else:
            return False
        b += 1
    return False
