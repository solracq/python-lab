'''
@author: Solrac
'''
from _io import UnsupportedOperation

#raise Exception("wrap core breach")
#raise Exception("wrong letter!")

try:
    dividend = int(input("Give me the dividend: "))
    divisor = int(input("Give me the divisor: "))
    print("Dividing {} and {}...".format(dividend, divisor))
    result = dividend/divisor
except ZeroDivisionError:
    #raise Exception("cannot divide by zero!")
    print("You Cannot Divide by Zero!")
except UnsupportedOperation:
    raise Exception("wrong opeand")
else:
    print("result is: ",result)
    
try:
    number=int(input("give me a number: "))
    print("Dividing the given number by 9 times", number/9)
except:
    #raise Exception("You cannot use operations in strings, convert to integer your number!")
    print("You cannot use operations in strings, convert to integer your number!")
finally:
    print("remember to change your number type to int")
