'''
@author: Solrac
'''
from employee import Employee
import unittest

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee("pu", "ug", 3000)
        
    def test_rise_default(self):
        self.my_employee.give_rise()
        
        self.assertEqual(self.my_employee.salary, 8000)
        
    def test_rise_customized(self):
        self.my_employee.set_rise_amount(1000)
        
        self.assertEqual(self.my_employee.salary, 4000)
        
    def test_rise_salaries(self):
        self.salaries = [1000, 2000, 3000]
        for salary in self.salaries:
            self.my_employee.store_salaries(salary)
            self.my_employee.salary = salary
            self.assertEqual(self.my_employee.salary, salary)
        
unittest.main()