'''
@author: Solrac
'''
import Restaurant

def restaurant_test(name, cuisine):
    my_restaurant = Restaurant.Restaurant(name, cuisine)
    
    print(my_restaurant.restaurant_name)
    print(my_restaurant.cuisine_type)
    
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
    
restaurant_test("Munich", "Familiar")
restaurant_test("Bajo el cielo de jalisco", "carne caballo")
restaurant_test("Cueva del zorro", "Nortenia")