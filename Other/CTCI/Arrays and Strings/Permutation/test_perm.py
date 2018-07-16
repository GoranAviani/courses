import unittest
import perm

class PermutationTestCase(unittest.TestCase):

    def test_check_permutatiin(self):
        my_perm = perm.check_permutation
        self.assertEqual(my_perm("dog", "god"), True)
        self.assertEqual(my_perm("stpauli", "stpauli"), False)
        self.assertEqual(my_perm("mmamm", "mmamm"), True)