import datetime

def computus(year):
    
    a = year % 19
    b = year / 100
    c = year % 100
    d = b / 4
    e = b % 4
    f = (b + 8) / 25
    g = (b - f + 1) / 3
    h = (19*a + b - d - g + 15) % 30
    i = c / 4
    k = c % 4
    L = (32 + 2*e + 2*i - h - k) % 7
    m = (a + 11*h + 22*L) / 451
    month = (h + L - 7*m + 114) / 31
    day = (h + L - 7*m + 114) % 31
    day += 1

    return (year, month, day)

def easter(year):
    return datetime.date(*computus(year))

def mardi_gras(year):
    return datetime.date(*computus(year)) - datetime.timedelta(days=47)
