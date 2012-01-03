kaprekar_chain_cache = {}

def next_in_chain(n):
    global kaprekar_chain_cache
    if n not in kaprekar_chain_cache:
        digits = list(str(n))
        while len(digits) < 4:
            digits.insert(0,"0")
        if len(set(digits)) == 1:
            kaprekar_chain_cache[n] = 6174
            return 6174
        digits.sort()
        ascend = int("".join(digits).lstrip("0"))
        digits.sort(reverse=True)
        descend = int("".join(digits))

        kaprekar_chain_cache[n] = abs(ascend - descend)
    return kaprekar_chain_cache[n]

def kaprekar_chain(n):
    chain = [n]
    while n != 6174:
        n = next_in_chain(n)
        chain.append(n)
    return chain

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
    longest = []
    length = -1

    for i in range(1001, 10000):
        chain = kaprekar_chain(i)
        if len(chain) > length:
            length = len(chain)
            longest = chain
    print "Longest Kaprekar Chain:"
    print longest
    print ""
    print "Kaprekar numbers less than 1000:"
    print [x for x in range(1000) if kaprekar(x)]
