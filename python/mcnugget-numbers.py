def non_mcnugget():
    """return a list of all non-McNugget numbers"""
    nugget = [0, 6, 9, 20]
    mcnugget = set([6, 9, 20])

    while True:
        mcnugget = set([m+n for m in mcnugget for n in nugget])

        for m in mcnugget:
            found = all([m+j in mcnugget for j in range(6)])
            if found:
                return [k for k in range(1, m) if k not in mcnugget]

        
