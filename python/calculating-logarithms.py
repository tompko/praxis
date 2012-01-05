epsilon = 0.00000001

def sqrt(n):
    x = 1.0
    while abs(n - x*x) > epsilon:
        x = x - ((x*x - n) / (2 * x))
    return x
    
def log(n, base):
    lo, hi = (0.0, 1.0), (1.0, float(base))

    while hi[1] <= n:
        lo, hi = hi, (hi[0] + 1, hi[1] * base)

    while abs(n - lo[1]) > epsilon:
        mid = ((lo[0] + hi[0]) / 2, sqrt(lo[1] * hi[1]))
        hi = mid if mid[1] > n else hi
        lo = mid if mid[1] <= n else lo
    return lo[0]
