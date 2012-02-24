def hailstone(n):
    ret = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        ret.append(n)
    return ret
