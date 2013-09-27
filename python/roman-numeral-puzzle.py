def roman(n):
    vals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

    index = 0
    ret = ""
    while n:
        while n < vals[index][0]:
            index += 1
        ret += vals[index][1]
        n -= vals[index][0]

    return ret

def count(string):
    ret = {}

    for c in string:
        ret[c] = ret.get(c, 0) + 1

    return ret

def roman_puzzle():
    sols = []

    for i in range(1, 2001):
        rom = roman(i)
        if all([x == 1 for x in count(rom).itervalues()]):
            sols.append((i, rom))
    return sols
