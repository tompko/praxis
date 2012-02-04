upside = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

def is_upside(n):
    digits = []
    updigs = []

    while n:
        dig = n % 10
        if dig not in upside:
            return False
        digits.append(dig)
        updigs.append(upside[dig])
        n /= 10

    updigs.reverse()
    return digits == updigs

def upside_n(n):
    upnums = []

    for i in range(n):
        if is_upside(i):
            upnums.append(i)

    return upnums
