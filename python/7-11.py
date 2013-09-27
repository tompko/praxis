import itertools

def divisors_711():
    divs = []
    for d in range(1, 711):
        if 711000000 % d == 0:
            divs.append(d)
    return divs

def second_eleven():
    for (a,b,c,d) in itertools.product(divisors_711(), repeat=4):
        if b < a or c < b or d < c:
            continue
        if a + b + c + d != 711:
            continue
        if a * b * c * d != 711000000:
            continue
        return (a,b,c,d)
