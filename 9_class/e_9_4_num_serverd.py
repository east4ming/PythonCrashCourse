"""Restaurant.

创建一个 Restaurant 类, 初始化方法3个属性:
restaurant_name 和 cuisine_type 和 number_served()
个方法:
- describe_restaurant()
- open_restaurant()
"""


class Restaurant():
    """Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Init Restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print Restaurant Info."""
        print('The Restaurant\'s Infomation are: ')
        print('\t- Restaurant_name: {}'.format(self.restaurant_name.title()))
        print('\t- Cuisine_type: {}'.format(self.cuisine_type.title()))

    def open_restaurant(self):
        """Open the Restaurant."""
        print('The Restaurant is running.')
    
    def set_number_served(self, number_served):
        """Set number served."""
        self.number_served = number_served
    
    def increment_number_served(self, everyday_nums):
        """Everyday nums served."""
        self.number_served += everyday_nums

shaxian = Restaurant('shaxian snap', 'SouthEast Chinese Food')
print('The number of the restaurant served is {}'.
      format(shaxian.number_served))
shaxian.number_served = 999
print('The number of the restaurant served is {}'.
      format(shaxian.number_served))
shaxian.set_number_served(1001)
print('The number of the restaurant served is {}'.
      format(shaxian.number_served))
shaxian.increment_number_served(99)
print('The number of the restaurant served is {}'.
      format(shaxian.number_served))
# shaxian.describe_restaurant()
# shaxian.open_restaurant()

# lanla = Restaurant('lanzhou noddles', 'NorthWest Chinese Food')
# lanla.describe_restaurant()
# guifen = Restaurant('guilin rice noodles', 'South Chinese Food')
# guifen.describe_restaurant()
