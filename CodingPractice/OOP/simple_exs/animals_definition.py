'''
@author: Solrac
'''
from AnimalClass import animal
from MamalsAnimalClass import mamals

if __name__ == '__main__':
    animal_cats = animal('Lion', 'big predator cat', 'strong', 'any animal')
    animal_cats.set_speed(30)
    animal_cats.print_animal_data()
    animal_mamal = mamals('Lion', 'big predator cat', 'strong', 'any animal')
    animal_mamal.definition()
    
    print()
    animal_cats.set_name('Cheeta')
    animal_cats.set_type('predator cat')
    animal_cats.set_skill('fast')
    animal_cats.set_food('fast animals')
    animal_cats.show_speed()
    animal_cats.increase_speed()
    animal_cats.increase_speed()
    animal_cats.increase_speed()
    animal_cats.print_animal_data()
    animal_mamal = mamals(animal_cats.get_name(), animal_cats.get_type(), animal_cats.get_skill(), animal_cats.get_food())
    animal_mamal.definition()
    
    
    

        