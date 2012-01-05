import itertools

def digits(n):
    ret = []
    while n > 0:
        ret.append(n % 10)
        n /= 10
    return ret

def same_five_digits():
    squares = []

    for i in range(100, 350):
        dig = digits(i*i)
        if not any([d > 5 or d == 0 for d in dig]) and len(dig) == 5:
            squares.append(i*i)

    poss = []
    for nums in itertools.combinations(squares, 3):
        dig_count = {}
        for n in nums:
            for d in digits(n):
                dig_count[d] = dig_count.get(d, 0) + 1

        if len(set(dig_count.iterkeys())) == 5 and\
        len(set(dig_count.itervalues())) == 5 and\
        not any([dig_count[i] == i for i in range(1, 6)]):
            single = [k for (k, v) in dig_count.iteritems() if v == 1][0]                
            poss.append((single, nums))

    sol_count = {}
    for p in poss:
        sol_count[p[0]] = sol_count.get(p[0], []) + [p[1]]

    return [s[0] for s in sol_count.itervalues() if len(s) == 1][0]
