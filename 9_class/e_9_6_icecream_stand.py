"""IceCreamStand.

继承 Restaurant 类. 添加 flavors 的属性, 用于存储一个由各种口味的冰淇淋组成的列表.
编写一个显示这些冰淇淋的方法. 创建一个 IceCreamStand 实例, 并调用这个方法.
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

class IceCreamStand(Restaurant):
    """IceCreamStand."""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def describe_flavors(self):
        print('The IceCreamStand contains: ')
        for flavor in self.flavors:
            print('- {}'.format(flavor))

icecream_stand = IceCreamStand('aixixili', 'desert', ['caomei', 'lvcao', 'juzi'])
icecream_stand.describe_flavors()
icecream_stand.describe_restaurant()
icecream_stand.open_restaurant()
