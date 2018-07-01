#Problem: Find the single different char between two strings.
#Test Cases
#
#    None input -> TypeError
#    'abcd', 'abcde' -> 'e'
#    'aaabbcdd', 'abdbacade' -> 'e'

import unittest
import diff_str

class DiffStringTestCase(unittest.TestCase):

    def test_diff_str(self):

        my_diff_str = DifferentStrings()
        self.assertRaises(TypeError, my_diff_str.test_diff_str, None)
        self.assertEqual(my_diff_str.test_diff_str('abcd', 'abcde'), 'e')
        self.assertEqual(my_diff_str.test_diff_str('aaabbcdd', 'abdbacade'), 'e')


