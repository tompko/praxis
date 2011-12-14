import random

def card():
    cols = [random.sample(range(a,b), 5) for (a,b) in
               zip([1, 16, 31, 46, 61], [16, 31, 46, 61, 76])]
    ret = [num for col in cols for num in col]
    ret.sort()
    return ret

def bingo(card):
    _test = lambda xs: sum(card[x] for x in xs) == 0
    if any(map(_test, [
        xrange(5),              # B
        xrange(5, 10),          # I
        [10, 11, 12, 13],       # N
        xrange(14, 19),         # G
        xrange(19, 24),         # O
        [0, 5, 10, 14, 19],     # 1st row
        [1, 6, 11, 15, 20],     # 2nd row
        [2, 7, 16, 21],         # 3rd row
        [3, 8, 12, 17, 22],     # 4th row
        [4, 9, 13, 18, 23],     # 5th row
        [0, 6, 17, 23],         # nw to se diag
        [4, 8, 15, 19]])):      # ne to sw diag
        return True
    else:
        return False

def play(n):
    cards = [card() for _ in range(n)]

    numbers = range(1, 76)
    random.shuffle(numbers)

    for i, num in enumerate(numbers):
        for c in cards:
            if num in c:
                c[c.index(num)] = 0
        if any(map(bingo, cards)):
            return i + 1

trials = 10000

print sum([play(1) for x in range(trials)]) / float(trails)
print sum([play(500) for x in range(trials)]) / float(trails)
