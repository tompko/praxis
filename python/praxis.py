#Columnar transposition
def make_key(text_len, keyword):
    key_len = len(keyword)
    columns = [range(text_len)[i::key_len] for i in range(key_len)]

    tkey = zip(keyword, range(key_len), columns)
    tkey.sort()

    return reduce(lambda x, y: x+y, [tk[2] for tk in tkey])

def transpose(message, keyword):
    key = make_key(len(message), keyword)

    return "".join([message[k] for k in key])

def untranspose(cipher, keyword):
    key = make_key(len(cipher), keyword)
    message = ["" for i in range(len(cipher))]

    for (i, k) in enumerate(key):
        message[k] = cipher[i]

    return "".join(message)

#Math utilities
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    q, r = a / b, a % b
    s, t = extended_gcd(b, r)
    return (t, s - q * t)

def lcm(a, b):
    g = gcd(a, b)
    return a * (b / g)

#Matrices
class Matrix():
    def __init__(self, row, col, val):
        self.vals = [[0 for c in range(col)] for r in range(row)]
        self.row = row
        self.col = col

        for i in range(row):
            for j in range(col):
                self.vals[i][j] = val[i*col + j]

        self.transposed = map(list, zip(*self.vals))

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise NotImplementedError
        if self.row != other.row or self.col != other.col:
            raise ValueError("Mismatched matrix dimensions")

        new_val = []
        for r in range(self.row):
            for c in range(self.col):
                new_val.append(self.vals[r][c] + other.vals[r][c])
        return Matrix(self.row, self.col, new_val)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise NotImplementedError
        if self.row != other.row or self.col != other.col:
            raise ValueError("Mismatched matrix dimensions")

        new_val = []
        for r in range(self.row):
            for c in range(self.col):
                new_val.append(self.vals[r][c] - other.vals[r][c])
        return Matrix(self.row, self.col, new_val)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            new_val = []
            for r in range(self.row):
                for c in range(self.col):
                    new_val.append(self.vals[r][c] * other)
            return Matrix(self.row, self.col, new_val)
        elif isinstance(other, Matrix):
            if self.col != other.row:
                raise ValueError("Mismatch in matrix sizes")
            new_val = []
            for r in range(self.row):
                for c in range(other.col):
                    val = sum([x[0]*x[1] for x in zip(self.rows(r), other.cols(c))])
                    new_val.append(val)
            return Matrix(self.row, other.col, new_val)
        else:
            raise NotImplementedError

    def __rmul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            new_val = []
            for r in range(self.row):
                for c in range(self.col):
                    new_val.append(self.vals[r][c] * other)
            return Matrix(self.row, self.col, new_val)
        else:
            raise NotImplementedError

    def __repr__(self):
        return "\n".join([" ".join([str(x) for x in self.vals[row]]) for row in range(self.row)])

    def transpose(self):
        vals = reduce(lambda x,y: x+y, self.transposed, [])
        return Matrix(self.col, self.row, vals)

    def rows(self, index):
        return self.vals[index]

    def cols(self, index):
        return self.transposed[index]

    def set_cell(self, row, col, val):
        self.vals[row][col] = val
        self.transposed[col][row] = val

#Primes
def seive(n):
    erato = [False,False,True] + [True, False] * ((n // 2) + 1)
    d = 3

    while d*d <= n:
        if erato[d]:
            f = d*d
            while f <= n:
                erato[f] = False
                f += d
        d += 2

    primes = [i for i in range(n) if erato[i]]

    return primes

def compute_wheel(limit):
    primes = seive(limit)
    circum = reduce(lambda x,y: x*y, primes, 1)
    spokes = [i for i in range(1, circum) if gcd(i, circum) == 1]
    diffs = [spokes[i+1] - s for i,s in enumerate(spokes[:-1])]
    diffs.insert(0, circum - spokes[-1] + 1)

    return primes, diffs

def wheel_factorise(n):
    factors = set([])
    d = 11
    primes, diffs = compute_wheel(d)

    for p in primes:
        while n % p == 0:
            factors.add(p)
            n /= p

    while d*d <= n:
        while n % d == 0:
            factors.add(d)
            n /= d
        d += diffs[0]
        diffs = diffs[1:] + diffs[:1]

    if n > 1:
        factors.add(n)
    ret = list(factors)
    ret.sort()
    return ret

def pollard_rho(n):
    c = 1
    while True:
        f = lambda x: x**2 + c

        x, y, d = 2, 2, 1

        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
        if d != n:
            return d

        c += 1

#Date functions
def jdn(year, month, day):
    """Calculate the Julian Day Number for the given date"""
    a = (14 - month) / 12
    y = year + 4800 - a
    m = month + 12 * a - 3

    ret = day + ((153*m + 2) / 5) + (365*y)
    ret = ret + (y / 4) - (y / 100) + (y / 400) - 32045

    return ret
