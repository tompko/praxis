def make_square(keyword):
    square = [[] for i in range(5)]
    coord_map = {}

    curr = (0,0)

    keyword = keyword.upper() + "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for k in keyword:
        if k.isalpha() and k not in coord_map:
            coord_map[k] = curr
            square[curr[1]].append(k)
            curr = (curr[0]+1, curr[1])
            if curr[0] == 5:
                curr = (0, curr[1] + 1)

    return square, coord_map
    
def encrypt(message, keyword):
    square, coord_map = make_square(keyword)

    encr = ""
    last = None
    for m in message.upper():
        if not m.isalpha():
            continue
        if m == "J":
            m = "I"
        if m == last:
            encr += "X"
        encr += m
        last = m
    if len(encr) % 2 == 1:
        encr += "X"
    encr

    pairs = [z for z in zip(encr[::2], encr[1::2])]
    cipher = ""
    
    for p in pairs:
        co1 = coord_map[p[0]]
        co2 = coord_map[p[1]]

        if co1[0] == co2[0]:
            co1 = (co1[0], (co1[1] + 1) % 5)
            co2 = (co2[0], (co2[1] + 1) % 5)
            cipher += square[co1[1]][co1[0]]
            cipher += square[co2[1]][co2[0]]
        elif co1[1] == co2[1]:
            co1 = ((co1[0] + 1) % 5, co1[1])
            co2 = ((co2[0] + 1) % 5, co2[1])
            cipher += square[co1[1]][co1[0]]
            cipher += square[co2[1]][co2[0]]
        else:
            cipher += square[co1[1]][co2[0]]
            cipher += square[co2[1]][co1[0]]

    return cipher

def decrypt(cipher, keyword):
    square, coord_map = make_square(keyword)

    pairs = [z for z in zip(cipher[::2], cipher[1::2])]
    message = ""
    
    for p in pairs:
        co1 = coord_map[p[0]]
        co2 = coord_map[p[1]]

        if co1[0] == co2[0]:
            co1 = (co1[0], (co1[1] - 1) % 5)
            co2 = (co2[0], (co2[1] - 1) % 5)
            message += square[co1[1]][co1[0]]
            message += square[co2[1]][co2[0]]
        elif co1[1] == co2[1]:
            co1 = ((co1[0] - 1) % 5, co1[1])
            co2 = ((co2[0] - 1) % 5, co2[1])
            message += square[co1[1]][co1[0]]
            message += square[co2[1]][co2[0]]
        else:
            message += square[co1[1]][co2[0]]
            message += square[co2[1]][co1[0]]

    return message
