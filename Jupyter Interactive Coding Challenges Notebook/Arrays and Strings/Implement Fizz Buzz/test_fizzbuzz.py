import unittest
import fizzbuzz

class FizzBuzzTestCase(unittest.TestCase):

    def test_fizzbuzz(self):
        my_fizzbuzz = fizzbuzz.FizzBuzz()
        self.assertRaises(TypeError, my_fizzbuzz.fizz_buzz, None)
        self.assertRaises(ValueError, my_fizzbuzz.fizz_buzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        self.assertEqual(my_fizzbuzz.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')