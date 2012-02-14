def divisors_sieve(limit):
    divisors = [[1] for i in range(limit)]

    for i in range(2, limit):
        m = i
        while m < limit:
            divisors[m].append(i)
            m += i

    return divisors

def sum_of_divisors_sieve(limit):
    sums = [1 for i in range(limit)]

    for i in range(2, limit):
        m = i
        while m < limit:
            sums[m] += i
            m += i

    return sums

def num_divisors_sieve(limit):
    count = [1 for i in range(limit)]

    for i in range(2, limit):
        m = i
        while m < limit:
            count[m] += 1
            m += i

    return divisors

def perfect_sieve(limit):
    sums = sum_of_divisors_sieve(limit)

    return [i for i in range(limit) if sums[i] == i*2]

def amicable_sieve(limit):
    sums = sum_of_divisors_sieve(limit)

    pairs = []
    
    for a in range(1, limit):
        b = sums[a] - a
        if b > a and b < limit and sums[b] - b == a:
            pairs.append((a,b))

    return pairs
