"""Binary Search: A simple task, easy to get wrong"""
import unittest

def binary_search(n, ns):
    """Search a list of ns for an element n

    Returns the index of n when n is in the list, or -1 if n is not found.
    Assumes the list is sorted in ascending order.
    """
    lo, high = 0, len(ns) - 1

    while lo <= high:
        mid = (lo + high) / 2
        if ns[mid] == n:
            return mid
        elif ns[mid] < n:
            lo = mid + 1
        elif ns[mid] > n:
            high = mid - 1

    return -1

class TestBinarySearch(unittest.TestCase):
    """Test the implementation of binary search"""
    
    def test_power_2(self):
        """Test with a list of power of 2 length

        First check all items in the list can be found, then check
        we fail high and low properly
        """
        for i in range(256):
            self.assertEqual(binary_search(i, list(range(256))), i)

        self.assertEqual(binary_search(-1, list(range(256))), -1)
        self.assertEqual(binary_search(-411, list(range(256))), -1)
        self.assertEqual(binary_search(256, list(range(256))), -1)
        self.assertEqual(binary_search(411, list(range(256))), -1)

    def test_non_power_2(self):
        """Test a list of non power of 2 length

        First check all items in the list can be found, then check
        we fail high and low properly
        """
        for i in range(200):
            self.assertEqual(binary_search(i, list(range(200))), i)

        self.assertEqual(binary_search(-1, list(range(200))), -1)
        self.assertEqual(binary_search(-411, list(range(200))), -1)
        self.assertEqual(binary_search(200, list(range(200))), -1)
        self.assertEqual(binary_search(411, list(range(200))), -1)

    def test_equal_list(self):
        """Test a list containing all equal elements

        Check we find the element, and fail and low properly
        """
        self.assertNotEqual(binary_search(1, [1]*10), -1)
        self.assertEqual(binary_search(0, [1]*10), -1)
        self.assertEqual(binary_search(2, [1]*10), -1)

if __name__ == "__main__":
    unittest.main()
