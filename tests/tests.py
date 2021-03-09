import unittest
from fibonacci_sum.fibonacci_sum import fibosum


class FibonacciSumTests(unittest.TestCase):
    def test_true1(self):
        self.assertEqual(fibosum(5), 13)

    def test_true2(self):
        self.assertEqual(fibosum(5.9), 13)

    def test_false1(self):
        self.assertFalse(fibosum('str'), False)


if __name__ == '__main__':
    unittest.main()
