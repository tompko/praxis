def from26_toint(number):
    ret = 0
    factor = 1

    while number:
        digit = ord(number[-1])
        number = number[: -1]
        ret += (digit - ord("A")) * factor
        factor *= 26

    return ret

def fromint_to26(number):
    ret = ""

    if number == 0:
        return "A"

    while number > 0:
        ret = chr(ord("A") + number % 26) + ret
        number /= 26

    return ret

def prashant_mul(a, b):
    return fromint_to26(from26_toint(a) * from26_toint(b))
