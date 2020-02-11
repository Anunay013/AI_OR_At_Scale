import unittest
import division

class TestMyModule(unittest.TestCase):

    def setUp(self):
        return

    def test_do_divide(self):
        first_arg = 4
        second_arg = 2

        result = division.divide(first_arg, second_arg)

        expected_result = 2

        self.assertEqual(result, expected_result)

    def divide_by_zero(self):
        a = 2
        b = 0

        result = division.divide(a, b)

        self.assertEqual(result, "Invalid")
