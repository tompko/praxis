class BlumBlumShub:
    def __init__(self, p, q, seed):
        self.mod = p * q
        self.seed = seed
        self.reset()

    def get_n_bits(self, n, b):
        """Returns a list of n items, each item contains b bits"""
        ret = []

        mod = 1 << b
        for i in range(n):
            ret.append(self.x % mod)
            self.x = pow(self.x, 2, self.mod)

        return ret

    def encrypt(self, string):
        chars = [ord(s) for s in string]
        bits = self.get_n_bits(len(chars), 8)

        return map(lambda x: x[0] ^ x[1], zip(chars, bits))

    def decrypt(self, cipher):
        bits = self.get_n_bits(len(cipher), 8)

        return "".join(map(lambda x: chr(x[0]^x[1]), zip(cipher, bits)))

    def reset(self):
        self.x = pow(self.seed, 2, self.mod)
