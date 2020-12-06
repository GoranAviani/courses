#Problem: Given an array, find the two indices that sum to a specific value.
#Test Cases
#    None input -> TypeError
#    [] -> ValueError
#    [1, 3, 2, -7, 5], 7 -> [2, 4]

import unittest
import two_sum

class SumStringsTestCase(unittest.TestCase):

    def test_two_sum(self):
        my_two_sum = two_sum.TwoSum()

        self.assertRaises(TypeError, my_two_sum.calculate_two_sum, None)
        self.assertRaises(ValueError, my_two_sum.calculate_two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        self.assertEqual(my_two_sum.calculate_two_sum(nums, target), expected)