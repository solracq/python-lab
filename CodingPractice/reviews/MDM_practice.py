'''
@author: Solrac
'''
import time
from CodingPractice.OOP.simple_exs import MDM_class
from random import randint
from itertools import combinations

def strings_manipulation():
    start_time = time.time()
    # Strings
    s = "Success is the ability to move from failure to failure with no loss of enthusiasm"
    
    # Files
    ios_logs = "C:/Users/Solrac/workspace/Python.Development/InterviewPractice/logs_ios.log"
    wifi_logs = "C:/Users/Solrac/workspace/Python.Development/InterviewPractice/wifi_logs_ios.log"
    # Opening files
    # ios_logs_lines = open(ios_logs)
    # wifi_logs_lines = open(wifi_logs)
    # Lists of file lines
    list_ios_logs = ios_logs_lines.readlines()
    list_wifi_logs = wifi_logs_lines.readlines()
    
    # Lists
    words_list = s.split(" ")
    chars_list = list(s) 
    
    print(s)
    print("Putting each word of the string into a list", '\n', words_list)
    print("putting each character of the string into a list", '\n', chars_list)
    print(s.swapcase())
    print("Number of times 'a' was found", s.count('a'))
    print(s[15:22])
    print(s.title())
    print(" ".join(words_list), '\n', "".join(chars_list))
    print("Maximum", max(s))
    print("Minimum", min(s))
    chars_list.sort()
    print(chars_list)
    chars_list.reverse()
    print(chars_list, '\n')
    print(sorted(words_list))
    print(sorted(words_list, reverse = True), '\n')
    print(s[15:22], "vs", s[36:43])
    s1 = " Testing is fun"
    print(s+s1, '\n')
    print(s1.join(words_list))
    
    if "Success" in s:
        print("Found word 'Success' in ", s)
    if s.find("failure") != -1:
        print("Found the first word 'failure' at ", s.index("failure"))
    if s.rfind("failure") != -1:
        print("Found the last word 'failure' at ", s.rindex("failure"))
    if s[15:22].startswith('a'):
        print(s[15:22], "starts with 'a'")
    if s[15:22].endswith('y'):
        print(s[15:22], "ends with 'y")
    s2 = "   abcdefg  "
    print(s2)
    print(s2.strip())
    print(s.replace('failure', 'successful', 1))
    
    # iOS logs
    for line in list_ios_logs:
        line = line.strip('\n')
        lista = line.split(": ")
        if len(lista) > 1:
            if lista[1] == 'Sensor':
                split_datetime_list = lista[0].split(" ")
                split_date_list = split_datetime_list[0].split('-')
                split_time_list = split_datetime_list[1].split(':')
                if (split_date_list[0] == '2020') and (split_date_list[1] == '01') and (split_date_list[2] == '12'):
                    split_second = split_time_list[2].split(".")
                    if (split_time_list[0] == '07') and (split_time_list[1] == '59') and (int(split_second[0]) > 37) and (int(split_second[0]) < 39):
                        if 'error' in line.lower() or 'err' in line.lower():
                            print(line)
    
    # wifi logs
    time_ = []
    for line in list_wifi_logs:
        date_list = line.split(" __")
        if len(date_list) > 1:
            date_list[0] = date_list[0].strip(' ')
            date_list[1] = date_list[1].strip('\n')
            if ('(stationary):' in line) or ('(moving):' in line):
                type_log_list = date_list[1].split('): ')
                type_log_list =type_log_list[1].replace(': ', ':')
                log_info_list = type_log_list.split(' ')
                time_item = log_info_list[len(log_info_list)-1]
                time_item = time_item.strip('secs')
                time_list = time_item.split(':')
                time_.append(float(time_list[1]))
    print()
    
    for line in list_wifi_logs:
        date_list = line.split(" __")
        if len(date_list) > 1:
            date_list[1] = date_list[1].strip('\n')
            if ('(stationary):' in line) or ('(moving):' in line):
                type_log_list = date_list[1].split('): ')
                type_log_list =type_log_list[1].replace(': ', ':')
                log_info_list = type_log_list.split(' ')
                time_item = log_info_list[len(log_info_list)-1]
                time_item = time_item.strip('secs')
                time_list = time_item.split(':')
                if float(time_list[1]) == max(time_):
                    print(line.strip(' '))
    print("Run Time =", time.time() - start_time)

def combinaciones(lista, n):
    return list(combinations(lista, n))

