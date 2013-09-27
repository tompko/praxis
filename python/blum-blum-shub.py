class BlumBlumShub:
    def __init__(self, p, q, seed):
        self.mod = p * q
        self.seed = seed
        self.reset()

    def stream(self, b):
        """Yields a stream of items, each item contains b bits"""
        mod = 1 << b
        while True:
            yield (self.x % mod)
            self.x = pow(self.x, 2, self.mod)

    def encrypt(self, string):
        return [ord(x[0]) ^ x[1] for x in zip(string, self.stream(8))]

    def decrypt(self, cipher):
        return "".join([chr(x[0]^x[1]) for x in zip(cipher, self.stream(8))])

    def reset(self):
        self.x = pow(self.seed, 2, self.mod)
