# Do "list" exercise
bicyles = ['trek', 'cannondale', 'redline', 'speialized']
print(bicyles)
# Index
print(bicyles[0])
print(bicyles[0].title)
# Index -1
print(bicyles[-1])
message = 'My first bicycle was a' + bicyles[0].title() + '.'
print(message)
# Edit list element
bicyles[0] = 'ducati'
# list append
bicyles.append('ducati')
print(bicyles)
# Empty list && append element
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# Insert element to list
motorcycles.insert(0, 'ducati')
print(motorcycles)
# `del` list element
del motorcycles[0]
print(motorcycles)
# `pop` list element
print(motorcycles)
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + '.')
# `pop` any element
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + '.')
# `remove` list element based value
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("\nA" + too_expensive.title() + " is too expensive for me.")
