#Determine if a string s1 is a rotation of another string s2, by calling (only once) a function is_substring


#Test Cases
#
#    Any strings that differ in size -> False
#    None, 'foo' -> False (any None results in False)
#   ' ', 'foo' -> False
#    ' ', ' ' -> True
#    'foobarbaz', 'barbazfoo' -> True

import unittest
import string_rotation

class StringRotationTestCase(unittest.TestCase):

    def test_is_substring(self):
        my_permutation = string_rotation.Permutation()

        self.assertEqual(my_permutation.is_rotation('o', 'oo'), False)
        self.assertEqual(my_permutation.is_rotation(None, 'foo'), False)
        self.assertEqual(my_permutation.is_rotation('', 'foo'), False)
        self.assertEqual(my_permutation.is_rotation('', ''), True)
        self.assertEqual(my_permutation.is_rotation('foobarbaz', 'barbazfoo'), True)
