from praxis import extended_gcd

def add(a, b, mod):
    return (a + b) % mod

def sub(a, b, mod):
    return (a - b) % mod

def mul(a, b, mod):
    return (a * b) % mod

def div(a, b, mod):
    inv_b, gcd = extended_gcd(b, mod)

    if gcd == 1:
        raise ValueError()

    return mul(a, inv_b, mod)

def exp(a, b, mod):
    if b == 0:
        return 1
    if b % 2 == 0:
        return exp(a**2 % mod, b / 2, mod)
    else:
        return (a * exp(a, b - 1, mod)) % mod

def legendre_symbol(a, p):
    ret = exp(a, (p - 1) / 2, p)
    return -1 if ret == (p - 1) else ret

def sqrt(n, p):
    if legendre_symbol(n, p) != 1:
        return 0
    if n == 0:
        return 0
    if p == 2:
        return 2
    if p % 4 == 3:
        return exp(n, (p + 1) / 4, p)

    s = 0
    q = p - 1
    while q % 2 == 0:
        s += 1
        q /= 2

    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1

    c = exp(z, q, p)
    r = exp(n, (q + 1) / 2, p)
    t = exp(n, q, p)
    m = s

    while t % p != 1:
        i = 0
        d = t
        while d % p != 1:
            d = exp(d, 2, p)
            i += 1
        b = exp(c, exp(2, m - i - 1, p), p)
        r = mul(r, b, p)
        t = mul(t, exp(b, 2, p), p)
        c = exp(b, 2, p)
        m = i
    return r
