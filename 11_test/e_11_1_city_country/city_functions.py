"""City and Country.

接受2个形参: 城市名和国家名.
返回格式为"City, Country"的字符串.

e_11_2:
添加第三个必须形参: population
返回格式为"City, Country - population xxx"字符串
"""

def city_info(city, country, population=''):
    """return "City, Country - population xxx" string."""
    the_city = ('{}, {}'.format(city, country)).title()
    if population:
        the_city += ' - population {}'.format(population)
    return the_city
