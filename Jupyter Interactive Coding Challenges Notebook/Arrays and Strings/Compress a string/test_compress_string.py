#Compress a string such that 'AAABCCDDDD' becomes 'A3BCCD4'. Only compress the string if it saves space.
#Test Cases
#
#    None -> None
#    '' -> ''
#    'AABBCC' -> 'AABBCC'
#    'AAABCCDDDD' -> 'A3BCCD4'

import unittest
import compress_string

class CompressStringTestCase(unittest.TestCase):

    def test_compress_string(self):
        my_compression = compress_string.CompressString()
        self.assertEqual(my_compression.compress_string(""),"")
        self.assertEqual(my_compression.compress_string("AABBCC"), "AABBCC")
        self.assertEqual(my_compression.compress_string("AAABCCDDDDE"), "A3BCCD4E")
        self.assertEqual(my_compression.compress_string("BAAACCDDDD"), "BA3CCD4")
        self.assertEqual(my_compression.compress_string("AAABAACCDDDD"), "A3BAACCD4")


