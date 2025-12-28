'''
@author: Solrac
'''

import time
import itertools
from random import randint
from itertools import combinations

start = time.time()

def conversions(s, lista, tupla, seto, dictionary):
    print('list', list(s))
    s2 = "".join(list(s))
    print('string:', s2)
    lista2 = s.split()
    print('list:',lista2)
    print('tuple',tuple(lista))
    print('list',list(tupla))
    print('list',list(seto))
    print('set',set(lista))
    dict_ = {'a': s, 'b': lista, 'c': tupla, 'd':seto, 'e':dictionary}
    print('dictionary', dict_)

def strings_manipulation(s):
    print(s.upper())
    print(s.lower())
    print(s.swapcase())
    print(s.casefold())
    print("counts of e =", s.count("e"))
    print("find first s =", s.find('s'))
    print("find last s =", s.rfind('s'))
    print("index of first r =", s.index('r'))
    print("index of last r =", s.rindex('r'))
    print("min", min(s))
    print("min", max(s))
    
    if s.startswith("N"):
        print("starts with", s[0])
    if s.endswith("e"):
        print("ends with", s[len(s)-1])
    s1= "abcd"
    if s1.isalpha():
        print(s1, "is alpha")
    s3 = "abcd123"
    if s3.isalnum():
        print(s3, "is alphanumeric")
    s4 = s1+s3
    print(s3.join(s4))
    num = str(987)
    print(s1.join(num))
    print(s)
    print(s.replace('a', 'A', 3))
    
    if "duper" in s:
        print("superduper")
        
def references(list_num):
    print("REFERENCES")
    list1 = list_num
    list2 = list_num[:]
    list3 = list_num.copy()
    print(list_num)
    del list_num[1:3]
    print(list_num.pop(0))
    print(list1)
    print(list2)
    print(list3)
    
def list_manipulation(list_num, list_words):
    lista = list_num[:]
    lista.append(list_words)
    print(lista)
    lista2 = list_num + list_words
    print(lista2)
    lista2.append("kiwi")
    print(lista2)
    print(len(lista2))
    print(lista2.count("kiwi"))
    lista2.extend("test")
    lista2.append("Test")
    print(lista2)
    print(lista2.index("strawberry"))
    list_words.sort(reverse = True)
    print(list_words)
    list_words.reverse()
    print(list_words)
    print(sorted(list_num))
    
    if "kiwi" in list_words:
        print("Gooood!")
        
    for fruit in list_words:
        print(fruit)
    
    # finding min and max
    list12 = [5, 3, 7, 9, 3, 8, 2]
    min = list12[0]
    for i in range(len(list12)-1):
        if min > list12[i+1]:
            min = list12[i+1]
    print("min", min)
    print()
    max = list12[0]
    for i in range(len(list12)-1):
        if max < list12[i+1]:
            max = list12[i+1]
    print("max", max)
    print()
    
def linearsearch(lista, searchkey):
    localization = -1
    for element in lista:
        if element == searchkey:
            localization = lista.index(element)
    return localization

def binarysearch(lista, searchkey):
    lista.sort()
    localization = -1
    start = 0
    end = len(lista)
    middle = int((start + end + 1) / 2)
    
    while (start < end) or (localization == -1):
        if lista[middle] == searchkey:
            localization = middle
        if lista[middle] < searchkey:
            start = middle + 1
        else:
            end = middle - 1
        middle = int((start + end + 1) / 2)
    return localization

def selectionsort(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i+1, len(lista)):
            if lista[min] > lista[j]:
                min = j
        swap(lista, i, min)

def swap(lista, first, second):
    temp = lista[first]
    lista[first] = lista[second]
    lista[second] = temp

def insertionsort(lista):
    for i in range(len(lista)):
        insert = lista[i]
        move_item = i
        while (move_item > 0) and (lista[move_item-1] > insert):
            lista[move_item] = lista[move_item-1]
            move_item -= 1
        lista[move_item] = insert
        
def findduplicate(lista):
    duplicates = []
    nondup = list()
    for i in range(len(lista)):
        if i in duplicates:
            continue
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                duplicates.append(lista[i])
                break
        if lista[i] not in duplicates:
            nondup.append(lista[i])
    print("duplicates", duplicates)
    print("nonduplicates", nondup)

