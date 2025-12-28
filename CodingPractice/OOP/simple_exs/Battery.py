'''
@author: Solrac
'''
'''A class that can be used to represent a Battery'''
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')
        
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85