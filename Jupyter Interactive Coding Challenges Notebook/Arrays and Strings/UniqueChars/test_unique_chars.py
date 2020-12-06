#Test Cases
#None -> False
#'' -> True
#'foo' -> False
#'bar' -> True


import unittest
import unique_chars

class testingUniqueChars(unittest.TestCase):



    def test_has_unique_word(self):
        my_unique = unique_chars.UniqueChars()
        self.assertEqual(my_unique.has_unique_char(None), False)
        self.assertEqual(my_unique.has_unique_char(""), True)
        self.assertEqual(my_unique.has_unique_char("foo"), False)
        self.assertEqual(my_unique.has_unique_char("bar"), True)
