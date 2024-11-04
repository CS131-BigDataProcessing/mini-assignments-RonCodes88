import unittest
from math_functions import power, divide
import math

class TestMathFunctions(unittest.TestCase):

    def test_power(self):
        self.assertEqual(power(3,2),9)
        self.assertEqual(power(3,0),1)
        self.assertEqual(power(-2,2),4)
        self.assertEqual(power(4,-1),0.25)
        self.assertEqual(power(4,-3), 1/64)
        self.assertEqual(power(1/2,2),1/4)
        self.assertEqual(power(-4,3), -64)
        self.assertEqual(power(0,3), 0)
        self.assertEqual(power(2,1/2), math.sqrt(2))

    def test_divide(self):
        self.assertEqual(divide(5,0), "Cannot divide by 0")
        self.assertEqual(divide(10,2), 5)
        self.assertEqual(divide(1,2), 0.5)
        self.assertEqual(divide(-10,2), -5)
        self.assertEqual(divide(10,-2), -5)
        self.assertEqual(divide(0,2), 0)
        self.assertEqual(divide(-10,-2), 5)


if __name__ == '__main__':
        unittest.main()


