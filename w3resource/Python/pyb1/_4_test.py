import unittest
from ._4_radius import calc_radius

class RadiusTestCase(unittest.TestCase):

    def test_calc_radius(self):
        result = calc_radius(1)
        self.assertEqual(result, 6.28)