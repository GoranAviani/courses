#Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.
#Test Cases
#
#    None -> None
#    '' -> ''
#    'AABBCC' -> 'AABBCC'
#    'AAABCCDDDD' -> 'A3BC2D4'

import unittest
import compress_string

class CompressStringTestCase(unittest.TestCase):

    def test_compress_string(self):
        my_compression = compress_string.CompressString()
        self.assertEqual(my_compression.compress_string(""),"")
        self.assertEqual(my_compression.compress_string("AABBCC"), "AABBCC")
        self.assertEqual(my_compression.compress_string("AAABCCDDDDE"), "A3BC2D4E")
        self.assertEqual(my_compression.compress_string("BAAACCDDDD"), "BA3C2D4")
        self.assertEqual(my_compression.compress_string("AAABAACCDDDD"), "A3BA2C2D4")


