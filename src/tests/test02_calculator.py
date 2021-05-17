import unittest

from src.base.calculator import sum, subtraction, multiplication, division, exponentiation


class TestCalculator(unittest.TestCase):
    def test_sum_5_and_25_return_30(self):
        self.assertEqual(sum(5, 25), 30)

    def test_subtraction_10_and_15_return_minus_5(self):
        self.assertEqual(subtraction(5, 15), -10)

    def test_multiplication_2_and_2_return_4(self):
        self.assertEqual(multiplication(2, 2), 4)

    def test_division_100_and_10_return_10(self):
        self.assertEqual(division(100, 10), 10)

    def test_exponentiation_4_and_4_return_64(self):
        self.assertEqual(exponentiation(4, 4), 256)


if __name__ == '__main__':
    unittest.main(verbosity=2)
