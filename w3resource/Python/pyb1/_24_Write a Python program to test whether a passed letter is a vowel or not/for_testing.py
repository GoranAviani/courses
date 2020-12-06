import unittest
from file24 import check_vowel

class VowelTestCase(unittest.TestCase):

   def test_if_vowel(self):
        result = check_vowel("a")
        self.assertEqual(result, "Vowel")

        result = check_vowel("b")
        self.assertEqual(result, "Not vowel")

        result = check_vowel("c")
        self.assertEqual(result, "Not vowel")

        result = check_vowel("e")
        self.assertEqual(result, "Vowel")