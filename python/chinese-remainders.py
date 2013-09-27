from praxis import extended_gcd

def chinese_remainder_theorem(ais, nis):
    """Construct a solution to the chinese remainder theorem

    Given a list of a[i]'s and n[i]'s constructs an x such that
    x = a[i] (mod n[i]) for all i
    """
    N = reduce(lambda x, y: x*y, nis, 1)
    ei = [extended_gcd(ni, N/ni)[1] * (N/ni)  for ni in nis]

    return sum([x[0]*x[1] for x in zip(ais, ei)]) % N
