def mod_out(ranges):
    ranges = ranges.split(",")
    ret = []

    for r in ranges:
        if "-" in r:
            a,b = r.split("-")
            for i in range(int(a), int(b) + 1):
                ret.append(i)
        else:
            ret.append(int(r))

    return ",".join([str(r) for r in ret])
