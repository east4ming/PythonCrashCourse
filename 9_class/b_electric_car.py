class Car():
    """模拟汽车的简单尝试."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_describe_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('The car has {} miles on it.'.format(self.odometer_reading))
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer.')
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """加满油."""
        pass

class ElectricCar(Car):
    """电动车的独特之处."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息."""
        print('The car has a {}-kWh battery.'.format(self.battery_size))

    def fill_gas_tank():
        """电动车没有油箱."""
        print('This car does not need a gas tank.')
    
my_tesla = ElectricCar('telsa', 'model s', 2016)
print(my_tesla.get_describe_name())
my_tesla.describe_battery()
