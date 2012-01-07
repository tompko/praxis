def make_polybius(keyword):
    keyword = [x.upper() for x in keyword if x.isalpha() and x.upper() != "I"]
    keyword += list("ABCDEFGHJKLMNOPQRSTUVWXYZ")

    square = [[] for i in range(5)]
    coord_map = {}

    col, row = 0,0
    for k in keyword:
        if k in coord_map:
            continue
        coord_map[k] = (row, col)
        square[row].append(k)
        col += 1
        if col == 5:
            col = 0
            row += 1

    coord_map["I"] = coord_map["J"]

    return square, coord_map

def encrypt(message, keyword=""):
    poly, co = make_polybius(keyword)

    coords = [co[m.upper()] for m in message if m.isalpha()]
    trans = reduce(lambda x, y: x + y, map(list, zip(*coords)), [])
    split = [trans[i*2:i*2+2] for i in range(len(trans) / 2)]
    cipher = [poly[s[0]][s[1]] for s in split]
    
    return "".join(cipher)

def decrypt(cipher, keyword=""):
    poly,co = make_polybius(keyword)

    coords = [list(co[c.upper()]) for c in cipher if c.isalpha()]
    coords = reduce(lambda x, y: x + y, coords, [] )
    split = [coords[:len(coords) / 2], coords[len(coords) / 2:]]
    trans = map(list, zip(*split))
    message = [poly[t[0]][t[1]] for t in trans]
    
    return "".join(message)
