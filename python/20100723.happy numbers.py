happy_numbers = {1: True}

def sum_of_squares(n):
    ret = 0
    while n:
        ret += (n % 10) ** 2
        n /= 10
    return ret

def happy(n):
    if n in happy_numbers:
        return happy_numbers[n]

    visited = set([n])

    while True:
        n = sum_of_squares(n)

        if n in happy_numbers:
            for v in visited:
                happy_numbers[v] = happy_numbers[n]
            return happy_numbers[n]
        if n in visited:
            for v in visited:
                happy_numbers[v] = False
            return False
        visited.add(n)

def happy_less_than(n):
    return [i for i in range(1, n) if happy(i)]
