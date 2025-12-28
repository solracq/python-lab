'''
@author: Solrac
'''

from CodingPractice.OOP.simple_exs.AnimalClass2 import Animal2
from MamalsAnimalClass2 import Mamals

if __name__ == "__main__":
    animal_cats = Animal2('Lion', 'big predator cat', 'strong', 'any animal')
    animal_cats.increase_speed(30)
    animal_cats.print_animal_data()
    animal_mamal = Mamals('Lion', 'big predator cat', 'strong', 'any animal')
    animal_mamal.print_animal_data()
    print()
    animal_cats.set_name("Puma")
    animal_cats.set_skill("strong")
    animal_cats.set_type("alone nocturnal hunter")
    animal_cats.set_food("nocturnal prays")
    animal_cats.increase_speed(15)
    animal_cats.print_animal_data()