import itertools

def green_eyes():
    group = ["blue"] * 11 + ["brown"] * 13 + ["green"] * 3

    win, total = 0, 0

    for sub_group in itertools.permutations(group, 3):
        if len([x for x in sub_group if x == "green"]) == 1:
            win += 1
        total += 1

    return float(win) / float(total)

if __name__ == "__main__":
    print green_eyes()

    
