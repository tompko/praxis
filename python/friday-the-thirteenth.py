from praxis import jdn

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
