def solve_search(xs):
    seen = set()

    for x in xs:
        if x in seen:
            return x
        seen.add(x)

def solve_sort(xs):
    xs.sort()

    for i in range(len(xs)):
        if xs[i] == xs[i+1]:
            return xs[i]
