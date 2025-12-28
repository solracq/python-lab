'''
@author: Solrac
'''
import unittest
from city_function import city_format

class Cities_TestCase(unittest.TestCase):
    def test_city_country(self):
        cityformat= city_format('buenos aires', 'argentina')
        self.assertEqual(cityformat, "Buenos Aires, Argentina")
        
    def test_city_country_population(self):
        cityformatpopulation = city_format('montevideo', 'uruguay', "233435642")
        self.assertEqual(cityformatpopulation, "Montevideo, Uruguay, 233435642")

unittest.main()

