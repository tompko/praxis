def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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
