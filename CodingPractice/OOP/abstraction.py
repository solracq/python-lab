from abc import ABC, abstractmethod # Abstract Base Class

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @property
    @abstractmethod
    def species(self): # Abstract Property: abstract methods used for properties. To make sure subclasses have certain attribute
        pass

    def move(self): # Concrete methods: methods in Abstract class with implementation
        return "Walk the walk, talk the talk"

class Dog(Animal):
    def speak(self):
        return "woof"

    @property
    def species(self):
        return "Canine"

class Cat(Animal):
    def speak(self):
        return "meow"

    @property
    def species(self):
        return "Feline"

animals = [Dog(), Cat()]
for pet in animals:
    print(pet.speak(), pet.species, pet.move())
