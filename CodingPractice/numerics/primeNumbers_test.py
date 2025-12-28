'''
@author: Solrac
'''
import unittest
from Queue import prime

class test_prime(unittest.TestCase):
    def setUp(self):
        self.prime = prime()
        
    def test_first_primes(self):
        self.assertTrue(self.prime, "No output")
        
unittest.main()