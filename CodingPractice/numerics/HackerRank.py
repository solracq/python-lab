'''
@author: Solrac
'''
import math
import time
import random
import sys
import itertools
from _socket import dup
#IMPORTING PYTHON DEBUGGER
import pdb



# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total = meal_cost + tip + tax
    #print(math.trunc(total))
    print(round(total,0))
    
meal_cost = 10.25
tip_percent = 17
tax_percent = 5
solve(meal_cost, tip_percent, tax_percent)
print()

# find the minimum number between adjacent elements in a list
def find_min_btw_nums(lista):
    lista.sort()
    list_ = []
    dict_ = dict()
    listb = []
    for i in range(len(lista)-1):
        list_.append((lista[i], lista[i+1])) # I append a tuple to a list
        dict_[list_[i]] = lista[i+1] - lista[i]
    i = 0
    for key, value in sorted(dict_.items()):
        if value == min(dict_.values()):
            p1, p2 = key
            #print("{} {}".format(p1, p2), end=" ")
            listb.append(p1)
            listb.append(p2)
    return listb
        
lista = [3, 4, 5, 2, 1]
print("FIND MINIMUM BTW NUMBERS")
print(lista)
print(find_min_btw_nums(lista))
print()

# verify if an integer is palindrome w/o using string conversion
def isPalindrome(x):
    status = False
    div_list = []
    mod_list = []
    div = 0
    mod = 0
    size = round(math.log10(x)+1) 
    for i in range(size):
        if i == 0:
            div = round(x / 10)
            mod = x % 10
        else:
            mod = div % 10
            div = round(div / 10)
        div_list.append(div)
        mod_list.append(mod)
        
    middle = round(size / 2)
    list1 = []
    list2 = []
    if size % 2 == 0:
        for i in range(middle):
            list1.append(mod_list[i])
        for i in range(middle, size):
            list2.append(mod_list[i])
        if sorted(list1) == sorted(list2):
            return True
    else:
        for i in range(middle):
            list1.append(mod_list[i])
        for i in range(middle+1, size):
            list2.append(mod_list[i])
        print(sorted(list1))
        print(sorted(list1))
        if sorted(list1) == sorted(list2):
            return True

x=12521
# Lenght of an integer
#print(round(math.log10(x)+1))
print(x)
print(isPalindrome(x))
print()

# getting status based on conditions
def conditionals(N):
    if N >= 1 and N <= 100:
        if N % 2 != 0:
            print('Weird')
        else:
            if N >= 2 and N <= 5:
                print('Not Weird')
            elif N >= 6 and N <= 20:
                print('Weird')
            elif N > 20:
                print('Not Weird')
                
N = 18
conditionals(N)
print()

