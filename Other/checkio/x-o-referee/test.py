import checkio
import unittest


class TestingTestCase(unittest.TestCase):

    def test_X1(self):
        resultCheckio = checkio.check_io(["XX.", "XXX", "XOX"])
        print(resultCheckio)
        self.assertEqual(resultCheckio, "X")

    def test_X2(self):
        resultCheckio = checkio.check_io(["XX.", "XXO", "XOX"])
        print(resultCheckio)
        self.assertEqual(resultCheckio, "X")

    def test_X3(self):
        resultCheckio = checkio.check_io(["OX.", ".X.", "OXO"])
        print(resultCheckio)
        self.assertEqual(resultCheckio, "X")

    def test_X4(self):
        resultCheckio = checkio.check_io(["O.X", ".XX", "OOX"])
        print(resultCheckio)
        self.assertEqual(resultCheckio, "X")




if __name__ == "__main__":
    unittest.check_io()


