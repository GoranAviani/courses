#Problem: Implement a function to reverse a string (a list of characters), in-place.

#Test Cases
#None -> None
#[''] -> ['']
#['f', 'o', 'o', ' ', 'b', 'a', 'r'] -> ['r', 'a', 'b', ' ', 'o', 'o', 'f']



import unittest
import reverse_string

class testingReverseStrings(unittest.TestCase):



    def test_has_unique_word(self):
        my_reverse = reverse_string.ReverseString()
        self.assertEqual(my_reverse.reversing_string(None), False)
        self.assertEqual(my_reverse.reversing_string(""), True)
        self.assertEqual(my_reverse.reversing_string(['f', 'o', 'o', ' ', 'b', 'a', 'r']), ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
      