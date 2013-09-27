from praxis import Matrix

def fib_recurse(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recurse(n - 1) + fib_recurse(n - 2)

def fib_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fib_matrix(n):
    if n == 0:
        return 0
    
    mat = Matrix(2, 2, [1, 1, 1, 0])
    ret = Matrix(2, 2, [1, 0, 1, 0])
    while n > 1:
        if n % 2 == 0:
            mat = mat * mat
            n /= 2
        else:
            ret = ret * mat
            n -= 1
    ret = ret * mat
    return ret.rows(1)[1]
