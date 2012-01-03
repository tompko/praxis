def knight_neighbours(cell, m, n, visited):
    offsets = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

    ns = []

    for o in offsets:
        newpos = (cell[0] + o[0], cell[1] + o[1])
        if newpos[0] < 0 or newpos[0] >= m:
            continue
        if newpos[1] < 0 or newpos[1] >= n:
            continue
        if newpos in visited:
            continue
        ns.append(newpos)

    return ns

def knights_tour(m, n, path=None):
    """recursively find a knights tour on an m by n board"""
    if not path:
        for x in range(m):
            for y in range(n):
                ret = knights_tour(m, n, [(x,y)])
                if ret:
                    return ret
        return None
    else:
        if len(path) == m*n:
            return path
        curr = path[-1]
        neighbours = knight_neighbours(curr, m, n, path)

        choice = [(ne, knight_neighbours(ne, m, n, path)) for ne in neighbours]
        choice.sort(key=lambda x: len(x[1]))

        for c in choice:
            ret = knights_tour(m, n, path + [c[0]])
            if ret:
                return ret
        return None
