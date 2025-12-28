'''
@author: Solrac
'''
import unittest
from first_duplicate import first_dup

class FirstDuplicateTestCase(unittest.TestCase):
    def setUp(self):
        self.str = "ABCA"
        self.str2 = "BCABA"
        self.str3 = "ABC"
        
    def test_str1_validation(self):
        my_first_duplicate = first_dup(self.str)
        self.assertEqual(my_first_duplicate, 'A')
        
    def test_str2_validation(self):
        my_first_duplicate = first_dup(self.str2)
        self.assertEqual(my_first_duplicate, 'B')
        
    def test_neg_validation(self):
        my_first_duplicate = first_dup(self.str3)
        self.assertEqual(my_first_duplicate, None)
        
unittest.main()