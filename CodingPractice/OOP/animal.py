class Animal:
    count = 0
    def __init__(self, species, name, sound):
        self._species = species
        self._name = name
        self._sound = sound
        Animal.count += 1

    def kill(self):
        if Animal.count == 0:
            return None
        Animal.count -= 1

    @property # To specify a Getter method
    def species(self):
        return self._species

    @property # To specify a Getter method
    def name(self):
        return self._name

    def make_sound(self):
        return self._sound

    @staticmethod
    def tformat(string:str):
        return string.title()

    @classmethod
    def zoo_size(cls):
        return cls.count

if __name__ == "__main__":
    leo = Animal("African Lion", "Leo", "Roarrrrrr")
    garfield = Animal("cat", "Garfield", "Meowwwww")
    felix = Animal("cat", "Felix", "Meowwwww")

    print(f"{leo.name} is a {Animal.tformat(leo.species)} -- {leo.make_sound()}")
    print(f"{garfield.name} is a {Animal.tformat(garfield.species)} -- {garfield.make_sound()}")
    print(f"{felix.name} is a {Animal.tformat(felix.species)} -- {felix.make_sound()}")
    print(f"The size of the Zoo is {Animal.zoo_size()}")

################ Tests ####################################
import pytest

@pytest.fixture
def animal_count():
    # Setup
    Animal.count = 0

    yield Animal.count

    # Teardown: Cleaning up count
    Animal.count = 0

def test_class_states(animal_count):
    animal1 = Animal("Leo", "Lion", "Roarrr")
    assert Animal.count == 1, f"{Animal.count} is incorrect!"
    animal2 = Animal("Felix", "Cat", "Meaooo")
    assert Animal.count == 2, f"{Animal.count} is incorrect!"
    animal2.kill()
    assert Animal.count == 1, f"{Animal.count} is incorrect!"\

def test_animal_attributes(animal_count):
    animal = Animal("Leo", "Lion", "Roarrr")
    assert animal.name == "Leo", f"{animal.name} is incorrect!"
    assert animal.species == "Lion", f"{animal.species} is incorrect!"
    assert animal.sound == "Roarrr", f"{animal.sound} is incorrect!"

def test_animal_attributes_setters(animal_count):
    animal = Animal("Leo", "Lion", "Roarrr")
    animal.name = "Felix"
    animal.species = "Feline"
    animal.sound = "Meaooo"
    assert animal.name == "Felix", f"{animal.name} is incorrect!"
    assert animal.species == "Feline", f"{animal.species} is incorrect!"
    assert animal.sound == "Meaooo", f"{animal.sound} is incorrect!"