# convert 12 time to 24hrs time
def timeConversion(time_):
    #Validate time
    #print(time.strptime(time_, "%H:%M:%SPM"))
    time_c = time_[:]
    time_c = time_c[:-2]
    try:
        if time.strptime(time_c, "%H:%M:%S"):
            list_12 = ['12', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
            list_A = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
            list_P = ['12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
            lista = list(time_)
    
            splited = time_c.split(':')
            hour = splited[0]
            position = list_12.index(hour)
            if lista[len(lista)-2] == 'A':
                hour = list_A[position]
            else:
                hour = list_P[position]
            splited[0] = hour
    
            return ":".join(splited)
    except ValueError:
        return "Invalid input"
    
time_="07:05:45PM"
print(time_)
print(timeConversion(time_))
print()

# Complete the sockMerchant function below. Find only paired numbers
def sockMerchant(ar):
    list_ = []
    count = 0
    for i in range(len(ar)):
        if i in list_:
            continue
        for j in range(i+1, len(ar)):
            if ar[i] == ar[j]:
                count += 1
                list_.append(j)
                break
    return count
            
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(ar)
print(sockMerchant(ar))
print()

# repete string n times and calculate the number of a's
def repeat_string(s, n):
    i = 0
    if len(s) == 1:
        return n
    else:
        while len(s) < n:
            #for i in range(len(s)):
            #    s = s + s[i]
            #    if len(s) == n:
            #        break
            s = s + s[i]
            i += 1
            if (i == len(s)):
                i = 0
    return s.count('a')

s="ab"
print(s)
print(repeat_string(s, 100))
print()

# show the minimum number to remove from two strings to make them anagram
def making_anagrams(a, b):
    list1 = list(a)
    list2 = list(b)
    set1 = set(list1)
    set2 = set(list2)
    set_= set1.symmetric_difference(set2)
    
    diff1 = len(list1) - len(set1)
    diff2 = len(list2) - len(set2)
    
    if diff1 != 0 and diff2 != 0:
        return len(set_)+diff2+diff1-2
        
    return len(set_)
    
a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
print("MAKING ANAGRAM")
print(making_anagrams(a, b))
print()

#The longest string that can be formed by deleting zero or more characters
def common_child(a, b):
    lista = []
    count = 0
    pos = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if b[j] in lista:
                continue
            if a[i] == b[j] and pos != j:
                lista.append(b[j])
                count += 1
                pos = j
                break
    print(lista)
    return count

a = 'OUDFRMYMAW'
b = 'AWHYFCCMQX'
print('common child:')
print(common_child(a, b))
print()

#Group anagrams
def groupAnagrams(strs):
    main_list = []
    lista = []
    duplicates = []
    for i in range(len(strs)):
        if strs[i] in duplicates:
            continue
        lista = []
        for j in range(i, len(strs)):
            if isAnagram(strs[i], strs[j]):
                lista.append(strs[j])
                duplicates.append(strs[j])
        main_list.append(lista)
    return main_list
        
def isAnagram(s1, s2):
    list1 = list(s1)
    list2 = list(s2)    
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(strs)
print(groupAnagrams(strs))   
print()
    
# REmove vowels from a string
def remove_vowels(s):
    list_s = list(s)
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels_list:
        while vowel in list_s:
            list_s.remove(vowel)  
    return "".join(list_s)
s = "Carlios Quiroz"
print(s)
print(remove_vowels(s), '\n')


def wrap(string, max_width):
    text = ""
    for i in range(1, len(string)+1):
        text = text + string[i-1]
        if i % max_width == 0:
            text = text + "\n"
    return text

string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4
print("Wrapping STIRNG:")
print(string)
print(wrap(string,max_width))
print()

# Find numberes with even number of digitsdef findNumbers(self, nums: List[int]) -> int:
def findNumbers(nums):
    count = 0
    if len(nums) >= 1 and len(nums) <= 500:
        for num in nums:
            #print(num ," ",math.trunc(math.log10(num)+1))
            if math.trunc(math.log10(num)+1) % 2 == 0:
                count += 1
    return count

print("FIND NUMS")
nums = [12, 345, 2, 6, 7896]
print(nums)
print()

#Decompress run-length encoded list
def decompress_list(lista):
    list_ = []
    for i in range(0, len(lista), 2):
        freq = lista[i]
        value = lista[i+1]
        while freq > 0:
            list_.append(value)
            freq -= 1
    return list_

lista = [1, 2, 3, 4]
print("DECOMPRESS LIST")
print(lista)
print(decompress_list(lista))

def solved(s):
    lista = s.split()
    list_ = []
    for element in lista:
        element = element.capitalize()
        list_.append(element)

    return " ".join(list_)

s = "hello world 3g"
print(s)
print(solved(s))

# String compression
def compression_list(lista):
    list_ = []
    for i in range(len(lista)):
        if len(list_) > 0 and lista[i] == lista[i-1]:
            continue
        count = 1
        j = i
        while j < len(lista)-1 and lista[j] == lista[j+1]:
            count += 1
            j += 1
            if len(list_) > 0 and lista[j] == list_[len(list_)-1]:
                continue
            list_.append(lista[j])
        if count >= 2:
            list_.append(str(count))
        if i == len(lista)-1 and lista[i] != lista[i-1]:
            list_.append(list_)
            
    print(list_)
    return len(list_)

def compression_list2(lista):
    dict_ = dict()
    dup = []
    list_ = []
    for character in lista:
        if character in dup:
            continue
        dict_[character] = lista.count(character)
        dup.append(character)
    for key, value in dict_.items():
        if value >= 2:
            list_.append(key)
            list_.append(str(value))
        elif value == 1:
            list_.append(key)
    print(list_)
    return len(list_)
        
lista = ["a","a","b","b","c","c","c","d","a"]
print(lista)
print(compression_list(lista))
print(compression_list2(lista))

def arrayPairSum(nums):
    total = 0
    nums.sort()
    for i in range(0, len(nums), 2):
        lista = []
        lista.append(nums[i])
        lista.append(nums[i+1])
        total += min(nums[i], nums[i+1])
    return total

nums = [1,4,3,2]
print("ARRAY PAIR SUM")
print(sorted(nums))
print(arrayPairSum(nums))
print()

def parenthesisVal(s):
    lista = list(s)
    op = ['{', '[', '(']
    cp = ['}', ']', ')']
    stack = []
    
    for i in range(len(s)):
        if lista[i] in op:
            stack.append(lista[i])
        elif lista[i] in cp:
            pos = cp.index(lista[i])
            if len(stack) > 0 and op[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                return "INVALID"
    if len(stack) == 0:
        return "VALID"
    
s = "{[()[]{}]}"
print(s)
print(parenthesisVal(s)) 
print()

def reverse_chunks(s, chunk):
    list_ = []
    for i in range(0, len(s), chunk):
        list_.append(reverse_string(s[i:i+chunk]))
    return "".join(list_)
        
def reverse_string(s):
    lista = list(s)
    list_ = []
    for i in range(len(lista)-1, -1, -1):
        list_.append(lista[i])
    return "".join(list_)

s = "abcdefghijkl"
print(s)
print(reverse_chunks(s, 3))
print()

# Left Rotation
def left_rotation(lista, n):
    j = 0
    while j <= n:
        list_ = []
        if j == len(lista):
            j = 0
        for i in range(j, len(lista)): 
            list_.append(lista[i])
            if i >= len(lista)-1:
                for k in range(0, len(lista)-len(list_)):
                    list_.append(lista[k])
        j += 1
    return list_

def left_rotation_simple(lista, n):
    return lista[n:] + lista[:n]
    
lista = [1, 2, 3, 4]
print(lista)
print(left_rotation(lista, 3))
print(left_rotation_simple(lista, 3))
print()

# powerful IntegerSizeTests
def powerfulIntegers(x, y, bound):
    output = []
    lista = [i for i in range(bound+1)]
    for i in range(bound):
        for j in range(bound):
            if x**i + y**j in lista:
                output.append(x**i + y**j)
    set_ = set(output)
    list_ = list(set_)
    return list_

x= 40
y= 40
bound = 10
print("POWERFUL INTEGERS")
print(powerfulIntegers(x, y, bound))
print()

# FIND DUPLICATES
def find_dup(s):
    dup = []
    for i in range(len(s)):
        if s[i] in dup:
            continue
        for j in range(i+1, len(s)):
            if s[j] in dup:
                continue
            if s[i] == s[j]:
                dup.append(s[j])
    return dup

def find_dup_count(s):
    dup = []
    for i in range(len(s)):
        if s[i] in dup:
            continue
        if s.count(s[i]) >= 2:
            dup.append(s[i])
    return dup

# FIND NON DUPLICATES
def find_nondup(s):
    ndup = []
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if i == j:
                continue
            if s[i] != s[j]:
                count += 1
        if count == len(s)-1:
            ndup.append(s[i])
    return ndup

def find_nondup_count(s):
    ndup = []
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            ndup.append(s[i])
    return ndup

s = 'DETERMINATION'
print(s)
print(find_dup(s))
print(find_dup_count(s))
print(find_nondup(s))
print(find_nondup_count(s))
print()
print(list(s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)))
print()

########################## PRACTICE #########################################
def linear_search(lista, k):
    found = -1
    for element in lista:
        if element == k:
            found = lista.index(element)
    return found 

def select_sort(lista):
    for i in range(len(lista)-1):
        min = i
        for j in range(i+1, len(lista)):
            if lista[min] > lista[j]:
                min = j
        swap(lista, i, min)
    return lista

def binary_search(lista, k):
    found = -1
    start = 0 
    end = len(lista)
    middle = round((start+end+1) / 2)
    while start < end and found == -1:
        if lista[middle] == k:
            found = middle
        if lista[middle] < k:
            start = middle + 1
        else:
            end = middle - 1
        middle = round((start+end+1) / 2)
    return found
                
def swap(lista, first, second):
    temp = lista[first]
    lista[first] = lista[second]
    lista[second] = temp
    
def sort_insert(lista):
    for i in range(1, len(lista)):
        insert = lista[i]
        move_item = i
        while move_item > 0 and lista[move_item-1] > insert:
            lista[move_item] = lista[move_item-1]
            move_item -= 1
        lista[move_item] = insert
    return lista 

lista = [5, 76, 23, 89, 54, 65, 22, 78, 42, 33, 57, 90, 1]
print(lista)
print(linear_search(lista, 33))
print(select_sort(lista))
print(binary_search(lista, 33))    
lista_ = [5, 76, 23, 89, 54, 65, 22, 78, 42, 33, 57, 90, 1]
print(lista_)
print(sort_insert(lista_))

def subsrings_prep(s):
    lista = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    return lista
s = "abc"
print(s)
print(subsrings_prep(s))
print()

def slicing_ex(s, bulk):
    lista = []
    for i in range(0, len(s), bulk):
        lista.append(reverse_strings(s[i:i+bulk]))
    return "".join(lista)
    
def reverse_strings(s):
    lista = []
    list_ = list(s)
    for i in range(len(list_)-1, -1, -1):
        lista.append(list_[i])
    return "".join(lista)

def rotatetoleft(s, n):
    return s[n:] + s[:n]
    
def rotatetoright(s, n):
    return s[-n:] + s[:-n]
    
print(s)
print(slicing_ex(s, 3))
print(rotatetoleft(s, 3))
print(rotatetoright(s, 3))
print()

def parenthesisval(s):
    op = ['{', '[', '(']
    cp = ['}', ']', ')']
    lista = list(s)
    stack = []
    for i in range(len(lista)):
        if lista[i] in op:
            stack.append(lista[i])
        elif lista[i] in cp:
            pos = cp.index(lista[i])
            if len(stack) > 0 and op[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                return "UNBALANCED"
    if len(stack) == 0:
        return "BALANCED"
    
s = "({[()]{}()[{}]})"
print(s)
print(parenthesisval(s))
print()

def lengthOfLongestSubstring(s):
    lista = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    list_=[]
    for element in lista:
        list_.append(len(remove_duplicates(element)))
    return max(list_)
    
def remove_duplicates(s):
    list_ = []
    lista = list(s)
    for i in range(len(lista)):
        if lista.count(lista[i]) >= 2:
            list_.append(lista[i])
                
    for i in range(len(list_)):
        lista.remove(list_[i])
    return "".join(lista)

s = "pwwkew"
s = "poder total"
print(s)
print('longest substring:', lengthOfLongestSubstring(s))

s = "words and 987"
lista = s.split(" ")
list_ = []
for element in lista:
    if element.isnumeric():
        list_.append(element)
print(list_)
lista = [[-1,0,1],[-1,2,-1],[-1,0,1]]
if lista[0] == lista[2]:
    print('equals')
print()
    
def find_phone_address(s, dict_):
    keys = []
    for key in dict_.keys():
        keys.append(key)
    
    if s in keys:
        print("{}={}".format(s, dict_[s]))
    else:
        print("Not found")
            
dict_ = {'sam': '99912222', 'tom': '11122222', 'harry': '12299933'}
s = "harry"
find_phone_address(s, dict_)

# product of list except self
def productExceptSelf(lista):
    total = 1
    size = len(lista)-1
    list_ = []
    if 0 not in lista:
        while size >= 0:
            total *= lista[size]
            size -= 1
    
        for i in range(1, len(lista)+1):
            list_.append(round(total/i))
            return list_
    else:
        prod = []
        for i in range(len(lista)):
            product = 1
            for j in range(len(lista)):
                if i == j:
                    continue
                product *= lista[j]
            prod.append(product)
        return prod
    
def productExceptSelf2(lista):
    list_ = []
    for i in range(len(lista)):
        prod = 1
        prodl = 1
        prodr = 1
        left = 0
        right = len(lista)-1
        if i == 0:
            while right > 0:
                prod *= lista[right]
                right -= 1
        elif i == len(lista)-1:
            while left < len(lista)-1:
                prod *= lista[left]
                left += 1
        else:
            while i > left and i < right:
                prodl *= left
                left += 1
                prodr *= right
                right -= 1
                prod = prodl * prodr 
        list_.append(prod)

lista = [1, 2, 3, 4]
print(productExceptSelf(lista))

# Separate numbers from a number
def separate_nums(num):
    len_num = math.trunc(math.log10(num)+1)
    lista = []
    for i in range(len_num):
        if i == 0:
            div = math.trunc(num / 10)
            mod = num % 10
        else:
            mod = div % 10
            div = math.trunc(div / 10)
        lista.append(mod)
    return lista

num = 12345
print("Numbers", num)
print("Separate numbers", separate_nums(num))  
print()  

def decToBin(n):
    if n == 0:
        return ""
    else:
        return decToBin(n // 2) + str(n % 2)

n = 4
print(decToBin(n))
print()

# Removing nested lists duplicates
lista = [1, 2, 3] 
lista2 = [1, 2, 3]
lista3 = [3, 2, 1]
list_ = [lista, lista2, lista3]
print(list_)
if list_[0] == list_[1]:
    list_.remove(list_[1])
    print(list_)
print()

# Group anagrams
def group_anagrams(strs):
    output = []
    lista = []
    dup = []
    for i in range(len(strs)):
        if strs[i] in dup:
            continue
        lista = []
        for j in range(i, len(strs)):
            list1 = list(strs[i])
            list2 = list(strs[j])
            if sorted(list1) == sorted(list2):
                lista.append(strs[j])
                dup.append(strs[j])
        output.append(lista)
    return output

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(strs)
print(group_anagrams(strs))
print()

##############
# minimum window sub-string
# Given a string S and a string T, find the minimum window in
# S which will contain all the characters in T
def minwindowsubs(s, t):
    pos = []
    res = []
    count = 0
    for j in range(len(t)):
        if t[j] in s:
            count += 1
    if count == len(t):
        for i in range(len(s)):
            if s[i] in t:
                pos.append(i)
                if len(pos) == len(t):
                    res.append(s[pos[0]:pos[len(pos)-1]+1])
                    pos.clear()
    dict_ = dict()            
    for i in range(len(res)):
        dict_[len(res[i])] = res[i]
    
    return dict_[min(dict_.keys())]

s = "ADOBECODEBANC"
t = "ABC"
print("MINIMUM WINDOW")
print(s)
print(t)
print(minwindowsubs(s, t))

def palindorme2(s):
    lista_alpha = []
    for i in range(len(s)):
        if s[i].isalpha() == True:
            lista_alpha.append(s[i].lower())
    s_alpha = "".join(lista_alpha)
    s_alpha_rev = s_alpha[::-1]
    if s_alpha == s_alpha_rev:
        return True
    else:
        return False

s = "A man, a plan, a canal: Panama"
print(palindorme2(s))

print(math.ceil(2.5))

## ORDER DICTIONARY BY VALUES
def topKFrequent(words, k):
    dict_ = dict()
    for i in range(len(words)):
        dict_[words[i]] = words.count(words[i]) 

    dict_oredred_by_values = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
    print(dict_oredred_by_values)
    lista = []
    count = 0
    
    for element in dict_oredred_by_values:
        lista.append(element)
        count += 1
        if count == k:
            break
    return lista

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(words)
print(topKFrequent(words, k))

# another example of ordering dictionary through values
list_ = []
dict_ = {'a': 5, 'd':7, 'b': 9, 'c': 2}
for key, value in sorted(dict_.items(), key=lambda x: x[1], reverse=True):
    print(key, value)
    
list_ = sorted(dict_.items(), key=lambda x: x[1])
lista = []
for element in list_:
    lista.append(list(element))
print(lista)
print()

# substrings of a string
def substring_practice(s):
    lista = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    return lista
s = "BANANA"
print(substring_practice(s))
print()

# combinations : subsets
def subsets(s, n):
    lista = list(s)
    return list(itertools.combinations(lista, n))
print("SUBSETS")
print(s)
print(subsets(s, 2))

# more on substrings
def reverse_substrings(s, chunk):
    lista = []
    list_ = list(s)
    for i in range(0, len(s), chunk):
        lista.append(reverse_(s[i:i+chunk]))
    return "".join(lista)
    
def reverse_(s):
    lista = list(s)
    list_ = []
    for i in range(len(lista)-1, -1, -1):
        list_.append(lista[i])
    return "".join(list_)

s = "abcdefghijkl"
print(s)
print(reverse_substrings(s, 4))
print()

# reverse string
print('original', s)
print('reversed', s[::-1])
print()

# rotation practice
def rotate_left_(s, n):
    return s[n:] + s[:n]

def rotate_right_(s, n):
    return s[-n:] + s[:-n]
print("rotate left: ", rotate_left_(s, 3))
print("rotate right: ", rotate_right_(s, 3))
print()

# Create a random matrix
def generate_matrix(n):
    matrix = [[random.randint(10, 90) for i in range(n)] for j in range(n)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j % n == 0:
                print()
            else:
                print(matrix[i][j], end=' ')
generate_matrix(6)
print("\n")

# numreical conversions
def dec_bin_rec(num):
    if num == 0:
        return ""
    else:
        return dec_bin_rec(num // 2) + str(num % 2)
num = 7
print(num, "to binary", dec_bin_rec(num))
print()

def bin_dec_(bnum):
    lista = list(bnum)
    lista.reverse()
    result = 0
    for i in range(len(lista)):
        result += int(lista[i]) * 2 ** i
    return result
bnum = '10011'
print(bnum, "to decimal", bin_dec_(bnum))
print()

def fibonacci_(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_(n-1) + fibonacci_(n-2)
    
print(fibonacci_(8))
print()

def prime_():
    for i in range(1, 101):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
                else:
                    print(i, end=' ')
                    break
    print()
    #raise Exception("Testing exception")
    try:
        print(2/0)
    except Exception as e:
        print(str(e))
        
print(prime_())
print()

import traceback

try:
    raise Exception('This is the error message')
except:
    errorFile = open('../error_handling/errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')

