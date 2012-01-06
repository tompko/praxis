import unittest

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

class TestMatrices(unittest.TestCase):
    def test_matrix(self):
        A = Matrix(3, 1, [1,2,3])
        B = Matrix(2, 3, [1,2,3,4,5,6])
        C = Matrix(2, 3, [2,3,4,3,4,5])
        D = Matrix(3, 4, [1,2,3,4,2,3,4,5,3,4,5,6])

        self.assertEqual(A.vals, [[1],[2],[3]])
        self.assertEqual(B.vals, [[1,2,3], [4,5,6]])
        self.assertEqual(C.vals, [[2,3,4], [3,4,5]])
        self.assertEqual(D.vals, [[1,2,3,4], [2,3,4,5], [3,4,5,6]])

        X = B + C
        self.assertEqual(X.vals, [[3,5,7], [7,9,11]])

        X = 2 * B
        self.assertEqual(X.vals, [[2,4,6], [8, 10, 12]])

        X = B * D
        self.assertEqual(X.vals, [[14,20,26,32], [32,47,62,77]])

        X = B.transpose()
        self.assertEqual(X.vals, [[1,4], [2,5], [3,6]])
if __name__ == "__main__":
    unittest.main()
