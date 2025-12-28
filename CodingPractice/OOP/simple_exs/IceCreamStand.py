'''
@author: Solrac
'''
from CodingPractice.OOP.simple_exs.RestaurantC import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['strawberry', 'chocolate', 'vanilla', 'pistacho', 'mango', 'coconut']
        
    def print_flavors(self):
        self.description()
        print('Available ice-cream flavors: ')
        for flavor in self.flavors:
            print(flavor)
            
icecream = IceCreamStand('La Dolce Vita', 'italian')
icecream.open()
icecream.print_flavors()
