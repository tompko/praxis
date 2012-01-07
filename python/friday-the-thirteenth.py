def jdn(year, month, day):
    a = (14 - month) / 12
    y = year + 4800 - a
    m = month + 12 * a - 3

    ret = day + ((153*m + 2) / 5) + (365*y)
    ret = ret + (y / 4) - (y / 100) + (y / 400) - 32045

    return ret

def fridays():
    month = 3
    year = 2009

    thirteenths = []
    for i in range(120):
        month += 1
        if month > 12:
            month -= 12
            year += 1
        if jdn(year, month, 13) % 7 == 4:
            thirteenths.append((year, month))
    return len(thirteenths)
