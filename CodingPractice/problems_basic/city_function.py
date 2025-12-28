'''
@author: Solrac
'''
def city_format(city, country, population=None):
    
    if population:
        city_country = city.title() + ", " + country.title() + ", " + population
    else:
        city_country = city.title() + ", " + country.title()
    return city_country
