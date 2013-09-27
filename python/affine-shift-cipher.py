from praxis import gcd, extended_gcd

def encrypt(message, key_a, key_b):
    assert(gcd(key_a, 26) == 1)

    cipher = ""

    for m in message:
        if m.isalpha():
            x = ord(m.upper()) - ord("A")
            y = (key_a * x + key_b) % 26
            cipher += chr(y + ord("A"))
        else:
            cipher += m

    return cipher

def decrypt(cipher, key_a, key_b):
    inverse, am_gcd = extended_gcd(key_a, 26)
    assert(am_gcd == 1)

    message = ""

    for c in cipher:
        if c.isalpha():
            x = ord(c.upper()) - ord("A")
            y = ((x - key_b) * inverse) % 26
            message += chr(y + ord("A"))
        else:
            message += c
    return message
