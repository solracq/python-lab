'''
@author: Solrac
'''

class Employee():
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.salaries = []
    
    def give_rise(self):
        self.salary += 5000
        
    def set_rise_amount(self, rise):
        self.salary += rise
        
    def store_salaries(self, salary):
        self.salaries.append(self.salary)
    
    def print_all(self):
        for salary_ in self.salaries:
            print(self.first.title(), self.last.title(), salary_)