def selectk(xs, k):
    """Select the smallest item for which k items of the set xs are smaller"""
    elem = xs[len(xs) / 2]

    smaller = [x for x in xs if x < elem]
    bigger = [x for x in xs if x > elem]

    if len(smaller) == k:
        return elem
    elif len(smaller) > k:
        return selectk(smaller, k)
    else:
        return selectk(bigger, k - len(smaller) - 1)
