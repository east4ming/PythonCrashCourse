"""Test city_functions.py.

"""

import unittest

from city_functions import city_info

class CitiesTestCase(unittest.TestCase):
    """测试 city_functions.py"""

    def test_city_country(self):
        city_country = city_info('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')
    def test_city_country_population(self):
        city_country_population = city_info('santiago', 'chile', '5000000')
        self.assertEqual(city_country_population, 'Santiago, Chile - population 5000000')
unittest.main()
