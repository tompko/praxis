import unittest

def write(n):
    """Writes a number n (< 1000000) in words"""
    assert(n < 1000000)

    ret = ""
    if n > 1000:
        ret = write(n / 1000)
        ret += " thousand "
        n = n % 1000
        if n > 0 and n < 100:
            ret += "and "
    if n >= 100:
        ret += write(n / 100)
        ret += " hundred "
        n = n % 100
        if n > 0:
            ret += "and "
    if n >= 20:
        tens = {9: "ninety", 8: "eighty", 7: "seventy",
                6: "sixty", 5: "fifty", 4: "forty",
                3: "thirty", 2: "twenty"}
        ret += tens[n / 10]
        n = n % 10
        if n > 0:
            ret += "-"
    if n > 0:
        units = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                 15: "fifteen", 16: "sixteen", 17: "seventeen",
                 18: "eighteen", 19: "nineteen"}
        ret += units[n]
        n = 0

    return ret

def oban_numbers():
    ret = []
    for i in range(1, 1000):
        if write(i).find("o") == -1:
            ret.append(i)
    return ret

class TestWrittenNumbers(unittest.TestCase):
    def test_write(self):
        self.assertEquals(write(5), "five")
        self.assertEquals(write(10), "ten")
        self.assertEquals(write(25), "twenty-five")
        self.assertEquals(write(65), "sixty-five")
        self.assertEquals(write(145), "one hundred and forty-five")
        self.assertEquals(write(267), "two hundred and sixty-seven")
        self.assertEquals(write(783), "seven hundred and eighty-three")
        self.assertEquals(write(1934), "one thousand nine hundred and thirty-four")

if __name__ == "__main__":
    unittest.main()
