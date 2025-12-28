'''
@author: Solrac
'''
from random import randint
from itertools import groupby
import json
from _operator import neg
import math


def getname():
    name = input("what is your name? ")
    return "Your name is "+ name

def getname2():
    name = input("what is your name? ")
    return "Your name is {}".format(name)

def suma(a, b):
    if b == 0:
        return a
    else:
        return suma(a^b, (a&b) << 1)
    
def compare(a, b):
    if a ^ b == 0:
        return '{} and {} are equals\n'.format(a, b)
    else:
        return '{} and {} are NOT equals\n'.format(a, b)
    
def resta(a, b):
    if b == 0:
        return a
    else:
        return resta(a ^ b, (~a & b) << 1)
    
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
    dividend = a
    divisor = b
    if divisor == 0:
        raise Exception("Division by zero not allowed!")
    if dividend == 0:
        return 0
    else:
        if dividend > divisor:
            count = 1
            res = dividend - divisor
            while res != 0:
                res = res - divisor
                count += 1
    return count
    
def mod_(a, b):
    dividend = a
    divisor = b
    try:
        result = dividend // divisor
    except ZeroDivisionError:
        print("Division by zero not allowed!")
    return dividend - (divisor * result)
    
def lists(lista):
    # find duplicates and non-duplicates
    dups = []
    nondups = []
    for i in range(len(lista)):
        if lista.count(lista[i]) >= 2:
            dups.append(lista[i])
        else:
            nondups.append(lista[i])
    print("duplicates:", dups)
    print("non duplicates:", nondups)
    
    dups = []
    nondups = list()
    for element in lista:
        if lista.count(element) >= 2:
            dups.append(element)
        else:
            nondups.append(element)
    print("duplicates:", dups)
    print("non duplicates:", nondups)
    
    # find duplcates
    listas = sorted(lista)
    s = 0
    e = len(listas) - 1
    dup = list()
    nondup = []
    while s <= e:
        temp = listas[s]
        s += 1
        if temp == listas[s]:
            dup.append(listas[s])
        else:
            if temp not in nondup:
                nondup.append(temp)
            if listas[s] not in nondup:
                nondup.append(listas[s])
        s += 1
    print("duplicates through sorted list:", dup)
    print("non duplicates through sorted list:", nondup)
    
    sorted_list = sorted(lista)
    dups.clear()
    nondups.clear()
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] == sorted_list[i+1]:
            dups.append(sorted_list[i+1])
        else:
            if i == 0:
                nondups.append(sorted_list[i])
            else:
                nondups.append(sorted_list[i+1])
    print("duplicates2:", dups)
    print("non duplicates2:", nondups)
    
    # generate and print matrix
    matrix0 = [[randint(10,90) for i in range(8)] for j in range(8)]
    for i in range(len(matrix0)):
        for j in range(len(matrix0[i])):
            print(matrix0[i][j], end=' ')
        print()
    
    matrix = [[randint(10, 90) for i in range(4)] for j in range(4)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    
def json_imports_exports(lista):
    dictionary = {'character1': 'Han-Solo', 'character2': 'Chewbaca', 'character3': 'Luke'}
    string_json = json.dumps(lista, indent = 4)
    dict_json = json.dumps(dictionary, indent = 4)
    json_file = open("../json_management/json_config.json", 'w')
    json_file.write(dict_json)
    json_file.write(string_json)
    json_file.close()
    
    json_string = json.dumps(dictionary, indent = 4, sort_keys = True)
    #method 1
    json_file0 = open("newjsonfile_m1.json", 'w')
    json_file0.write(json_string)
    json_file0.close()
    #method 2
    with open("newjsonfile_m2.json", 'w') as jsonobject:
        jsonobject.write(json_string)
    
    with open("../json_management/json_config.json") as fileobject:
        aquiredData = fileobject.readlines()
    dictionary_from_file = json.loads(dict_json) 
    print(dictionary_from_file)
    
    json_string2 = json.dumps(dictionary, indent = 4)
    with open("testarrosa.json", 'w') as fileobject:
        fileobject.write(json_string2)
        
    with open("newjsonfile_m2.json") as json_obj:
        dict_ = json.load(json_obj)
    print('Parsing json file to dictionary: ', dict_)
    
def printSpiralMatrix(size):
    print('\nMatrix to be printed:')
    matrix = [[randint(10, 90) for i in range(size)] for j in range(size)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    
    start_row = 0
    start_column = 0
    end_row = len(matrix)
    end_column = len(matrix)
    lista = list()
    while (start_row < end_row) and (start_column < end_column):
        for i in range(start_column, end_column):
            lista.append(matrix[start_row][i])
            
        start_row += 1
        
        for i in range(start_row, end_row):
            lista.append(matrix[i][end_column - 1])
            
        end_column -= 1
        
        if start_row < end_row:
            for i in range(end_column - 1, start_column - 1, -1):
                lista.append(matrix[end_row - 1][i])
                
            end_row -= 1
            
        if start_column < end_column:
            for i in range(end_row - 1, start_row - 1, -1):
                lista.append(matrix[i][start_column])
                
            start_column += 1
            
    print('Printed Spiral Matrix:', lista)
    print()
    
def find_substring(string, sub_string):
    counter = 0
    while sub_string in string:
        counter += 1
        temp_string = string.replace(sub_string, "", 1)
        string = temp_string[:]
    return "Number of {} substrings in {} string is {}".format(sub_string, string, counter)

def parenthesis_validation(sp):
    p = list(sp)
    stack = []
    op = ['{', '[', '(']
    cp = ['}', ']', ')']
    for i in range(len(p)):
        if p[i] in op:
            stack.append(p[i])
        elif p[i] in cp:
            location = cp.index(p[i])
            if len(stack) > 0 and stack[len(stack)-1] == op[location]:
                stack.pop()
            else:
                return 'UNBALANCED'
    if len(stack) == 0:
        return 'BALANCED'
    
def reverse_chuncks(s, chunck):
    lista = []
    for i in range(0, len(s), chunck):
        lista.append(s[i:i+chunck][::-1])
    return "".join(lista)

def primeNums(n):
    if n > 0:
        for i in range(1, n+1):
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                    else:
                        print(i, end = ', ')
                        break
    print()
    
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
    
def fibonacci_series(n):
    if n > 0:
        for i in range(1, n+1):
            print(fibonacci(i), end = ', ')
    print()
    
def conversionDecBin(num):
    if num <= 0:
        return ""
    else:
        return conversionDecBin(num // 2) + str(num % 2)
    
def conversionBinDec(s):
    s = s[::-1]
    result = 0
    for i in range(len(s)):
        result += int(s[i]) * (2**i)
    return result
    
def find_sum_2sums(lista, x):
    found = -1
    lista_sorted = sorted(lista)
    print('\nsorted list', lista_sorted)
    print("looking for", x)
    s = 0
    e = len(lista_sorted) - 1
    while s < e:
        if lista_sorted[s] + lista_sorted[e] == x:
            return [s, e]
        if lista_sorted[s] + lista_sorted[e] < x:
            s += 1
        else:
            e -= 1
    return found

def find2sum(lista, x):
    listaS = sorted(lista)
    s = 0
    e = len(listaS) - 1
    not_found = -1
    while s < e:
        if listaS[s] + listaS[e] == x:
            return [s, e]
        if listaS[s] + listaS[e] < x:
            s += 1
        else:
            e -= 1
    return not_found

def find_sum_3nums(lista, x):
    notfound = -1
    lista.sort()
    for i in range(len(lista)):
        s = i + 1
        e = len(lista) - 1
        while i < e: 
            if lista[s] + lista[e] + lista[i] == x:
                return [lista[s], lista[e], lista[i]]
            elif lista[s] + lista[e] + lista[i] < x:
                s += 1
            else:
                e -=1
    return notfound
                
def find_sum_4nums(lista, x):
    notfound = -1
    lista.sort()
    for i in range(len(lista)-1):
        for j in range(len(lista)):
            s = j + 1
            e = len(lista) - 1
            while s < e:
                if lista[s] + lista[e] + lista[i] + lista[j] == x:
                    return [lista[s], lista[e], lista[i], lista[j]]
                elif lista[s] + lista[e] + lista[i] + lista[j] < x:
                    s += 1
                else:
                    e -= 1
    return notfound

def find_closest_sum(lista, x):
    lista.sort()
    print(lista)
    diff = 10000000
    s = 0
    e = len(lista) - 1
    s_res = 0
    e_res = 0
    while s < e:
        if abs(lista[s] + lista[e] - x) < diff:
            s_res = s
            e_res = e
            diff = abs(lista[s] + lista[e] - x)
        if lista[s] + lista[e] < x:
            s += 1
        else:
            e -= 1
    return [lista[s_res], lista[e_res]]

def reverse_only_alphas(string):
    lista = list(string)
    s = 0
    e = len(lista) - 1
    while s < e:
        if lista[s].isalpha() and lista[e].isalpha():
            temp = lista[s]
            lista[s] = lista[e]
            lista[e] = temp
            s += 1
            e -= 1
        elif lista[s].isalpha():
            e -= 1
        elif lista[e].isalpha():
            s += 1
        else:
            s += 1
            e -= 1
    return "".join(lista)

def swap(lista, first, second):
    temp = lista[first]
    lista[first] = lista[second]
    lista[second] = temp

def select_sort(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min]:
                min = j
        swap(lista, i, min)
    return lista

def insert_sort(lista):
    for i in range(1, len(lista)):
        insert = lista[i]
        move_item = i
        while insert > 0 and lista[move_item - 1] > insert:
            lista[move_item] = lista[move_item - 1]
            move_item -= 1
        lista[move_item] = insert
    return lista

def select_search(lista, k):
    notfound = -1
    for element in lista:
        if element == k:
            return lista.index(element)
    return notfound

def binary_search(lista, k):
    lista.sort()
    print(lista)
    found = -1
    s = 0
    e = len(lista) - 1
    m = (s + e) // 2
    while s < e or found == -1:
        if lista[m] == k:
            found = m
        if lista[m] < k:
            s += 1
        else:
            e -= 1
        m = (s + e) // 2
    return found

def anagram_val(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

def find_goodtest(generated_test, test_ids):
    for dictionary in generated_test:
        if dictionary['test_id'] in test_ids:
            return dictionary

def order_dictionary(string):
    # Create dictionary
    dictionary = dict()
    for i in range(len(string)):
        dictionary[string[i]] = string.count(string[i])
        
    # order dictionary by keys
    print("Dictionary counts orederd by key:")
    for key, value in sorted(dictionary.items()):
        print('{}: {}'.format(key, value), end=' ')
    print()
    
    # order dictionary by values
    print("Dictionary counts orederd by value:")
    for key, value in sorted(dictionary.items(), key = lambda x: x[1]):
        print('{}: {}'.format(key, value), end=' ')
    print()

def convert_to_dict(lista):
    dictionary = dict()
    for element in lista:
        dictionary[element] = lista.count(element)
    return dictionary

def compare_dict_keys(dictionary1, dictionary2):
    dict1_keys = list(dictionary1.keys())
    dict2_keys = list(dictionary2.keys())
    status = False
    if len(dictionary1) == len(dictionary2):
        for i in range(len(dictionary1)):
            if dict1_keys[i] != dict2_keys[i]:
                break
            else:
                status = True
    return status

def compare_dict_values(dictionary1, dictionary2):
    if compare_dict_keys(dictionary1, dictionary2):
        dict1_values = list(dictionary1.values())
        dict2_values = list(dictionary2.values())
        count = 0
        for i in range(len(dictionary1)):
            if dict1_values[i] == dict2_values[i]:
                count += 1
        if len(dictionary1) == count:
            return True        
    else:
        return False
    
def compare2dicts(list1, list2):
    list1.sort()
    list2.sort()
    dict1 = convert_to_dict(list1)
    dict2 = convert_to_dict(list2)
    
    if compare_dict_keys(dict1, dict2) and compare_dict_values(dict1, dict2):
        return True
    else:
        return False
    
def compare2dictsSimple(list1, list2):
    list1.sort()
    list2.sort()
    dict1 = convert_to_dict(list1)
    dict2 = convert_to_dict(list2)
    count = 0
    if len(dict1) == len(dict2):
        for key1, value1 in dict1.items():
            for key2, value2 in dict2.items():
                if (key1 == key2) and (value1 == value2):
                    count += 1
        print('equal elements =', count, ' dictionaries lengths', len(dict1))
        if count == len(dict1):
            return True
        else:
            return False
    else:
        return False
    
def merge_sort(lista):
    if len(lista) > 1:
        s = 0
        e = len(lista) - 1
        m = e // 2
        L = lista[:m+1]
        R = lista[m+1:]
        merge_sort(L)
        merge_sort(R)
        '''if e <= 0:
            return ""
        else:
            print('{}\t\t{}'.format(L, R))
            merge_sort(R)
            merge_sort(L)'''
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    
def string_manipulation():
    s = "Naomi and Carlitos are very super duper cute" 
    print(s.swapcase())
    print(s.find('N'))
    print(s.rfind('n'))
    print(s.replace('duper', 'dupper', 1))
    print(s.index('Carlitos'))
    print('min', min(s))
    print('max', max(s))
    if s.startswith(s[0]):
        print('starts with "N" at', s.index('N'))
    if s.endswith('e'):
        print('ends with e at', s.rindex('e'))
    print(s+s)
    print(list(s))
    print(s.split())
    print("/".join(s.split()))
    sto = s[:]
    print(sto)
    sto = s[::-1]
    print(sto)
    s = "swaroop"
    if s.startswith('s'):
        print('Starts with S')
    if s.endswith('p'):
        print('Ends with P')
    if 'oo' in s:
        print(s.find('oo'))
    if s.find("x") == -1:
        print('Not found "x"')
    print("'oo' was found on {}, one at {} and the other at {}".format(s, s.find('o'), s.rfind('o')))
    print("'oo' was found on {}, one at {} and the other at {}".format(s, s.index('o'), s.rindex('o')))
    s2 = "Cute Naomi, chula"
    print(s2.title())
    print(s2.swapcase())
    print(s2.split())
    print(s2.split(',', 1))
    listas = list(s2)
    print("+".join(listas))
    s1 = "El cArLiToS quiroz es guaperrimo"
    print(s1.split(" ", 2))
    print(s1.rsplit(" ", 2))
    print(s1[3:11] + " " + s1[12:18].title() + " " + s1[22::][::-1])
    print(s[1:] + s[:1]) # to the left
    print(s[-1:] + s[:-1]) # to the right
    print()

def substring(s):
    lista = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    return lista

def longest_substring_noWordsDuplicates(s):
    lista = substring(s)
    lista_set = set(lista)
    temp = []
    for element in lista_set:
        temp.append(len(element))
    return max(temp)

def longest_substring_noLettersDuplicates(s):
    lista = substring(s)
    temp_list = []
    for element in lista:
        temp_list.append(len(remove_duplicates(element)))
    return max(temp_list)

def remove_duplicates(s):
    lista = list(s)
    temp_lista = lista[:]
    for element in temp_lista:
        if temp_lista.count(element) >= 2:
            lista.remove(element)
    return "".join(lista)

def list_manipulation(lista):
    print('List Manipulation:')
    print(lista)
    lista0 = lista.copy()
    lista1 = lista[:]
    lista.append(100)
    lista.remove(88)
    del lista[0:2]
    lista0.pop()
    lista1.pop()
    lista1.pop
    lista1.extend(lista0)
    print('original list:', lista)
    print('list referenced:', lista0)
    print('list cloned:', lista1)
    
def separate_numbers(num):
    length = round(math.log10(num)) + 1
    temp = []
    temp.append(num % 10)
    result = num // 10
    while result != 0:
        temp.append(result % 10)
        result = result // 10
    return temp[::-1]

def separate_nums(num):
    res = []
    for i in range(math.round(math.log10(num)+1)):
        if i == 0:
            div = num // 10
            mod = num % 10
        else:
            mod = div % 10
            div = div // 10
        res.append(mod)
    return res[::-1]

def group_anagrams_bf(strs):    
    main = list()
    anagram = []
    strs_cp = strs[:]
    for i in range(len(strs)):
        if strs[i] in anagram:
            continue
        else:
            anagram = []
            if strs[i] in strs_cp:
                anagram.append(strs[i])
            else:
                continue
        for j in range(i + 1, len(strs)):
            if sorted(strs[i]) == sorted(strs[j]):
                anagram.append(strs[j])
                strs_cp.remove(strs[j])
        main.append(anagram)
    return main

def group_anagrams(s1):
    s2 = s1[:]
    main = []
    for i in range(len(s1)):
        if s1[i] not in s2:
            continue
        pointer = 0
        e = len(s2) - 1
        anagram = []
        while pointer <= e:
            if sorted(s1[i]) == sorted(s2[pointer]):
                anagram.append(s2[pointer])
                s2.remove(s2[pointer])
            else:
                pointer += 1
            e = len(s2) - 1
        main.append(anagram)
    return main

def minwindowsubs(s, t):
    pointer = 0
    e = len(s) - 1
    temp = list(t)
    res = []
    main = []
    while pointer <= e:
        if s[pointer] in t:
            while len(temp) != 0:
                if s[pointer] in temp:
                    temp.remove(s[pointer])
                res.append(s[pointer])
                pointer += 1
            main.append(res)
            res = []
            temp = list(t)
        pointer += 1
    
    dict_ = dict()
    for element in main:
        dict_[len(element)] = element
    
    lista = list(sorted(dict_.items()))
    
    return "".join(lista[0][1])

def palindorme(string):
    s = 0
    e = len(string) - 1
    string = string.lower()
    while s < e:
        if string[s].isalpha() and string[e].isalpha():
            if string[s] != string[e]:
                return False
            else:
                s += 1
                e -= 1
        elif string[s].isalpha():
            e -= 1
        elif string[e].isalpha():
            s += 1
        else:
            s += 1
            e -= 1
    return True

def order_dictionary_values(words):
    dictionary = dict()
    for characters in words:
        dictionary[characters] = words.count(characters)    
    sorted_dict = list(sorted(dictionary.items(), key = lambda x: x[1], reverse = True))
    return sorted_dict
    
def substring_practice(s):
    lista = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    return lista

def grouping_data(data):
    unique_keys = []
    groups = []
    sorted_data = sorted(data)
    
    for key, group in groupby(sorted_data):
        unique_keys.append(key)
        groups.append(list(group))
    
    print('original data: ', data)
    print('sorted data: ',sorted_data)
    print('keys: ',unique_keys)
    print('groups: ',groups)
    
def remove_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sl = list(s)
    for vowel in vowels:
        while vowel in sl:
            sl.remove(vowel)
    return "".join(sl)

def list_():
    numbers = [randint(10, 90) for i in range(20)]
    mythical = ["Unicorn", "Balrog", "Vampire", "Dragon", "Minotaur"]
    list_= ['Dragon Hart', 'Dragon Sumack']
    #Adding
    print(numbers)
    mythical.append("Dragon Jack")
    mythical.insert(0, "Dragon Lore")
    mythical.extend(list_)
    print(mythical)
    
    #Removing
    mythical.remove("Dragon")
    print(mythical)
    del mythical[1:2]
    print(mythical)
    print(mythical.pop())
    print(mythical)
    lista = [i for i in range(1, 10, 2)]
    print("odd numbers:", lista)
    lista = [i for i in range(2, 11, 2)]
    print("even numbers", lista)
    
def tuples():
    tuple1 = ('January', 'February', 'March')
    tuple2 = tuple1 + ('April', 'May')
    tuple3 = tuple1, ('June', 'July')
    print(tuple1)
    print(tuple2)
    print(tuple3)
    x, y, z = tuple1
    print('unfolding...', x, y , z)
    print(tuple2[2])
    print('index', tuple2.index('May'))
    print(tuple2[2:3])
    
def dictionary():
    dict_car = {
                'name' : "Carlitos", 
                'age' : 5, 
                'hobby' : "build legos", 
                'likes' : "Cars", 
                'color' : "blue", 
                'movies' : ["Aladdin", "paw-petrol", "lion king"], 
                'superheroes' : ("spiderman", "batman", "superman")
                }
    for element in dict_car:
        print('{}:'.format(element))
        
        if type(dict_car[element]) == list or type(dict_car[element]) == tuple:
            for j in range(len(dict_car[element])):
                print('\t{}'.format(dict_car[element][j]))
        else:
            print('\t{}'.format(dict_car[element]))
    
def sets():
    set_ = set()
    set_ = {"cherry", "blueberry", "rasperry", "blueberry"}
    set2 = ("apple", "pineapple", "mango")
    print(set_)
    set_.add(set2)
    set_.add("banana")
    print(set_)
    for element in set_:
        print(element)
    set_.remove('banana')
    print(set_)
    set3 = {"orange", "melon"}
    set_.update(set3)
    print(set_)
    set4 = {"kiwi",}
    print(set4)
    set5 = set_.union(set4)
    print(set5)
    set5.add("banana")
    print(set5)
    set5.discard("banana")
    print(set5)
    set6 = set5.intersection(set4)
    print(set6)
    set6_ = set4.intersection(set5)
    print(set6_)
    set7 = set5.difference(set4)
    set7_ = set_.difference(set3)
    set8 = set5.symmetric_difference(set4)
    print(set7)
    print(set7_)
    print(set8)
    
if __name__ == "__main__":
    #print(getname2()) 
    print(5 ^ 3)
    print(1 << 3) # 1 * 2^3
    print('sum of 5+3 =', suma(5, 3))
    
    print('substraction of 5-3 =', resta(5, 3))
    
    print('multiplication of 5 * 3 =', multiplication(5, -3))
    
    print('division of 6 / 3 =', division(6, 3))
    
    print('mod of 7 / 3 =', mod_(7, 3))
    
    print(compare(5, 5))
    print(compare(9, 8))
    
    lista = [randint(10, 90) for i in range(10)]
    print(lista)
    
    lists(lista)
    
    json_imports_exports(lista)
    
    printSpiralMatrix(6)
    
    string = "TestCaseTestCaseCaseTest"
    sub_string = "CaseT"
    print(find_substring(string, sub_string))
    print()
    
    sp = "{[([])[]{()}]}"
    print(parenthesis_validation(sp))
    print()
    
    s = "abcdefghijkl"
    print(s)
    print(reverse_chuncks(s, 3))
    
    print()
    primeNums(100)
    
    print('factorial of 5 =', factorial(5))
    
    print('fibonacci series of 5 =', fibonacci(10))
    
    fibonacci_series(10)
    
    print(conversionDecBin(5))
    
    s = "101"
    print(conversionBinDec(s))
    
    string = 'a#@b?*c&d!-+@e'
    print(string)
    print(reverse_only_alphas(string))
    
    x = 80
    print(find_sum_2sums(lista, x))
    print(find2sum(lista, x))
    
    lista = [90, 88, 2, 23, 24, 56, 70, 48, 33, 63, 12, 88, -20, -3, -1]
    print(lista)
    print('sum of 3 nums is 0 =', find_sum_3nums(lista, 0))
    print('sum of 4 nums is 0 =', find_sum_4nums(lista, 0))
    print('closest sum of x = 1 is', find_closest_sum(lista, 1))
    
    lista = [90, 88, 2, 23, 24, 56, 70, 48, 33, 63, 12, 88, -20, -3, -1]
    print(lista)
    print('select sort:', select_sort(lista))
    
    lista = [90, 88, 2, 23, 24, 56, 70, 48, 33, 63, 12, 88, -20, -3, -1]
    print(lista)
    print('insert_sort:', insert_sort(lista))
    
    lista = [90, 88, 2, 23, 24, 56, 70, 48, 33, 63, 12, 88, -20, -3, -1]
    print(lista)
    print('looking for -20, which is at', select_search(lista, -20))
    print('through binary search 70 is at', binary_search(lista, 70))
    
    str1 = "cinema"
    str2 = "iceman"
    print("{} and {} are anagrams? {}".format(str1, str2, anagram_val(str1, str2)))
    
    test_ids = ['cat', 'dog', 'log']
    generated_tests = [{'test_id': 'dogz', 'number': 12}, {'test_id': 'log', 'number':15}]
    print(find_goodtest(generated_tests, test_ids))
    
    string = "Peristance and Determination alone are all powerful a#@b?*c&d!-+@e"
    order_dictionary(string)
    
    list1 = ['apple', 'orange', 'kiwi', 'pineaple', 'strawberry']
    list2 = ['kiwi', 'apple', 'orange', 'strawberry', 'pineaple', 'apple']
    print(list1)
    print(list2)
    print("Compare two dicts" ,compare2dicts(list1, list2))
    print("Compare two dicts simpler" ,compare2dictsSimple(list1, list2))
    
    print()
    lista = [90, 88, 2, 23, 24, 56, 70, 48, 33, 63, 12, 88, -20, -3, -1]
    print(lista)
    merge_sort(lista)
    print(lista)
    print()
    string_manipulation()
    list_manipulation(lista)
    print()
    s = "poder total"
    print(substring(s))
    print(longest_substring_noWordsDuplicates(s))
    print(longest_substring_noLettersDuplicates(s))
    print()
    
    numbers = 12345
    print(numbers)
    print(separate_numbers(numbers))
    print()
    
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(strs)
    print(group_anagrams_bf(strs))
    print(group_anagrams(strs))
    print()
    
    s = "ADOBECODEBANC"
    t = "ABC"
    print(s)
    print(t)
    print('Minimum window substring: ', minwindowsubs(s, t))
    print()
    
    s = "A man, a plan, a canal: Panama"
    print(s)
    print('Is it a plaindrome?', palindorme(s))
    print()
    
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    print(words)
    print(order_dictionary_values(words))
    print()
    
    s = "BANANA"
    print(substring_practice(s))
    print()
    
    data = ['a', 'b', 'a', 'a', 'c', 'd', 'b', 'g', 'f', 'c']
    grouping_data(data)
    
    s = "Hola Carlitos"
    print(s)
    print(remove_vowels(s))
    print()
    
    list_()
    print()
    tuples()
    print()
    
    dictionary()
    print()
    
    sets()
    print()