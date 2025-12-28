class Employee:
    _count = 0
    _registry = []

    def __init__(self, name):
        self._name = name
        Employee._count += 1
        if self not in Employee._registry:
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
        return f"Employee({self.name!r})"

    @classmethod
    def remove(cls, obj):
        Employee._count -= 1
        if obj in cls._registry:
            cls._registry.remove(obj)

    @staticmethod
    def round_salary(salary):
        return round(salary)

class Permanent(Employee):
    def __init__(self, name, yr_salary):
        super().__init__(name)
        self._salary = yr_salary

    @property
    def salary(self):
        return self._salary / 12

    @salary.setter
    def salary(self, salary):
        self._salary = salary

class Contract(Employee):
    def __init__(self, name, hour_salary):
        super().__init__(name)
        self._salary = hour_salary

    @property
    def salary(self):
        return self._salary * 8 * 25

    @salary.setter
    def salary(self, salary):
        self._salary = salary

import pytest

@pytest.fixture
def employee_count():
    Employee._count = 0

    yield Employee._count

    Employee._count = 0

@pytest.fixture
def employee_registry():
    Employee._registry = []

    yield Employee._registry

    Employee._registry = []

def test_salaries(employee_count, employee_registry):
    ana = Permanent("Ana", 100000.9)
    assert Employee.round_salary(ana.salary) == 8333
    bob = Permanent("Bob", 90000)
    assert Employee.round_salary(bob.salary) == 7500
    daniel = Contract("Daniel", 300)
    assert Employee.round_salary(daniel.salary) == 60000
    Employee.remove(bob)
    assert Employee._count == 2
    assert Employee._registry == [Employee('Ana'), Employee('Daniel')]