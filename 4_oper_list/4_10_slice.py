cubes = [x**3 for x in range(1, 11)]
print("The first three items in the list are:")
for cube in cubes[:3]:
    print(cube)

print("Three items from the middle of the list are: ")
for cube in cubes[4:7]:
    print(cube)

print("The last three items in the list are: ")
for cube in cubes[-3:]:
    print(cube)
