"""Compute the count of pythagorean triples with perimeter not exceeding
one million"""

def primitive_triples(limit):
    """Returns a list of primitive triples with sum less than limit"""
    def loop(a, b, c):
        """Recursively generate primitive triples"""
        res = []
        if sum([a, b, c]) < limit:
            if a < b:
                res.append((a, b, c))
            else:
                res.append((b, a, c))
            res.extend(loop(a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c))
            res.extend(loop(a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c))
            res.extend(loop(-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c))
        return res

    return loop(3, 4, 5)

def bounded_triples(limit):
    """Returns the number of triples with perimeter less than limit"""
    return sum([limit // sum(t) for t in primitive_triples(limit)])
