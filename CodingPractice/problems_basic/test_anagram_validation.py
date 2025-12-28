'''
@author: Solrac
'''
import unittest
from CodingPractice.problems_basic.anagram_validation import anagram_validation1
from CodingPractice.problems_basic.anagram_validation import dictionary_counter
from CodingPractice.problems_basic.anagram_validation import compare_dictionaries

class AnagramTestCase(unittest.TestCase):
    def setUp(self):
        str1= "cinema"
        str2= "iceman"
        str3= "icemar"
        self.anagram_success = anagram_validation1(str1, str2)
        self.anagram_failure = anagram_validation1(str1, str3)
        self.dict1 = dictionary_counter(str1)
        self.dict2 = dictionary_counter(str2)
        self.dict3 = dictionary_counter(str3)
        
    def test_verify_successful(self):
        self.assertTrue(self.anagram_success, "The result is False!")
        
    def test_verify_failure(self):
        self.assertFalse(self.anagram_failure, "The result is True")
        
    def test_verify_compare_successful(self):
        anagram_compare_success = compare_dictionaries(self.dict1, self.dict2)
        self.assertTrue(anagram_compare_success, "The result is False!")
        
    def test_verify_compare_failure(self):
        anagram_compare_failure = compare_dictionaries(self.dict1, self.dict3)
        self.assertFalse(anagram_compare_failure, "The result is True")
    
unittest.main()