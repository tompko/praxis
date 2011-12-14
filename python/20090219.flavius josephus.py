def josephus(n, step):
    ret = []
    people = [True for i in range(n)]
    pos = step - 1

    while len(ret) < n - 1:
        ret.append(pos)
        people[pos] = False
        count = 0

        while count < step:
            pos += 1
            pos %= n
            if people[pos]:
                count += 1

    for i in range(n):
        if people[i]:
            ret.append(i)

    return ret
