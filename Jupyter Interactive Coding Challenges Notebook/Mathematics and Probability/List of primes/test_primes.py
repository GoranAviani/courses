import unittest
import compress_string

class CompressStringTestCase(unittest.TestCase):

    def test_generate_primes(self):
        my_primes= primes.PrimeGenerator()
        self.assertRaises(TypeError, my_primes.generate_primes, None)
    	self.assertRaises(TypeError, prime_generator.generate_primes, 98.6)
        self.assertEqual(my_primes.generate_primes(20), [False, False, True, 
                                                           True, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True])
 
        print('Success: generate_primes')