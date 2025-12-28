'''
@author: Solrac
'''

from Car import Car
from CarBattery import CarBattery

class CarElectric(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = CarBattery()
        
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
        
    def get_battery_range(self):
        print('Battery range is between 0 to', self.battery.battery_size)