def first_character(string):
    counts = {}

    for s in string:
        if not s in counts:
            order += s
        counts[s] = counts.get(s, 0) + 1

    for s in string:
        if counts[o] == 1:
            return o

    return None
