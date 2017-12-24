"""Liked Places

创建一个名为 favorite_places 的字典.
在这个字典中, 将三个人的名字用作key;
对于其中的某个人, 都储存他喜欢的1-3个地方.
遍历该字典, 并将每个人和喜欢的地方打印出来.
"""

favorite_places = {
    'casey': ['hedong', 'nanjing', 'wuxi'],
    'eve': ['shenzhen', 'chongqing', 'wuxi'],
    'yangxin': ['xiamen', 'shanghai', 'xian']
}
for person, places in favorite_places.items():
    print('{}\'s favorite places are: '.format(person))
    for place in places:
        print('\t{}'.format(place), end='\t')
    print()
