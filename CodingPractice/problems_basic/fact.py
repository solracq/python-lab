'''
@author: Solrac
'''

def fact_no_recursive(num):
    number = float(num)
    factorial = 1
    while number>0:
        factorial = factorial * number
        number = number -1
    return factorial

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print(fact_no_recursive(20))
    print(factorial(20))