def next_permutation(xs):
    if len(xs) < 1:
        return xs

    i = len(xs) - 1

    while True:
        ii = i
        i -= 1

        if xs[i] < xs[ii]:
            j = len(xs) - 1
            while xs[i] >= xs[j]:
                j -= 1
            xs[i],xs[j] = xs[j],xs[i]
            xs = xs[:ii] + xs[-1:ii-1:-1]
            return xs
        if i == 0:
            return xs[::-1]

def digits(x):
    ret = []
    while x > 0:
        ret.insert(0, x % 10)
        x /= 10
    return ret

def next_greater(a):
    ans = next_permutation(digits(a))
    return reduce(lambda x, y: x*10 + y, ans, 0)
