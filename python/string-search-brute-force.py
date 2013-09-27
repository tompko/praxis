import unittest

def string_match(string, substring, start):
    length = len(substring)
    for i in range(length):
        if string[start+i] != substring[i]:
            return False
    return True

def string_search(string, substring, start=0):
    length = len(string) - len(substring) + 1

    for i in range(start, length):
        if string_match(string, substring, i):
            return i
    return -1

class TestStringSearch(unittest.TestCase):
    def test_match(self):
        self.assertEqual(string_match("abcd", "abcd", 0), True)
        self.assertEqual(string_match("abcd", "fghi", 0), False)

        self.assertEqual(string_match("abcdefghi", "fghi", 5), True)
        self.assertEqual(string_match("abcdefghi", "fghz", 5), False)

    def test_search(self):
        self.assertEqual(string_search("abcdefghi", "abcd"), 0)
        self.assertEqual(string_search("abcdefghi", "fghi"), 5)
        self.assertEqual(string_search("abcdefghi", "cdef"), 2)

        self.assertEqual(string_search("abcdefghi", "fghi", 5), 5)
        self.assertEqual(string_search("abcdefghi", "abcd", 5), -1)

        self.assertEqual(string_search("abcdefghi", "wxyz"), -1)

if __name__ == "__main__":
    unittest.main()
