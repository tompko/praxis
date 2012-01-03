def iterate(n):
    sumi = 0
    while n > 0:
        sumi += (n % 10) ** 2
        n = n // 10
    return sumi

def happy1(n):
    tortoise = n
    hare = n

    while True:
        tortoise = iterate(tortoise)
        hare = iterate(iterate(hare))

        if hare == 1:
            return True
        if hare == tortoise:
            return False

def happy2(n):
    seen = set([n])
    current = n
    while True:
        current = iterate(current)

        if current == 1:
            return True
        if current in seen:
            return False
        seen.add(current)
