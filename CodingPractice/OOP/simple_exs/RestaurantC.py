'''
@author: Solrac
'''
class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_serverd = 0
        self.days = 0
        
    def description(self):
        print('The Restaurant', self.name.title(), 'is of', self.type.title(), 'cuisine')
        
    def open(self):
        print(self.name.title(), 'is open')
        
    def set_number_served(self):
        self.number_serverd = int(input("How many users have been serving? "))
        self.days = int(input("How many days have been serving? "))
        
    def print_number_served(self):
        print('The restaurant', self.name, 'has been serving to', self.number_serverd, 'customers')
        
    def increment_number_served(self):
        print('The restaurant', self.name, 'has served', self.number_serverd * int(self.days), 'users in', int(self.days), 'days')
        
restaurant = Restaurant('The godfather', 'italian')
restaurant.description()
restaurant.open()
restaurant.print_number_served()
restaurant.set_number_served()
restaurant.print_number_served()
restaurant.increment_number_served()
print()

mxrestaurant = Restaurant('Tortas Cheli', 'mexican')
mxrestaurant.description()
mxrestaurant.open()
mxrestaurant.print_number_served()
mxrestaurant.set_number_served()
mxrestaurant.print_number_served()
mxrestaurant.increment_number_served()
print()

chrestaurant = Restaurant('the chao-main', 'chinese')
chrestaurant.description()
chrestaurant.open()
chrestaurant.print_number_served()
chrestaurant.set_number_served()
chrestaurant.print_number_served()
chrestaurant.increment_number_served()