def tuples_manipulation():
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    for month in months:
        print(month, end='      ')
    months = months + ('January', 'April')
    months = months + ('August',)
    print()
    print(months)
    greetings = ("hello", "Hi")
    months = months + greetings
    print(months)
    for i in range(len(months)):
        print(months[i], end= '   ')
    print()
    print(months.index('August'))
    print(sorted(months))
    print(sorted(months, reverse = True))
    print(max(months))
    print(min(months))
    if months.count('August') == 2:
        print("There are two Augusts")
    list_combinations = combinaciones(months, 2)
    print(list_combinations)
    print(max(list_combinations))
    print(min(list_combinations))
    print()
    
    list_moda = [('January', 31), ('February', 29), ('March', 31), ('April', 30), ('May', 31), ('June', 30), ('July', 31), ('August', 31), ('September', 30), ('October', 31), ('November', 30), ('December', 31)]
    print(list_moda[7])
    print(list_moda[7][0], list_moda[7][1])
    tuple_ = (1, 2, 3, 4, 5)
    for i in range(len(list_moda)):
        print(list_moda[i][0], " : ", list_moda[i][1]) 
    
    months = months + ('January', 'April', 'August')
    print(months)
    
    mnth = months[:]
    mnth = mnth, tuple_
    print(mnth)
    
    #get duplicates
    duplicates = []
    nondup = []
    for month in months:
        if month in duplicates:
            continue
        if months.count(month) >= 2:
            duplicates.append(month)
        if months.count(month) == 1 and month != 'hello' and month != 'Hi':
            nondup.append(month)
    print("Duplicated months: ", duplicates)
    print("Non-duplicated months: ", nondup)
    print(months.index("March"))
    print(max(nondup))
    print(min(nondup))
    print(nondup[-3:-1])
    test = ('testarrosa', 'testDrive', 333)
    print(test)
    print("{} : {} : {}".format(*test))
    (car, game, favnum) = test
    print("{} / {} / {}".format(car, game, favnum))
    list_ = [i for i in range(5)]
    print(list_)
    print()

def set_manipulation():
    list_ = ['apple', 'orange', 'kiwi', 'melon', 'mango', 'banana', 'strawberry', 'blueberry', 'cherry']
    seto = set(list_)
    setu = set()
    
    print(seto)
    for i in range(20):
        setu.add(randint(10, 90))
    print(setu)

    print(setu.pop(), setu)
    print(seto.pop(), seto)
    
    seto.remove("cherry")
    print("After removing cherry: ", seto)
    seto.add("passion fruit")
    print("After adding new fruit ", seto)
    seto.add("passion fruit")
    print("After adding new fruit ", seto)
    print("sorted: ", sorted(seto))
    print("reversed: ", sorted(seto, reverse = True))
    print(max(seto))
    print(min(seto))
    print(list(combinations(setu, 2)))
    set_ = set()
    set_.add("test")
    print(set_)
    
    s="abracadabra"
    s_set = set(s)
    list_ = list(s_set)
    s1 = "".join(list_)
    s2 = "".join(s_set)
    print(s1, " ", s2)
    
    s_set1 = s_set.copy()
    print(s_set1)
    s_set1.update('M', 'D', 'M')
    print(s_set1,'\n')
    print()
    
    seto.discard("orange")
    for fruit in seto:
        print(fruit)
    
    set1 = set(s1)
    set2 = set(s2)
    set2.add('x')
    set1.add('z')
    print("union adbcrxz", set1.union(set2))
    print("diff z", set1.difference(set2))
    print("diff x", set2.difference(set1))
    print("inter rdabc", set1.intersection(set2))
    print("inter rdabc", set2.intersection(set1))
    print("symetric diff xz", set1.symmetric_difference(set2))
    
    if set1.isdisjoint(set2):
        print("there is no intersection")
        
    if set1.issubset(set2):
        print("set1 is subset of set2")
    
    if set1.issuperset(set2):
        print("set1 is superset of set2")
    print()

