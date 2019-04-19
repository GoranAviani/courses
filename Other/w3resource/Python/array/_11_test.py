import unittest
from _11_remove_idem_by_index_list import removeByIndex

class removingTestCase(unittest.TestCase):

    def test_removeByIndex(self):
        result = removeByIndex([3,4,5,6,9],4)
        self.assertEqual(result, [3,4,5,9])