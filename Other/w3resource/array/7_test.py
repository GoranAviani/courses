import unittest
from a7_append_elements_of_list_to_list import addingToList

class ListsTestCase(unittest.TestCase):

   def test_addingToList(self):
       result = addingToList([1, 3, 5, 7, 9])
       self.assertEqual(result, [1, 3, 5, 7, 9, 1, 3, 5, 7, 9])