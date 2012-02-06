def max_diff(xs):
    """Returns i and j that maximise x[j] - x[i] with i <= j"""
    min_x, min_i, i = xs[0], 0, 0
    max_diff, j = 0, 0

    for k, x in enumerate(xs):
        if x < min_x:
            min_x = x
            min_i = k
        if x - min_x > max_diff:
            max_diff = x - min_x
            i = min_i
            j = k

    return i, j
