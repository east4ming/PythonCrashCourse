my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods.append('ice cream')
print('My favorite foods are: ')
for my_food in my_foods:
    print(my_food)
print("My friend's favorite foods are: ")
for friend_food in friend_foods:
    print(friend_food)
