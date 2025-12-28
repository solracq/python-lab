class Person:
    def __init__(self, name):
        self._name = name

class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self._id = id

    def show_role(self):
        print(f"Employee name {self._name} with id {self._id}")

class Manager(Employee):
    def __init__(self, name, id, directs=0):
        super().__init__(name, id)
        self._directs = directs

    def department(self, dept):
        print(f"{self._name} with id {self._id} and with {self._directs} directs is in the {dept} department")


if __name__ == "__main__":
    mgr = Manager("Gordon Gekko", "123", 45)
    mgr.show_role()
    mgr.department("Investments")