class Employee:
    count = 0
    objs = []

    def __init__(self, name):
        self.__name = name
        Employee.count += 1
        Employee.objs.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def salary(self):
        raise NotImplementedError()

    def bye_emplyee(self):
        Employee.count -= 1
        Employee.objs.remove(self)

    @classmethod
    def remove_employee(cls, obj):
        if obj in Employee.objs:
            Employee.objs.remove(obj)

    def __str__(self):
        return f"Monthly Salary of Employee {Employee._to_title(self.__name)}: ${self.salary()}"

    @staticmethod
    def _to_title(string: str) -> str:
        return string.title()

    @classmethod
    def number_empoloyees(cls):
        return cls.count

    @classmethod
    def employee_objects(cls):
        return cls.objs

    def __repr__(self):
        return f"Employee({self.__name}, {self.salary()})"

class Permanent(Employee):
    def __init__(self, name, msalary):
        super().__init__(name)
        self.msalary = msalary

    def salary(self):
        return self.msalary

class Contract(Employee):
    def __init__(self, name, hsalary):
        super().__init__(name)
        self.hsalary = hsalary

    def salary(self):
        return (self.hsalary * 8) * 20

if __name__ == "__main__":
    mark = Permanent("mark", 1000)
    print(mark)
    jena = Permanent("jena", 5000)
    print(jena)
    daniel = Contract("daniel", 40)
    print(daniel)
    print(f"Number of employees: {Employee.number_empoloyees()} employees")
    print(f"Objects in employees: {Employee.employee_objects()}")
    mark.name = "john"
    print(mark)
    print(Employee.employee_objects())
    mark.bye_emplyee()
    print(Employee.number_empoloyees())
    print(Employee.employee_objects())
    Employee.remove_employee(daniel)
    print(Employee.employee_objects())

