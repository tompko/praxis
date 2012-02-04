partitions = {}

def partition(n):
    if n in partitions:
        return partitions[n]
    if n == 0:
        return 1
    if n < 0:
        return 0

    ret = 0
    for k in range(1, n+1):
        a = partition(n - (k*(3*k-1))/2)
        b = partition(n - (k*(3*k+1))/2)
        ret += (-1)**(k+1) * (a + b)
    partitions[n] = ret
    return ret
