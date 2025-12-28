'''
@author: Solrac
'''

from CodingPractice.OOP.simple_exs.AnimalClass import animal

class mamals(animal):
    def __init__(self, name, types, skill, food):
        super().__init__(name, types, skill, food)
        self.animal_type = 'mammal'
        self.birth_process = 'mother\'s belly'
        self.blood_type = 'warm blood'
        
    def definition(self):
        print('The {} is a {} animal, this means it was born from {}. Therefore, it is of {}'.format(self.name, self.animal_type, self.birth_process, self.blood_type))