import unittest
import math
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

    def test_sum_multiple_entries(self):
        x_y_exits = (
            (-5, -5, -10),
            (77, 23, 100),
            (22, 11, 33),
            (1.75, 0.25, 2),
        )

        for x_y_exit in x_y_exits:
            with self.subTest(x_y_exit=x_y_exit):
                x, y, exit = x_y_exit
                self.assertEqual(sum(x, y), exit)

    def test_subtraction_multiple_entries(self):
        x_y_exits = (
            (-8, 10, -18),
            (10, 3, 7),
            (22, 11, 11),
            (100, 100, 0),
        )

        for x_y_exit in x_y_exits:
            with self.subTest(x_y_exit=x_y_exit):
                x, y, exit = x_y_exit
                self.assertEqual(subtraction(x, y), exit)

    def test_multiplication_multiple_entries(self):
        x_y_exits = (
            (4, 4, 16),
            (12, 3, 36),
            (1, 1, 1),
            (0, -2.34, 0),
        )

        for x_y_exit in x_y_exits:
            with self.subTest(x_y_exit=x_y_exit):
                x, y, exit = x_y_exit
                self.assertEqual(multiplication(x, y), exit)

    def test_division_multiple_entries(self):
        x_y_exits = (
            (125, 25, 5),
            (12, 3, 4),
            (77, 1, 77),
            (128, 128, 1),
        )

        for x_y_exit in x_y_exits:
            with self.subTest(x_y_exit=x_y_exit):
                x, y, exit = x_y_exit
                self.assertEqual(division(x, y), exit)

    def test_exponentiation_multiple_entries(self):
        x_y_exits = (
            (5, 5, 3125),
            (1, 2, 1),
            (2, 2, 4),
            (8, 3, 512),
        )

        for x_y_exit in x_y_exits:
            with self.subTest(x_y_exit=x_y_exit):
                x, y, exit = x_y_exit
                self.assertEqual(exponentiation(x, y), exit)

    def test_sum_not_int_or_float_return_assertion_error(self):
        with self.assertRaises(AssertionError):
            sum("fruits", 1)

    def test_subtraction_not_int_or_float_return_assertion_error(self):
        with self.assertRaises(AssertionError):
            subtraction(math.sqrt(100), "1")

    def test_multiplication_not_int_or_float_return_assertion_error(self):
        with self.assertRaises(AssertionError):
            multiplication("3.1416", 123)

    def test_division_not_int_or_float_return_assertion_error(self):
        with self.assertRaises(AssertionError):
            division("green", 200)

    def test_exponentiation_not_int_or_float_return_assertion_error(self):
        with self.assertRaises(AssertionError):
            exponentiation(2, "blue")


if __name__ == '__main__':
    unittest.main(verbosity=2)
