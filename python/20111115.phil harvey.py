import itertools

def test(xs, ys):
    if sum(xs) != sum(ys):
        return False
    if sum([x*x for x in xs]) != sum([y*y for y in ys]):
        return False
    if sum([x**3 for x in xs]) != sum([y**3 for y in ys]):
        return False
    return True

def phil_harvey():
    for xs in itertools.combinations(range(1,17), 8):
        ys = [y for y in range(1, 17) if not y in xs]
        if test(xs, ys):
            print list(xs)
            print ys
            break
