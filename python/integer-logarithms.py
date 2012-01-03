def ilog(n, base=10):
    lo, blo = 0, 1
    hi, bhi = 1, base

    while bhi <= n:
        lo, blo = hi, bhi
        hi, bhi = hi * 2, bhi * bhi

    while hi - lo > 1:
        mid = (hi + lo) / 2
        bmid = blo * base ** (mid - lo)

        if bmid < n:
            lo, blo = mid, bmid
        elif bmid > n:
            hi, bhi = mid, bmid
        else:
            return mid

    return lo
