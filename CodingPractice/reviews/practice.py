'''
@author: Solrac
'''
import json


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if i != len(string)-1:
            if string[i] == sub_string[0]:
                c = 0
                for j in range(len(sub_string)):
                    if (i+j) < len(string)-1:
                        if string[i+j] == sub_string[j]:
                            c += 1
                if c == len(sub_string):
                    count += 1
    return count
# Execution
string = "TestCaseTestCase"
sub_string = "CaseT"
count = count_substring(string, sub_string)
print(count)

def parenthesis_balancing(s):
    p = list(s)
    op = ['{', '[', '(']
    cp = ['}', ']', ')']
    stack = []
    for i in range(len(p)):
        if p[i] in op:
            stack.append(p[i])
        elif p[i] in cp:
            location = cp.index(p[i])
            if len(stack) > 0 and op[location] == stack[len(stack)-1]:
                stack.pop()
            else:
                return "UNBALANCED"
    if len(stack) == 0:
        return "BALANCED"
# Execution
s = "{[()[]{}]}"
print(s)
print(parenthesis_balancing(s))
    
def reverse_chunks(s, chunk):
    #s[i:chunk]
    list_= []
    for i in range(0, len(s), chunk):
        list_.append(reverse(s[i:chunk+i]))
    return "".join(list_)

def reverse(s):
    lista = list(s)
    listarv = []
    for i in range(len(lista)-1, -1, -1):
        listarv.append(lista[i])
    return "".join(listarv)
# Execution
s = "abcdefghijkl"
print(s)
print(reverse_chunks(s, 3))

def find_sum_two_nums(arr:list, x:int):
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == x:
                return (i, j)

# Execution
arr = [50, 20, 10, 80, 75, 35]
x = 60
print(arr)
print(find_sum_two_nums(arr, x))
print()

def find_sum_two_nums_two_point_approach(arr:list, x:int):
    s = 0
    e = len(arr) - 1
    arr.sort()
    while s < e:
        if arr[s] + arr[e] == x:
            return (s, e)
        elif arr[s] + arr[e] < x:
            s += 1
        else:
            e -= 1
    return False

# Execution
x = 70
arr = [50, 20, 10, 80, 75, 35]
arr.sort()
print(arr)
print(f"Two Point Approach: {find_sum_two_nums_two_point_approach(arr, x)}\n")

