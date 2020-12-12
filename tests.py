import unittest

from calc import Calc

class TestCalc(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(Calc.add(2,3), 5, "should be 5")

    def test_subtract(self):
        self.assertEqual(Calc.subtract(5,3), 2, "should be 2")

    def test_multiply(self):
        self.assertEqual(Calc.multiply(2,3), 6, "should be 6")

    def test_divide(self):
        self.assertEqual(Calc.divide(4,2), 2, "should be 2")

    def test_sqrt(self):
        self.assertEqual(Calc.sqrt(4), 2, "should be 2")

if __name__ == '__main__':
    unittest.main()
