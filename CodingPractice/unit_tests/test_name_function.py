'''
@author: Solrac
'''
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('joe', 'doe')
        self.assertEqual(formatted_name, 'john smith')
        
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('john', 'smith', 'dy')
        self.assertEqual(formatted_name, 'john smith')
        
    def test_one_name(self):
        formatted_name = get_formatted_name('jack', '')
        self.assertEqual(formatted_name, 'Test ')
        
unittest.main()
