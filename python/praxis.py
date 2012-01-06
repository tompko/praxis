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
