'''
@author: Solrac
'''
import math
import random

#Generate random numbers
def random_gen():
    rand = random.randint(0, 101)
    rand_range = random.randrange(0, 10, 2)
    return rand, rand_range

def get_sign(a, b):
    sign = ""
    if a < 0 and b < 0:
        sign = "+"
    elif a < 0:
        sign = "-"
    elif b < 0:
        sign = "-"
    return sign

#Multiplication w/o operand
def multiply(a:int, b:int):
    sign = get_sign(a, b)
    a = abs(a)
    b = abs(b)
    prod = 0
    for i in range(b):
        prod += a
    return f"{sign}{prod}"

#Division w/o operand
def divide(a:int, b:int):
    count = 0
    sign = get_sign(a, b)
    a = abs(a)
    b = abs(b)
    res = a
    if b <= 0:
        return "Division cannot be infinite!"
    if a < b:
        return "This program cannot process decimal results"
    while res > 0:
        res = a - b
        a = res
        count += 1
    return f"{sign}{count}"

#mod w/o operand
def mod(a:int, b:int):
    a = abs(a)
    b = abs(b)
    if b <= 0:
        return "Division cannot be infinite"
    if a < b:
        return "This program cannot process decimal results"
    return a - (a//b * b)

#sum w/o operand
def suma(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return suma(a ^ b, (a & b) << 1)

#substraction w/o operand
def substract(a:int, b:int):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return substract(a ^ b, (~a & b) << 1)

#factorials
def factorial(num: int):
    fact = 1
    for i in range(num):
        fact *= (num - i)
    return fact

def fact(num: int):
    if num <= 1:
        return 1
    else:
        return num * fact(num-1)

#fibonacci
def fibo(num:int):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num - 2) + fibo(num - 1)

#Matrix
def gen_matrix(num: int):
    matrix = []
    for i in range(num):
        row = []
        for j in range(num):
            row.append(random.randint(1, 100))
        matrix.append(row)
    return matrix

def gen_matrix_simple(num:int):
    return [[random.randint(1,90) for column in range(num)] for row in range(num)]

def print_matrix(matrix:list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

if __name__ == "__main__":
    # Random #s
    print(random_gen())
    # Multiply #s
    a = 2
    b = -3
    print(f"{a} X {b} = {multiply(a, b)}")
    # Divide #s
    a = 25
    b = 5
    print(f"{a} X {b} = {divide(a, b)}")
    # Mod #s
    a = 7
    b = 3
    print(f"{a} % {b} = {mod(a, b)}")
    # suma
    a = 3
    b = 5
    print(f"{a} + {b} = {suma(a,b)}")
    # substract
    a = 5
    b = 3
    print(f"{a} - {b} = {substract(a, b)}")
    # factorial
    num = 5
    print(f"Factorial of {num} is {factorial(num)}")
    print(f"Factorial of {num} is {fact(num)}")
    num = 20
    print(f"Fibonacci of {num} is {fibo(num)}")
    # Matrix
    matrix = gen_matrix(2)
    print(matrix)
    print_matrix(matrix)
    # compare
    a = 2
    b = 5
    if a^b == 0:
        print(f"{a} == {b}")
    else:
        print(f"{a} != {b}")
    matrix = gen_matrix_simple(5)
    print_matrix(matrix)
