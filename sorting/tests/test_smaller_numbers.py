import unittest
from ..smaller_numbers import smallerNumbersThanCurrent


class TestSmallerNumber(unittest.TestCase):
    '''tests smaller number'''

    def test_smaller(self):
        nums = [8, 1, 2, 2, 3]
        result = smallerNumbersThanCurrent(nums)
        expected = [4, 0, 1, 1, 3]
        self.assertEqual(result, expected)

    def test_smaller_for_random_numbers(self):
        nums = [6, 5, 4, 8]
        result = smallerNumbersThanCurrent(nums)
        expected = [2, 1, 0, 3]
        self.assertEqual(result, expected)

    def test_smaller_for_equal_nums(self):
        nums = [7, 7, 7, 7, 7]
        result = smallerNumbersThanCurrent(nums)
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(result, expected)
