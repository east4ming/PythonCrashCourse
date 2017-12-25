"""Favorite Places.

调查用户的度假胜地. 
使用类似"If you could visit one place in the world, where would you go?"
并打印调查结果.
"""

prompt = 'If you could visit one place in the world, where would you go? '
favorite_places = {}
while True:
    name = input('\nWhat is your name? ')
    favorite_place = input(prompt)
    favorite_places[name] = favorite_place
    repeat = input('Would you like to another person to respond? (yes/no)')
    if repeat == 'no':
        break
print('\n--- Favorite Places Results ---')
for name, favorite_place in favorite_places.items():
    print('{}\'s favorite place is {}.'.format(name, favorite_place.upper()))
