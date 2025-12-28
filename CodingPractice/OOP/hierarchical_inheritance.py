class Person:
    def __init__(self, name):
        self._name = name

class Employee(Person):
    def role(self):
        print(f"{self._name} works as an employee")

class Intern(Person):
    def role(self):
        print(f"{self._name} is an intern")

if __name__ == "__main__":
    emp = Employee("Mr. Garfield")
    emp.role()
    coop = Intern("Tina")
    coop.role()