def dictionary_manipulation():
    dictionary = dict()
    dictionary["movie"] = "Redrick"
    dictionary["car"] = "Testarrosa"
    dictionary["color"] = "blue"
    dictionary["music"] = "storm"
    dictionary["test"] = "beautiful"

    print(dictionary)
    print(dictionary.keys())
    print(dictionary.values())
    print(dictionary.items())
    
    del dictionary["test"]
    print(dictionary)
    rmvd = dictionary.pop("music")
    print(rmvd)
    print(dictionary)
    dict_ = {
            'mov1': "as good as it gets",
            'mov2': "beautiful mind",
            'mov3': "ronin",
            'mov4': "scott pilgrim vs the world" ,
             }
    for keys, values in dict_.items():
        dictionary[keys]=values
    print(dictionary)
    
    list_= ["Aladdin", "paw-petrol", "lion king"]
    list2_ = [1, 2, 3, 4, 5]
    tuple_ = ("spiderman", "batman", "superman")
    set_ = {'orange', 'banana', 'strawberry', 'blueberry', 'cherry', 'mango', 'melon', 'apple', 'kiwi'}
    
    dict_car = {
                'name' : "Carlitos", 
                'age' : 5, 
                'hobby' : "build legos", 
                'likes' : "Cars", 
                'color' : "blue", 
                'movies' : list_, 
                'superheroes' : tuple_,
                'fuits': set_,
                'elements': dict_,
                'nums': list2_,
                }
    
    for keys, values in dict_car.items():
        print("{} : ".format(keys))
        if values == list_ or values == tuple_ or values == set_ or values == list2_:
            for value in values:
                print("\t{}".format(value)) 
        elif values == dict_:
            for vkey, vvalue in values.items():
                print("\t{}: {}".format(vkey, vvalue))
        else:
            print("\t{}".format(values))
            
    s = "Success is the ability to move from failure to failure with no loss of enthusiasm"
    dict1 = dict() 
    duplicate = []
    for i in range(len(s)):
        if s[i] in duplicate:
            continue
        dict1[s[i]] = s.count(s[i])
        duplicate.append(s[i])
    
    ordered_list = sorted(dict1.keys())
    
    for element in ordered_list:
        print("{} : {}".format(element, dict1[element]))
    
    total = 0
    for values in dict_car.values():
        if values == list2_:
            for val in values:
                if val != str(val):
                    total += val
    print(total)
    print()
    
def list_manipulation():
    lista = list()
    lista.append(34)
    lista.append(45)
    lista.append(88)
    lista.append(23)
    lista.append(16)
    lista.append(53)
    lista.append(77)
    lista.append(90)
    lista.append(65)
    lista.append(5)
    lista.append(19)
    lista.append(52)
    lista.append(62)
    lista.append(58)
    lista.append(17)
    lista.remove(16)
    print(lista)
    
    print("find 77:", linear_search(lista, 77))
    print("find 88:", binary_search(lista, 88))
    
    selection_sort(lista)
    print(lista)
    lista.reverse()
    print(lista)
    insert_sort(lista)
    print(lista)
    
    lista.append(90)
    lista.append(65)
    lista.append(5)
    print(lista)
    
    dup = find_duplicates(lista)
    print(dup)
    unq = find_uniques(lista)
    print(unq)
    
def find_duplicates(lista):
    duplicates = []
    for i in range(len(lista)):
        if lista[i] in duplicates:
            continue
        if lista.count(lista[i]) == 2:
            duplicates.append(lista[i])
    return duplicates

def find_uniques(lista):
    unique = []
    for i in range(len(lista)):
        if lista.count(lista[i]) == 1:
            unique.append(lista[i])
    return unique
    
def linear_search(lista, key):
    location = -1
    for i in range(len(lista)):
        if lista[i] == key:
            location = lista.index(lista[i])
    return location

