'''
@author: Solrac
'''
from RestaurantC import Restaurant

class Fonda(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.close_hours = 21
        
    def close(self):
        print('La fonda', self.name.title(), 'closes at', self.close_hours,"hrs")
        
    def show_hours(self):
        self.description()
        self.open()
print()
fonda1 = Fonda('bajo el cielo de jalisco', 'mexican')
fonda1.show_hours()
fonda1.close()
print()

fonda2 = Fonda('Almida', 'egipcia')
fonda2.show_hours()
fonda2.close()
