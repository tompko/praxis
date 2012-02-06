radix = 1000

class BigNumber(object):
    def __init__(self, number):
        self.rep = []

        if number < 0:
            self.rep.append(-1)
            number = -number
        else:
            self.rep.append(1)

        count = 0
        while number:
            count += 1
            self.rep.append(number % radix)
            number /= radix
        self.rep[0] *= count

    def __abs__(self):
        x = BigNumber(0)
        x.rep = [abs(self.rep[0])] + self.rep[1:]
        return x

    def __neg__(self):
        x = BigNumber(0)
        x.rep =[-self.rep[0]] + self.rep[1:]
        return x

    def compare(self, other):
        if self.rep[0] < other.rep[0]:
            return -1
        if self.rep[0] > other.rep[0]:
            return 1

        for i in range(-1, -len(self.rep) - 1, -1):
            if self.rep[i] < other.rep[i]:
                return -1
            if self.rep[i] > other.rep[i]:
                return 1
        return 0
    
    def __lt__(self, other):
        return self.compare(other) == -1
    
    def __le__(self, other):
        comp = self.compare(other)
        return comp == -1 or comp == 0
    
    def __eq__(self, other):
        return self.compare(other) == 0
    
    def __ne__(self, other):
        return self.compare(other) != 0
    
    def __ge__(self, other):
        comp = self.compare(other)
        return comp == 0 or comp == 1
    
    def __gt__(self, other):
        return self.compare(other) == 1
    
    def is_positive(self):
        return self.rep[0] > 0

    def is_negative(self):
        return self.rep[0] < 0

    def is_zero(self):
        return self.rep[0] == 0

    def is_even(self):
        if self.rep[0] == 0:
            return True
        return self.rep[1] % 2 == 0

    def is_odd(self):
        if self.rep[0] == 0:
            return False
        return self.rep[1] % 2 != 0

    def __repr__(self):
        return repr(self.rep)
        
