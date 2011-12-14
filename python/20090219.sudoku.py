def cross(xs, zs):
    return [x + z for x in xs for z in zs]

rows = "123456789"
cols = "ABCDEFGHI"
squares = cross(cols, rows)
vals = "123456789"

unitlist = ([cross(c, rows) for c in cols] +
            [cross(cols, r) for r in rows] +
            [cross(a, b) for a in ["ABC", "DEF", "GHI"] for b in ["123", "456", "789"]])
units = dict([(s, [u for u in unitlist if s in u]) for s in squares])
peers = dict([(s, set(sum(units[s], [])) - set([s])) for s in squares])

def parse_grid(grid):
    values = dict([(s, vals) for s in squares])

    for s, d in grid_values(grid).items():
        if d in vals and not assign(values, s, d):
            return False
    return values

def grid_values(grid):
    chars = [c for c in grid if c in vals or c in "0."]
    assert len(chars) == 81
    return dict(zip(squares, chars))

def assign(values, s, d):
    other_values = values[s].replace(d, "")

    for v in other_values:
        if not eliminate(values, s, v):
            return False
    return values

def eliminate(values, s, d):
    if not d in values[s]:
        return values

    values[s] = values[s].replace(d, "")

    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        for s2 in peers[s]:
            if not eliminate(values, s2, d2):
                return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values

def solve(grid):
    return search(parse_grid(grid))

def search(values):
    if not values:
        return False
    if all(len(values[s]) == 1 for s in squares):
        return values

    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    for d in values[s]:
        ret = search(assign(values.copy(), s, d))
        if ret:
            return ret
    return False

def display(values):
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for c in cols:
        print ''.join(values[c+r].center(width)+('|' if r in '36' else '')
                      for r in rows)
        if c in 'CF': print line
    print
