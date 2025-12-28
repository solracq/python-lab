class Employee:
    _count = 0
    _registry = []  # class level list all instances

    def __init__(self, name):
        self._name = name
        Employee._count += 1
        Employee._registry.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @classmethod
    def head_count_size(cls):
        return Employee._count

    @classmethod
    def all(cls):
        return list(cls._registry)

    def __repr__(self):
        return f"Employee({self._name!r})"

    @classmethod
    def remove(cls, obj):
        if obj in cls._registry:
            cls._registry.remove(obj)

    @staticmethod
    def round_salary(salary):
        return round(salary)


class Permanent(Employee):
    def __init__(self, name, yr_salary):
        super().__init__(name)
        self.yr_salary = yr_salary

    @property
    def salary(self):
        return self.yr_salary / 12


class Contract(Employee):
    def __init__(self, name, hour_salary):
        super().__init__(name)
        self.hour_salary = hour_salary

    @property
    def salary(self):
        return self.hour_salary * 8 * 25


if __name__ == "__main__":
    ana = Permanent("Ana", 100000)
    print(Employee.round_salary(ana.salary))
    bob = Permanent("Bob", 90000)
    print(Employee.round_salary(bob.salary))
    daniel = Contract("Daniel", 300)
    print(Employee.round_salary(daniel.salary))
    print(Employee.head_count_size())
    print(Employee.all())
    Employee.remove(bob)
    print(Employee.all())