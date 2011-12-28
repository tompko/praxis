def make_key(text_len, keyword):
    key_len = len(keyword)
    columns = [range(text_len)[i::key_len] for i in range(key_len)]

    tkey = zip(keyword, range(key_len), columns)
    tkey.sort()

    return reduce(lambda x, y: x+y, [tk[2] for tk in tkey])

def transpose(message, keyword):
    key = make_key(len(message), keyword)

    return "".join([message[k] for k in key])

def untrans(cipher, keyword):
    key = make_key(len(cipher), keyword)
    message = ["" for i in range(len(cipher))]

    for (i, k) in enumerate(key):
        message[k] = cipher[i]

    return "".join(message)

def encrypt(message, key1, key2):
    return transpose(transpose(message, key1), key2)

def decrypt(cipher, key1, key2):
    return untranspose(untranspose(cipher, key2), key1)
