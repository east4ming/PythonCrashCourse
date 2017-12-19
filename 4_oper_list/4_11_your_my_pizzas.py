pizzas = ['Pizza Hut', "Papa John's", "Domino"]
friend_pizzas = pizzas[:]
pizzas.append('Pizza Panic')
friend_pizzas.append('Turbo Pizza')
print('My favorite pizzas are: ')
for my_pizza in pizzas:
    print(my_pizza)
print("My friend's favorite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
