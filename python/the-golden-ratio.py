def golden(m):
    """Returns the nth continued fraction approximation to the golden ratio."""
    n, d = 1, 1
    for i in range(m):
        n, d = n + d, n
    return (n, d)
