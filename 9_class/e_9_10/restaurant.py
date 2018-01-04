"""Restaurant.

创建一个 Restaurant 类, 初始化方法2个属性:
restaurant_name 和 cuisine_type 
2个方法:
- describe_restaurant()
- open_restaurant()
"""


class Restaurant():
    """Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Init Restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print Restaurant Info."""
        print('The Restaurant\'s Infomation are: ')
        print('\t- Restaurant_name: {}'.format(self.restaurant_name.title()))
        print('\t- Cuisine_type: {}'.format(self.cuisine_type.title()))

    def open_restaurant(self):
        """Open the Restaurant."""
        print('The Restaurant is running.')
