import itertools

def problem_1960_01():
    ret = []
    for i in range(100, 1000):
        if i % 11 == 0:
            n = i
            m = n / 11
            ss = 0
            while n > 0:
                ss += (n % 10) ** 2
                n /= 10
            if m == ss:
                ret.append(i)
    return ret
                
def problem_1962_01():
    i = 1
    mul = 10
    
    while i < 10000000:
        while mul < i:
            mul *= 10
        if (i*10 + 6) * 4 == 6*mul + i:
            return i*10 + 6
        i += 1

    return "Fail"

def problem_1963_06():
    for co in itertools.permutations("ABCDE"):
        desc = "".join(co)
        if sum([x[0] == x[1] for x in zip(desc, "ABCDE")]) != 0:
            continue
        if sum([x[0] == x[1] for x in zip(desc, "DAECB")]) != 2:
            continue
        valid = True
        pairs = ["AB", "BC", "CD", "DE"]
        for p in pairs:
            if desc.find(p) >= 0:
                valid = False
                break
        if not valid:
            continue
        pairs = ["DA", "AE", "EC", "CB"]
        numPairs = 0
        for p in pairs:
            if desc.find(p) >= 0:
                numPairs += 1
        if numPairs != 2:
            continue

        return desc
