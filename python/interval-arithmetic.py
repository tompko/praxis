class Interval():
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        assert(lower < upper)

    def __add__(self, other):
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def __sub__(self, other):
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def __mul__(self, other):
        vals = [self.lower * other.lower,
                self.lower * other.upper,
                self.upper * other.lower,
                self.upper * other.upper]
        return Interval(min(vals), max(vals))

    def __div__(self, other):
        if other.lower <= 0 <= other.upper:
            raise ZeroDivisionError

        vals = [self.lower / other.lower,
                self.lower / other.upper,
                self.upper / other.lower,
                self.upper / other.upper]
        return Interval(min(vals), max(vals))

    def __repr__(self):
        return "[" + str(self.lower) + ", " + str(self.upper) + "]"
