'''
@author: Solrac
'''

def comparing_numbers_wo_operators(a, b):
    if a ^ b == 0:
        print(a, "and", b, 'are equals')
    else:
        print(a, "and", b, 'are NOT equals')
    
comparing_numbers_wo_operators(5, 5)
comparing_numbers_wo_operators(5, 8)