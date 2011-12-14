def seive(n):
    erato = [False, True] * ((n // 2) + 1)
    erato[1] = False
    erato[2] = True

    d = 3

    while d*d <= n:
        if erato[d]:
            f = d*d
            while f <= n:
                erato[f] = False
                f += d
        d += 2

    primes = []

    for i in range(n+1):
        if erato[i]:
            primes.append(i)

    return primes
