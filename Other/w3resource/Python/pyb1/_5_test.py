import unittest

from _5_reverse_print_fullname import revNames

class ReverseTestCase(unittest.TestCase):

    def test_revNames(self):
        result = revNames("Goran", "Aviani")
        self.assertEqual(result, "naroG inaivA")