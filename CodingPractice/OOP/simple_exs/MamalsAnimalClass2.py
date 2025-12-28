'''
@author: Solrac
'''

from CodingPractice.OOP.simple_exs.AnimalClass2 import Animal2

class Mamals(Animal2):
    def __init__(self, name, type, skill, food):
        super().__init__(name, type, skill, food)
        self.animal_type = 'mamal'
        self.birth_process = 'mother\'s belly'
        self.blood_type = 'warm blood' 
    
    def definition(self):
        print("The {} is a {} animal, this means it was born from {}. Therefore, it is of {}"
              .format(self.name, self.animal_type, self.birth_process, self.blood_type))

