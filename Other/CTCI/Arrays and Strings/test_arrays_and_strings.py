import unittest
import arrays_and_strings

class ArraysTestCase(unittest.TestCase):

    def test_unique(self):
        my_unique = arrays_and_strings.unique
        self.assertEqual(my_unique("aaabb"), False)
        self.assertEqual(my_unique("abcde"), True)
        self.assertEqual(my_unique("abcde312"), True)
        self.assertEqual(my_unique("abcde33"), False)