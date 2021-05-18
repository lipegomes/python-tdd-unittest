"""
TDD - Test Driven Development
"""

import unittest

from src.base.bacon_with_eggs import bacon_with_eggs


class TestBaconWithEggs(unittest.TestCase):
    def test_bacon_with_eggs_assertion_error_do_not_receive_int(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs('')

    def test_bacon_with_eggs_return_bacon_with_eggs_if_the_input_is_a_multiple_of_3_and_5(self):
        inputs = (15, 30, 90, 120)
        output = "Bacon with Eggs"

        for input in inputs:
            with self.subTest(input=input, output=output):
                self.assertEqual(
                    bacon_with_eggs(input),
                    output,
                    msg=f"'{input}' id not return the '{output}'"
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)
