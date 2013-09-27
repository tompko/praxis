import unittest

def add_letters(a, b):
    a = ord(a) - ord("A")
    b = ord(b) - ord("A")
    c = (a + b) % 26
    return chr(c + ord("A"))

def sub_letters(a, b):
    a = ord(a) - ord("A")
    b = ord(b) - ord("A")
    c = (a - b) % 26
    return chr(c + ord("A"))

def encrypt(message, keyword):
    keyword += message

    return "".join([add_letters(*z) for z in zip(message, keyword)])

def decrypt(cipher, keyword):
    message = ""

    for c in cipher:
        k = keyword[0]
        keyword = keyword[1:]
        m = sub_letters(c, k)
        keyword += m
        message += m

    return message

class TestAutoKey(unittest.TestCase):
    def test_arithmetic(self):
        self.assertEqual(add_letters("A", "P"), "P")
        self.assertEqual(add_letters("C", "R"), "T")

        self.assertEqual(sub_letters("W", "S"), "E")
        self.assertEqual(sub_letters("Z", "L"), "O")

    def test_cipher(self):
        self.assertEqual(encrypt("ACOLLECTIONOFETUDES", "PRAXIS"),
                         "PTOITWCVWZYSHXBIQSX")
        self.assertEqual(decrypt("PTOITWCVWZYSHXBIQSX", "PRAXIS"),
                         "ACOLLECTIONOFETUDES")
        
if __name__ == "__main__":
    unittest.main()
