import itertools
from praxis import transpose, untranspose

def encrypt(message, polybius, keyword):
    polybius = polybius.lower()

    trans = {}
    for (key, val) in zip(polybius, itertools.product("ADFGX", repeat=2)):
        val = val[0] + val[1]
        trans[key] = val
        if key == 'i':
            trans['j'] = val
        if key == 'j':
            trans['i'] = val

    ppoly = "".join([trans[m.lower()] for m in message])

    return transpose(ppoly, keyword)

def decrypt(cipher, polybius, keyword):
    untrans = untranspose(cipher, keyword)

    trans = {}
    for (val, key) in zip(polybius, itertools.product("ADFGX", repeat=2)):
        key = key[0] + key[1]
        trans[key] = val
    
    groups = [untrans[2*i:2*i+2] for i in range(len(untrans) / 2)]

    return "".join([trans[g] for g in groups])
