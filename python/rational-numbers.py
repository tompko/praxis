from praxis import gcd, lcm

class Rational(object):
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        self.num = numerator if denominator >= 0 else -numerator
        self.den = abs(denominator)
        self.reduce_terms()

    def __add__(self, other):
        if isinstance(other, Rational):
            new_den = lcm(self.den, other.den)
            sfact, ofact = new_den / self.den, new_den / other.den
            new_num = (self.num * sfact) + (other.num * ofact)
            return Rational(new_num, new_den)
        raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Rational):
            new_den = lcm(self.den, other.den)
            sfact, ofact = new_den / self.den, new_den / other.den
            new_num = (self.num * sfact) - (other.num * ofact)
            return Rational(new_num, new_den)
        raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, Rational):
            new_num = self.num * other.num
            new_den = self.den * other.den
            return Rational(new_num, new_den)
        raise NotImplementedError

    def __div__(self, other):
        if isinstance(other, Rational):
            new_num = self.num * other.den
            new_den = self.den * other.num
            return Rational(new_num, new_den)
        raise NotImplementedError

    def __lt__(self, other):
        return (self.num * other.den) < (other.num * self.den)

    def reduce_terms(self):
        g = gcd(self.num, self.den)
        self.num /= g
        self.den /= g

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)
