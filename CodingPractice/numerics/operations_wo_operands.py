'''
@author: Solrac
'''
from _operator import neg

def add(a, b):
    if b == 0:
        return a
    else:
        return add(a^b, (a&b) << 1)
    
def substraction(a, b):
    if b == 0:
        return a
    else:
        return substraction(a ^ b, (~a & b) << 1)

def multiplication(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        abs_a = abs(a)
        abs_b = abs(b)
        total = 0
        if abs_a > abs_b:
            for i in range(abs_b):
                total +=  abs_a
        else:
            for i in range(abs_a):
                total += abs_b
        
        if a < 0 or b < 0:
            return neg(total)
        else:
            return total

def division(a, b):
    result = 0
    if a > b and b != 0:
        resta = a
        while resta != 0:
            resta -= b
            if resta >= 0:
                result += 1
            else:
                break
    return result

def mod_(a, b):
    return a - b * (a // b)

if __name__ == '__main__':
    a = 51
    b = 23
    print('sum: ', add(a,b))
    print('substraction: ', substraction(a, b))
    print('multiplication: ', multiplication(a, b))
    print('module: ', mod_(a, b))
    print('division: ', division(8, 2))
    