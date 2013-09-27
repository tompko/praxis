def hamming_weight(n):
    count = 0
    while n:
        count += 1
        n &= n - 1
    return count

lookup = [hamming_weight(n) for n in range(256)]

def hamming_lookup(n):
    count = 0

    while n:
        count += lookup[n % 256]
        n /= 256

    return count