def binary_search(lista, key):
    location = -1
    selection_sort(lista)
    start = 0
    end = len(lista)
    middle = int((start + end + 1) / 2)
    while (start <= end) or (location == -1):
        if lista[middle] == key:
            location = middle
        if lista[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
        middle = int((start + end + 1) / 2)
    return location
    
def selection_sort(lista):
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
    
def insert_sort(lista):
    for i in range(1, len(lista)):
        insertion = lista[i]
        move_item = i
        while (move_item > 0) and (lista[move_item-1] > insertion):
            lista[move_item] = lista[move_item-1]
            move_item -= 1
        lista[move_item] = insertion
        
def anagram_validation(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
    
def comparison_bit_operators(a, b):
    if a^b == 0:
        print("{} and {} are equals".format(a,b))
    else:
        print("{} and {} are NOT equals".format(a,b))
        
def reversing_list(lista):
    list_ = []
    for i in range(len(lista)-1, -1, -1):
        list_.append(lista[i])
    return list_

def factorial_calc(n):
    if n <= 1:
        return 1
    else:
        return n*factorial_calc(n - 1)
    
def find_first_nonduplicate(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]

def find_first_duplicate(s):
    for i in range(len(s)):
        if s.count(s[i]) == 2:
            return s[i]
        
def find_unique_set(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.difference(set2)

def find_common_set(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

def find_common(list1, list2):
    new_list = []
    for element1 in list1:
        if element1 in new_list:
            continue
        for element2 in list2:
            if element2 in new_list:
                continue
            if element1 == element2:
                new_list.append(element1)
    return new_list

def find_unique(list1, list2):
    new_list = []
    for element1 in list1:
        if element1 in new_list:
            continue
        for element2 in list2:
            if element2 in new_list:
                continue
            if element1 not in list2:
                new_list.append(element1)
                break
    return new_list
            
def remove_duplicates(lista):
    nondup = []
    for i in range(len(lista)):
        if lista.count(lista[i]) == 1:
            nondup.append(lista[i])
    return nondup 
        
def find_first_second_maxs(lista):
    list_ = remove_duplicates(lista)
    print(list_)
    print("First maximum is ", max(list_))
    list_.remove(max(list_))
    print("Second maximum is ", max(list_))
    
def fizz_buzz():
    for i in range(0, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def find_max_sum(lista):
    total = 0
    new_list = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            total = lista[i] + lista[j]
            new_list.append(total)
    return max(new_list)

def sort_occurrences(lista):
    # 1 occurence
    one_occur = []
    two_occur = []
    three_occur = []
    more_occur = []
    for i in range(len(lista)):
        if lista.count(lista[i]) == 1:
            one_occur.append(lista[i])
        elif lista.count(lista[i]) == 2:
            two_occur.append(lista[i])
        elif lista.count(lista[i]) == 3:
            three_occur.append(lista[i])
        else:
            more_occur.append(lista[i])
    one_occur.sort()
    two_occur.sort()
    three_occur.sort()
    more_occur.sort()
    return one_occur + two_occur + three_occur + more_occur
    
def remove_vowels(s):
    s_list = list(s)
    new_list = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s_list)):
        if s_list[i] not in vowels:
            new_list.append(s_list[i])
    return "".join(new_list)

def urlify(s):
    s = s.strip()
    list_ = s.split(" ")
    return "%20".join(list_)

def balanced_parentheses_stack(s):
    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']
    stack = []
    for element in range(len(s)):
        if element in open_list:
            stack.append(element)
        elif element in close_list:
            location = s.index(element)
            if (len(stack) > 0) and (open_list[location] == stack[len(stack)-1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"

# Driver function
if __name__ == "__main__":
    start_time = time.time()
    # strings_manipulation()
    tuples_manipulation()
    set_manipulation()
    dictionary_manipulation()
    list_manipulation()
    
    s1 = "cinema"
    s2 = "iceman"
    print("Are '{}' and '{}' anagrams? {}".format(s1, s2, anagram_validation(s1, s2)))
    
    a= 4
    b= 4
    comparison_bit_operators(a, b)
    
    lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(lista)
    print(reversing_list(lista))
    
    lista_even = [i for i in range(0, 10, 2)]
    lista_odd = [i for i in range(1, 10, 2)]
    print(lista_even)
    print(lista_odd)
    print(factorial_calc(5))
    print(time.asctime())
    
    mdm = MDM_class.Mdm("cloi", 7)
    print(mdm.get_name(), mdm.get_age())
    mdm.set_name('gordolfo')
    mdm.set_age(5)
    mdm.sit()
    mdm.roll()
    print()
    
    s = "google"
    print(s)
    print("first non-duplicate is: ", find_first_nonduplicate(s))
    print()
    
    s1 = "ABCA"
    s2 = "BCABA"
    s3 = "ABC"
    print(s1)
    print("first duplicate is: ", find_first_duplicate(s1))
    print(s2)
    print("first duplicate is: ", find_first_duplicate(s2))
    print(s3)
    print("first duplicate is: ", find_first_duplicate(s3))
    print()
    
    lista = [5, 17, 19, 23, 34, 45, 52, 53, 58, 62, 65, 77, 88, 90, 90, 65, 5]
    find_first_second_maxs(lista)
    
    fizz_buzz()
    
    list1 = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
    list2 = ["THREE", "SEVEN", "EIGHT", "FOUR", "THREE"]
    print(find_common_set(list1, list2))
    print(find_unique_set(list1, list2))
    print(find_unique_set(list2, list1))
    print("other apporach common", find_common(list1, list2))
    print("other approach unique", find_unique(list1, list2))
    print("other approach unique", find_unique(list2, list1))
    print()
    
    print(lista)
    print("Maximum sum from list above: ", find_max_sum(lista))
    list_ = [-1, -2, -3, -4]
    print(list_)
    print("Maximum sum from list above: ", find_max_sum(list_))
    print()
    
    list_ = [3, 1, 2, 2, 4]
    print(list_)
    print(f"SORT OCCURENCES: {sort_occurrences(list_)}")
    print()
    
    s = "carlitos"
    print(s)
    print(remove_vowels(s))
    print()
    
    try:
        a = 3
        b = 0
        print(a/b)
    except ZeroDivisionError:
        print("Not allowed zero division!")
    finally:
        print()
        
    s = "  Mr. John Smith "
    print(urlify(s))
    
    s = "{[]{()}}"
    print(balanced_parentheses_stack(s))
    s = "[{}{})(]"
    print(balanced_parentheses_stack(s))
    print()
    
    print("Elapsed time = ", time.time()-start_time)