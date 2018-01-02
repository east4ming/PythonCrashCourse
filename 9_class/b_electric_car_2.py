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

class Battery():
    """模拟电动汽车电瓶."""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印一条电动车电瓶的消息."""
        print('The car has a {}-kWh battery.'.format(self.battery_size))
    
    def get_range(self):
        """打印一条消息, 指出电动车的里程."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = 'This car can go approximately {} miles on a full charge.'.format(range)
        print(message)


class ElectricCar(Car):
    """电动车的独特之处."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """电动车没有油箱."""
        print('This car does not need a gas tank.')
    
my_tesla = ElectricCar('telsa', 'model s', 2016)
print(my_tesla.get_describe_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
