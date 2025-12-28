class Person:
    def __init__(self, name):
        self.name = name

class Job:
    def __init__(self, salary):
        self.salary = salary

class Employee(Person, Job):
    def __init__(self, name, salary, loquesea):
        Person.__init__(self, name)
        Job.__init__(self, salary)
        self.loquesea = loquesea

    def details(self):
        print(self.name, "earns",self.salary)


if __name__ == "__main__":
    emp = Employee("Jennifer", 50000, "loquesea")
    emp.details()