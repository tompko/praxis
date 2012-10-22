"""Caclulate kappa(n) - the number of prime partitions of a number n"""

import itertools

from sieve_of_eratosthenes import sieve

def kappa(num):
    """Calculate the number of prime partitions of a number num

    A prime partition of a number is a set of primes which sum to that number.
    """
    #First calculate a list of sum of prime factors
    #using a sieve
    sopf = [0 for i in range(num + 1)]
    
    for i in range(2, num+1, 2):
        sopf[i] = 2

    pri = 3
    while pri <= num:
        if sopf[pri] == 0:
            div = pri
            while div <= num:
                sopf[div] += pri
                div += pri
        pri += 2

    #Calculate each successive kappa from 2 to num
    #Each kappa relies on the smaller kappas in its calculation
    kaps = [0 for i in range(num + 1)]

    for n in range(2, num+1):
        kaps[n] = sopf[n] + sum([sopf[n - j] * kaps[j] for j in range(1, n)])
        kaps[n] /= n

    return kaps[num]

def prime_partitions(num):
    """Calculate a list of all prime partitions of num"""
    parts = {}

    parts[0] = set([()])
    parts[1] = set([])
    primes = sieve(num+1)

    for n in range(2, num + 1):
        parts[n] = set()
        for p in itertools.takewhile(lambda x: x <= n, primes):
            for pa in parts[n - p]:
                parts[n].add(tuple(sorted(pa + (p,))))
    return sorted(parts[num])
