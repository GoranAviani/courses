import unittest
import urlify

class UrlifyTestCase (unittest.TestCase):

    def test_urlify_this(self):
        my_urlify = urlify.do_urlify
        self.assertEqual(my_urlify("test test  "), "test%20test")
        self.assertEqual(my_urlify("test test test    "), "test%20test%20test")