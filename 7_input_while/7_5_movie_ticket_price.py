"""Movie Ticket Price.

一个电影院, 根据年龄计价:
3岁以内免费, 3-12岁10元, 12岁以上15元.
写一个循环, 问用户年龄, 并打印票价.
"""

# 3 Ways
# 1. input
age_str = ''
while age_str != 'quit':
    age_str = input('How old are you? ')
    if age_str != 'quit':
        age = int(age_str)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        print('You should pay ${}.'.format(price))

# 2. flag
flag = True
while flag:
    age_str = input('How old are you? ')
    if age_str != 'quit':
        age = int(age_str)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        print('You should pay ${}.'.format(price))
    else:
        flag = False

# 3. break
while True:
    age_str = input('How old are you? ')
    if age_str != 'quit':
        age = int(age_str)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        print('You should pay ${}.'.format(price))
    else:
        break
