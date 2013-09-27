import sys

epsilon = sys.float_info.epsilon

def horner(x, coeffs):
    """Use the Horner algorithm to calculate the value of a
    polynomial at a point"""
    b = 0
    for c in coeffs[::-1]:
        b = c + (x * b)

    return b

def sign(x):
    """Return the sign of x"""
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0

def conways_constant():
    """Find conways constant

    Conways constant is given by the unique positive real root
    of the polynomial with the following coefficients. Find the root
    by bisection
    """
    coeffs = [-6, 3, -6, 12, -4, 7, -7, 1, 0, 5, -2, -4, -12, 2,
              7, 12, -7, -10, -4, 3, 9, -7, 0, -8, 14, -3, 9, 2, -3,
              -10, -2, -6, 1, 10, -3, 1, 7, -7, 7, -12,-5, 8, 6, 10,
              -8, -8, -7, -3, 9, 1, 6, 6, -2, -3, -10, -2, 3, 5, 2,
               -1, -1, -1, 0 -1, -1, 1, 2, 2, -1, -2, -1, 0, 1]

    #Establish bounds on the root so we have an interval to bisect over
    lo, hi = 0.0, 1.0
    horner_lo, horner_hi = horner(lo, coeffs), horner(hi, coeffs)

    while sign(horner_lo) == sign(horner_hi):
        lo, hi = hi, hi*2
        horner_lo, horner_hi = horner(lo, coeffs), horner(hi, coeffs)

    #Perform the bisection to sufficient accuracy
    while hi - lo > epsilon:
        mid = (lo + hi) / 2
        horner_mid = horner(mid, coeffs)

        if sign(horner_lo) == sign(horner_mid):
            lo = mid
            horner_lo = horner_mid
        else:
            hi = mid
            horner_hi = horner_mid

    return lo