def combinaciones(list_, n):
    return list(combinations(list_, n))
    
# Driver function
if __name__ == "__main__":
    s = "Naomi and Carlitos are very super duper cute" 
    
    list_num = [randint(10, 90) for i in range(10)]
    list_words = ['kiwi', 'banana', 'strawberry', 'orange', 'blueberry', 'mango', 'pear', 'apple', 'rasperry', 'melon', 'papaya', 'watermelon']
    
    tuple_months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    
    set_colors = {'blue', 'red', 'green', 'purple', 'orange', 'black', 'white', 'grey', 'yellow', 'magenta', 'pink', 'brown'}

    dictionary = {
                  'solrac': {
                             'name': 'CaloBeto',
                             'number': list_num[3],
                             'month': tuple_months[7],
                             'fruit': list_words[0],
                             'color': 'green',
                             'likes': 'watch movies',
                             'hobbies': 'FIFA19',
                             'movies': 'Ronin',
                           },
                  'carlitos': {
                               'name': 'CarloEddy',
                               'number': list_num[5],
                               'month': tuple_months[11],
                               'fruit': list_words[4],
                               'color': 'blue',
                               'likes': 'cars',
                               'hobbies': 'soccer',
                               'movies': 'Aladdn',
                               },
                  'nquiroz': {
                              'name': 'Naomi',
                              'number': list_num[2],
                              'month': tuple_months[2],
                              'fruit': list_words[4],
                              'color': 'pink',
                              'likes': 'purses',
                              'hobbies': 'play in water',
                              'movies': 'Princess',
                              },
                  'yuyis': {
                            'name': 'Yu',
                            'number': list_num[8],
                            'month': tuple_months[9],
                            'fruit': list_words[7],
                            'color': 'purple',
                            'likes': 'shopping',
                            'hobbies': 'cooking',
                            'movies': 'As good as it gets',
                            },
                  }
    
    print("string:", s)
    print("lista num:", list_num)   
    print("lista words:", list_words)
    print("tuple months:", tuple_months)
    print("set colors:", set_colors)
    print()
    for key, value in dictionary.items():
        print("{} : ".format(key))
        for vkey, vvalue in value.items():
            print("\t{} : {}".format(vkey, vvalue))
    print()
    conversions(s, list_words, tuple_months, set_colors, dictionary)
    print()
    strings_manipulation(s)
    print()
    references(list_num)
    print()
    list_manipulation(list_num, list_words)
    print()
    
    lista = [5, 3, 7, 9, 3, 8, 2]
    print(lista)
    print("found number 8 at index", linearsearch(lista, 8))
    print("found number 8 at index", binarysearch(lista, 8))
    selectionsort(lista)
    print(lista)
    lista = [80, 35, 75, 11, 7, 38, 34, 45, 35, 67, 17, 14, 83, 94, 88, 56, 2, 10, 77, 51, 93, 30, 5, 52, 70, 1, 99, 84, 22, 11, 4, 76, 69, 45, 2]
    print(lista)
    insertionsort(lista)
    print(lista)
    print()
    findduplicate(lista)
    print()
    list_ = ['A', "B", 'C', 'D']
    print(combinaciones(list_, 2))
    print('\n')
    
def password_validation(s):
    if atleast_one_uppercase(s) and min_chars(s, 8) and atleast_one_number(s) and atleast_one_symbol(s):
        return True
    else:
        return False
    
def min_chars(s, min):
    if len(s) >= min:
        return True
    else:
        return False

def atleast_one_uppercase(s):
    count = 0
    for i in range(len(s)):
        if s[i] == s[i].upper():
            count += 1
    if count >= 1 and count <= len(s)-2:
        return True
    else:
        return False

def atleast_one_number(s):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    chars_ = list(s)
    for i in range(len(nums)):
        if nums[i] in chars_:
            return True
    return False
        
def atleast_one_symbol(s):
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '_', '=', '+', '-', '/', '?', '.', '~']
    chars_ = list(s)
    for i in range(len(symbols)):
        if symbols[i] in chars_:
            return True
    return False

s = 'Test@rrosa3'
print("Is {} a valid password? {}".format(s, password_validation(s)))