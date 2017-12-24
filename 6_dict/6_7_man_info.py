yangxin = {
    'first_name': 'Yang',
    'last_name': 'Xin',
    'age': 26,
    'city': 'Xiamen',
    }
casey = {
    'first_name': 'Cui',
    'last_name': 'Kaidong',
    'age': 26,
    'city': 'Shanghai'
}
eve = {
    'first_name': 'Yao',
    'last_name': 'Yanping',
    'age': 26,
    'city': 'Wuxi'
}
people = [yangxin, casey, eve]
for person in people:
    for k, v in person.items():
        print('{}: \t{}'.format(k, v))
