"""Baker, Cooper, Fletcher, Miller and Smith live on different floors of an
apartment house that contains only five floors. Baker does not live on the top
floor. Cooper does not live on the bottom floor. Fletcher does not live on
either the top or the bottom floor. Miller lives on a higher floor than does
Cooper. Smith does not live on a floor adjacent to Fletcher’s. Fletcher does
not live on a floor adjacent to Cooper’s. Where does everyone live?
"""

import itertools

def valid_dwell(floors):
    """Return whether a given ordering is valid according to the puzzle"""
    valid = True
    if floors[0] == "Baker":
        valid = False
    if floors[4] == "Cooper":
        valid = False
    if floors[0] == "Fletcher" or floors[4] == "Fletcher":
        valid = False
    if floors.index("Miller") > floors.index("Cooper"):
        valid = False
    if abs(floors.index("Smith") - floors.index("Fletcher")) == 1:
        valid = False
    if abs(floors.index("Fletcher") - floors.index("Cooper")) == 1:
        valid = False
    return valid

def multiple_dwellings():
    """Solve the mulitple dwellings puzzle

    Generate all permutations of people living in the apartment and
    filter out the invalid ones.
    """
    people = ["Baker", "Cooper", "Fletcher", "Miller", "Smith"]

    return [p for p in itertools.permutations(people) if valid_dwell(p)]

if __name__ == "__main__":
    print multiple_dwellings[0]
