from praxis import transpose, untranspose

def encrypt(message, key1, key2):
    return transpose(transpose(message, key1), key2)

def decrypt(cipher, key1, key2):
    return untranspose(untranspose(cipher, key2), key1)
