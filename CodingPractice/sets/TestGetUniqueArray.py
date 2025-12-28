'''
@author: Solrac
'''
import unittest
from CodingPractice.sets.GetUnique import get_unique

class GetUniqueTestCase(unittest.TestCase):
    def setUp(self):
        s1 = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
        s2 = ["THREE", "SEVEN", "EIGHT", "FOUR", "THREE"]
        my_unique = get_unique(s1, s2)

    def test_getu1(self):
        s1 = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
        s2 = ["THREE", "SEVEN", "EIGHT", "FOUR", "THREE"]
        
        self.assertEqual(get_unique(s1, s2), ['THREE', 'FOUR'])
        
unittest.main()