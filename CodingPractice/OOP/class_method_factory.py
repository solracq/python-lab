from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def by_bdate(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __str__(self):
        return f"{self.name} is {self.age}. Is the person an adult? {Person.is_adult(self.age)}"

person1 = Person("John", 45)
print(person1)
person2 = Person.by_bdate("Tessio", 1975)
print(person2)