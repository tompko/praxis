import unittest

def foo(xs):
    return reduce(lambda x, y: x + y*y, sorted(xs)[1:], 0)

class TestSumOfSquares(unittest.TestCase):
    def test_foo(self):
          self.assertEqual(foo([3, 4, 5]), 41)
          self.assertEqual(foo([3, 5, 4]), 41)
          self.assertEqual(foo([4, 3, 5]), 41)
          self.assertEqual(foo([4, 5, 3]), 41)
          self.assertEqual(foo([5, 3, 4]), 41)
          self.assertEqual(foo([5, 4, 3]), 41)
          self.assertEqual(foo([3, 3, 4]), 25)
          self.assertEqual(foo([3, 4, 3]), 25)
          self.assertEqual(foo([4, 3, 3]), 25)
          self.assertEqual(foo([3, 4, 4]), 32)
          self.assertEqual(foo([4, 3, 4]), 32)
          self.assertEqual(foo([4, 4, 3]), 32)
          self.assertEqual(foo([3, 3, 3]), 18)

if __name__ == "__main__":
    unittest.main()
