'''
@author: Solrac
'''
from city_function import city_format

def collect_print_cityformat():
    print("Press 'q' to quit at any time")
    
    while True:
        city= input("provide city: ")
        if city == 'q':
            break
        
        country= input('provide country: ')
        if country == 'q':
            break
        
        population = input('provide population: ')
        if population == 'q':
            break
        
        cityformat= city_format(city, country, population)
        print(cityformat)
    
collect_print_cityformat()