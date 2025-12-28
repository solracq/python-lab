'''
@author: Solrac
'''

from Car import Car
from CarElectric import CarElectric

if __name__ == "__main__":
    my_new_car = Car("Mazda", "CX-9", 2003)
    print('My car\'s description :', my_new_car.get_description_name())
    print('My car\'s odometer is :', my_new_car.get_odometer())
    my_new_car.update_odometer(70)
    my_new_car.read_odomoter()
    my_new_car.increment_odometer(5)
    my_new_car.read_odomoter()
    my_new_car.fill_gas_tank()
    print()
    my_new_electric_car = CarElectric('Tesla', 'Model S', 2018)
    print('My car\'s description :', my_new_electric_car.get_description_name())
    print('My car\'s odometer is :', my_new_electric_car.get_odometer())
    my_new_electric_car.fill_gas_tank()
    my_new_electric_car.get_battery_range()
    