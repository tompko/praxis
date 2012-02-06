def make_key(rails, message_length):
    items = list(range(message_length))
    key = [[] for i in range(rails)]
    index, dirc = 0, 1

    for i in items:
        key[index].append(i)

        if index == 0:
            dirc = 1
        elif index == rails - 1:
            dirc = -1

        index += dirc

    return reduce(lambda x, y: x+ y, key)

def encrypt(message, rails):
    return "".join([message[k] for k in make_key(rails, len(message))])

def decrypt(cipher, rails):
    message = sorted(zip(make_key(rails, len(cipher)), cipher))
    return "".join([m[1] for m in message])

