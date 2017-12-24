"""Cities

创建一个名为 cities 的字典, 其中将三个城市作为key;
对于每座城市, 都创建一个字典, 并在其中包含该城市所属的国家/人口约数以及关于该城市的事实.
即 country/population/fact. 将每个城市的名字及有关的信息打印出来.
"""

cities = {
    'xi an': {
        'country': 'china',
        'population': 1000000,
        'fact': 'The six dynasties of the ancient capital'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 10000000,
        'fact': 'Tokyo Hot!'
    },
    'New York': {
        'country': 'USA',
        'population': 9000000,
        'fact': 'Bat Man.'
    }
}
for city, city_infos in cities.items():
    print('The city\'s information: {}'.format(city.title()))
    for k, v in city_infos.items():
        print('\tIt\'s {} is {}'.format(k, v))

cities['England'] = {
    'country': 'UK',
    'population': 2095039,
    'fact': 'gay gay'
}

print(cities['England'])
