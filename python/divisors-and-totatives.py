import itertools

def factorise(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    d = 3
    while d*d <= n:
        while n%d == 0:
            factors.append(d)
            n /= d
    if n > 1:
        factors.append(n)
    return factors

def subsets(xs):
    yield []
    for i in range(1, len(xs)):
        for c in itertools.combinations(xs, i):
            yield list(c)
    yield xs
    raise StopIteration

def divisors(n):
    factors = factorise(n)

    prod = lambda x: reduce(lambda x, y: x*y, x, 1)
    divisors = list(set(map(prod, subsets(factors))))
    divisors.sort()
    return divisors

def sum_divisors(n):
    return sum(divisors(n))

def num_divisors(n):
    return len(divisors(n))

def totatives(n):
    divs = divisors(n)
    divs.remove(1)

    ret = [x for x in range(1, n)]

    for d in divs:
        ret = [r for r in ret if r % d != 0]
    return ret

def totient(n):
    return len(totatives(n))
