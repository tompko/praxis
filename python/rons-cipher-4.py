class RC4:
    def __init__(self, key):
        self.set_key(key)
        
    def set_key(self, key):
        self.K = list(range(256))
        if type(key) == str:
            key = [ord(k) for k in key]

        j = 0
        klen = len(key)
        for i in range(256):
            j = (j + self.K[i] + key[i % klen]) % 256
            self.K[i], self.K[j] = self.K[j], self.K[i]

    def stream(self):
        i, j = 0, 0

        while True:
            i = (i + 1) % 256
            j = (j + self.K[i]) % 256
            self.K[i], self.K[j] = self.K[j], self.K[i]
            yield self.K[(self.K[i] + self.K[j]) % 256]

    def encrypt(self, string):
        return [ord(x[0]) ^ x[1] for x in zip(string, self.stream())]

    def decrypt(self, cipher):
        return "".join([chr(x[0] ^ x[1]) for x in zip(cipher, self.stream())])
