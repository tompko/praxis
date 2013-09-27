def seive(n):
    erato = [False,False,True] + [True, False] * ((n // 2) + 1)
    d = 3

    while d*d <= n:
        if erato[d]:
            f = d*d
            while f <= n:
                erato[f] = False
                f += d
        d += 2

    primes = [i for i in range(n) if erato[i]]

    return primes
