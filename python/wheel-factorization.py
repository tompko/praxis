from praxis import gcd, seive

def compute_wheel(limit):
    primes = seive(limit)
    circum = reduce(lambda x,y: x*y, primes, 1)
    spokes = [i for i in range(1, circum) if gcd(i, circum) == 1]
    diffs = [spokes[i+1] - s for i,s in enumerate(spokes[:-1])]
    diffs.insert(0, circum - spokes[-1] + 1)

    return primes, diffs

def wheel_factorise(n):
    factors = set([])
    d = 11
    primes, diffs = compute_wheel(d)

    for p in primes:
        while n % p == 0:
            factors.add(p)
            n /= p

    while d*d <= n:
        while n % d == 0:
            factors.add(d)
            n /= d
        d += diffs[0]
        diffs = diffs[1:] + diffs[:1]

    if n > 1:
        factors.add(n)
    ret = list(factors)
    ret.sort()
    return ret
