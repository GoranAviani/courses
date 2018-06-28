import unittest
import permutation

class PermutationTestCase(unittest.TestCase):

    def test_permutation(self):
        my_permutation = permutation.Permutation()
        self.assertEqual(my_permutation.check_permutation((None, "foo")), False)
        self.assertEqual(my_permutation.check_permutation(("", "foo")), False)
        self.assertEqual(my_permutation.check_permutation(("Nib", "foo")), False)
        self.assertEqual(my_permutation.check_permutation(("act", "cat")), True)
        self.assertEqual(my_permutation.check_permutation(("a ct", "ca t")), True)