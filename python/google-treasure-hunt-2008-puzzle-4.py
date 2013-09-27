import praxis

def sums(xs, n, limit):
    start, finish = 0, n
    sumi = 0
    for i in range(n):
        sumi += xs[i]
    ret = []

    while finish < len(xs) and sumi <= limit:
        ret.append(sumi)
        sumi -= xs[start]
        sumi += xs[finish]
        start += 1
        finish += 1
    
    return ret

def intersect(xs, ys):
    ret = []

    xs.sort()
    ys.sort()
    xind, yind = 0,0    
    while xind < len(xs) and yind < len(ys):
        if xs[xind] == ys[yind]:
            ret.append(xs[xind])
            xind += 1
            yind += 1
        elif xs[xind] < ys[yind]:
            xind += 1
        else:
            yind += 1

    return ret

def treasure():
    primes = praxis.seive(10**7)
    sums541 = sums(primes, 541, primes[-1])
    sums41 = sums(primes, 41, primes[-1])
    sums17 = sums(primes, 17, primes[-1])
    sums7 = sums(primes, 7, primes[-1])
    
    psums541 = intersect(primes, sums541)
    psums41 = intersect(psums541, sums41)
    psums17 = intersect(psums41, sums17)
    psums7 = intersect(psums17, sums7)
    
    return psums7[0]

if __name__ == "__main__":
    print treasure()
