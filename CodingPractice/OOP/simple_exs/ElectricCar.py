'''
@author: Solrac
'''
from CodingPractice.OOP.simple_exs.Car import Car
from Battery import Battery

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
        
    def get_battery_range(self):
        print('Battery range is between 0 to', self.battery.battery_size)
        
my_tesla = ElectricCar('Tesla', 'model S', '2016')
print()
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.get_battery_range()
my_tesla.battery.upgrade_battery()
my_tesla.get_battery_range()