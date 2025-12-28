'''
@author: Solrac
'''
def fib_norecursion(num):
    print("Calculating the Fibonacci sequences of {0} iterations".format(num))
    number = int(num)
    fibonacci = 0
    unit=0
    dec=1
    i=0
    while i < number-1:
        fibonacci = unit + dec
        unit = dec
        dec = fibonacci
        i = i + 1 
    return fibonacci
    
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    print(fib_norecursion(20))
    print(fibonacci(20))