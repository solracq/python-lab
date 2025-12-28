'''
@author: Solrac
'''

class CarBattery:
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh batery')
        
    def upgrage_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85