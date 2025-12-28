'''
@author: Solrac
'''
import math


def palindrome_verification(s):
    list_only_alpha = []
    for i in range(len(s)):
        if s[i].isalpha() == True:
            list_only_alpha.append(s[i])
    s_only_alpha = "".join(list_only_alpha)
    s_only_alpha = s_only_alpha.lower()        
    
    # Reverse string
    s_rev = s_only_alpha[::-1]
    print(s_only_alpha)
    print(s_rev)
    if s_only_alpha == s_rev:
        return True
    else:
        return False
    
s = "A man, a plan, a canal: Panama"
print(s)
print(palindrome_verification(s))

def palindrome_ver_simple(s):
    pointer = 0
    end = len(s)-1
    onlyalpha = []
    while pointer <= end:
        if s[pointer].isalnum():
            onlyalpha.append(s[pointer])
        pointer += 1
    new_s = "".join(onlyalpha)
    new_s_rev = new_s[::-1]
    if new_s.lower() == new_s_rev.lower():
        return True
    else:
        return False
    
print(palindrome_ver_simple(s))

def numerical_palindrome(num):
    num_size = math.trunc((math.log10(num) + 1))
    print(num_size)
    if num_size == 5:
        lista = []
        res = 1
        for i in range(1, num_size + 1):
            dig = num % 10
            lista.append(dig)
            res = math.trunc(num / 10)
            num = res
    reversed_list = [lista[i] for i in range(num_size - 1, -1, -1)]
    if lista == reversed_list:
        print(f"{lista} == {reversed_list}")
        print("Palindrome!")
    else:
        print("Not a palindrome")

num = 12321
numerical_palindrome(num)