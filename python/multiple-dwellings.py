import itertools

people = ["Baker", "Cooper", "Fletcher", "Miller", "Smith"]

def multiple_dwellings():
    for perm in itertools.permutations(people):
        #Baker does not live on the top floor.
        if perm.index("Baker") == 4:
            continue
        #Cooper does not live on the bottom floor.
        if perm.index("Cooper") == 0:
            continue
        #Fletcher does not live on either the top or the bottom floor.
        if perm.index("Fletcher") == 0 or perm.index("Fletcher") == 4:
            continue
        #Miller lives on a higher floor than does Cooper.
        if perm.index("Miller") < perm.index("Cooper"):
            continue
        #Smith does not live on a floor adjacent to Fletcher's.
        if abs(perm.index("Smith") - perm.index("Fletcher")) == 1:
            continue
        #Fletcher does not live on a floor adjacent to Cooper's.
        if abs(perm.index("Fletcher") - perm.index("Cooper")) == 1:
               continue
        return perm
