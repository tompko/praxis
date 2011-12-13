import unittest

def search(xs, n):
    imin, imax = 0, len(xs) - 1

    while imin <= imax:
        half = (imin + imax) / 2
        
        if xs[half] == n:
            return half
        elif xs[half] < n:
            imin = half + 1
        elif xs[half] > n:
            imax = half - 1

    return -1

class BinaryTest(unittest.TestCase):
    def test_search(self):
        power2 = range(2**8)

        for i in range(2**8):
            self.assertEqual(search(power2, i), power2.index(i))

        self.assertEqual(search(power2, -6), -1)
        self.assertEqual(search(power2, 1025), -1)

        nonpow2 = range(300)

        for i in range(300):
            self.assertEqual(search(nonpow2, i), nonpow2.index(i))

        self.assertEqual(search(nonpow2, -42), -1)
        self.assertEqual(search(nonpow2, 9000), -1)

if __name__ == "__main__":
    unittest.main()
