def kaprekar(k):
    n = 1
    power = 10
    while power <= k:
        power *= 10
        n += 1

    x = k ** 2
    x, y = x % power, x // power

    if x + y == k:
        return True
    return False

if __name__ == "__main__":
    print [x for x in range(1, 1000) if kaprekar(x)]
