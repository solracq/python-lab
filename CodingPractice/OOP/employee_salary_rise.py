'''
@author: Solrac
'''
from employee import Employee

print("Employees Salary Rise")

print("Press 'q' at any time to quit: ")

while True:
    first = input('Provide first name: ')
    if first == 'q':
        break
    
    last = input('Provide last name: ')
    if last == 'q':
        break
    
    salary = int(input('Provide salary: '))
    if salary == 'q':
        break
    
    my_employee = Employee(first, last, salary)
    
    my_employee.print_all()
    
    answer = input('provide a fix rise (y/n)? ')
    if answer.lower() == 'y':
        my_employee.give_rise()
    else:
        rise = int(input('Provide a custom rise: '))
        my_employee.set_rise_amount(rise)
    
    my_employee.store_salaries(my_employee.salary)
    my_employee.print_all()
