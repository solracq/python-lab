'''
@author: Solrac
'''

"""A class that can be used to represent a car"""

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
             
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print('This car has', str(self.odometer_reading), "miles on it!")
        
    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print('You cannot roll back an odometer')
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
    def fill_gas_tank(self):
        print('Filling tank...')
    
    
my_new_car = Car('BMW', 's4', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(45)
my_new_car.read_odometer()
my_new_car.increment_odometer(5)
my_new_car.read_odometer()
print()

my_used_car = Car('Nissan', 'Versa', 2007)
print(my_used_car.get_descriptive_name())
my_used_car.increment_odometer(100)
my_used_car.read_odometer()