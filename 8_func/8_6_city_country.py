"""City Country.

接收城市的名称及其所属的国家. 并打印.
"""

def city_country(city_name, country):
    """City Country."""
    city_info = city_name + ', ' + country
    return city_info.title()

print(city_country('santiago', 'chile'))
print(city_country('Fishing Island', 'China'))
print(city_country('Taiwan', 'China'))
