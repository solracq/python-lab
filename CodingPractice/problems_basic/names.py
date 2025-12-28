'''
@author: Solrac
'''
from CodingPractice.problems_basic.name_function import get_formatted_name

print("Enter a 'q' to leave the program.")

while True:
    first = input('\nGive me a first name: ')
    if first == 'q':
        break
    
    last = input('\nGive me a last name: ')
    if last == 'q':
        break
    
    middle = input('\nIf you want to provide middle name type it, otherwise press ENTER: ')
    
    formatted_name = get_formatted_name(first, last, middle)
    print(formatted_name)