from praxis import gcd

def compute_wheel(primes):
    circum = reduce(lambda x,y: x*y, primes, 1)
    spokes = []

    for i in range(1, circum):
        if gcd(i, circum) == 1:
            spokes.append(i)

    diffs = []
    for i,s in enumerate(spokes[:-1]):
        diffs.append(spokes[i+1] - s)
    diffs.insert(0, circum - spokes[-1] + 1)

    start = primes[-1]
    prime = False
    while not prime:
        prime = True
        start += 1
        for p in primes:
            if start % p == 0:
                prime = False
                break
    
    return start, diffs

def wheel_factorise(n):
    primes = [2,3,5,7]
    factors = set([])

    for p in primes:
        while n % p == 0:
            factors.add(p)
            n /= p

    d, diffs = compute_wheel(primes)

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
