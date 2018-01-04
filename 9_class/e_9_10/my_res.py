import restaurant

shaxian = restaurant.Restaurant('shaxian snap', 'SouthEast Chinese Food')
print(shaxian.restaurant_name.title())
print(shaxian.cuisine_type.title())

shaxian.describe_restaurant()
shaxian.open_restaurant()

lanla = restaurant.Restaurant('lanzhou noddles', 'NorthWest Chinese Food')
lanla.describe_restaurant()
guifen = restaurant.Restaurant('guilin rice noodles', 'South Chinese Food')
guifen.describe_restaurant()
