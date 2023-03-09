import math
import unittest
from calculator import Calculator


class ApplicationTest(unittest.TestCase):

    def test_add(self):
        test_cases = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        for tc in test_cases:
            ret = Calculator.add(*tc)
            ans = tc[0] + tc[1]
            self.assertEqual(ret, ans)
        with self.assertRaises(TypeError):
            Calculator.add(1, '0')

    def test_divide(self):
        test_cases = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        for tc in test_cases:
            ret = Calculator.divide(*tc)
            ans = tc[0] / tc[1]
            self.assertEqual(ret, ans)
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(1, 0)

    def test_sqrt(self):
        test_cases = [1, 2, 3, 4, 5]
        for tc in test_cases:
            ret = Calculator.sqrt(tc)
            ans = math.sqrt(tc)
            self.assertEqual(ret, ans)
        with self.assertRaises(ValueError):
            Calculator.sqrt(-1)

    def test_exp(self):
        test_cases = [1, 2, 3, 4, 5]
        for tc in test_cases:
            ret = Calculator.exp(tc)
            ans = math.exp(tc)
            self.assertEqual(ret, ans)
        with self.assertRaises(TypeError):
            Calculator.exp('0')


if __name__ == '__main__':
    unittest.main()
