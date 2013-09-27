def onefourfive(xs):
    if len(xs) == 1:
        return xs

    x = xs.pop(0)

    ret = []
    for z in onefourfive(xs[:]):
        for s in ["", "+", "*"]:
            ret.append(x + s + z)

    return ret

def exercise():
    xs = onefourfive(list("123456789"))

    xs = [(eval(x), x) for x in xs]
    ys = dict()

    for x in xs:
        l = ys.get(x[0], [])
        l.append(x[1])
        ys[x[0]] = l

    maxn = -1
    maxt = 0
    maxexp = None

    for y in ys:
        if len(ys[y]) > maxn:
            maxn = len(ys[y])
            maxt = y
            maxexp = ys[y]

    print "Most frequent result:", maxt
    print "Expressions with that result:"
    print "\n".join(maxexp)
