'''
@author: Solrac
'''
import json
import logging
import traceback
import time
import math
import random
from itertools import combinations
import itertools
import urllib
from bs4 import BeautifulSoup
import ssl

start_time = time.time()

logging.basicConfig(filename='../logs/logs_.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s %(message)s')

logging.info('Convert dictionary to json')
def convert_to_json():
    logging.debug('Create config File')
    config_dict = {'Gotcha_srv':{
                                  'username': 'tester1',
                                  'email': 'tester1@gotcha.com',
                                  'password': 'abcd234',
                                  'certificate': 'tester.cer',
                                  'platform': 'Windows',
                                  'language': 'Java',
                                  },
                    'Ronin_srv': {
                                  'username': 'tester2',
                                  'email': 'tester1@ronin.com',
                                  'password': 'dfd536',
                                  'certificate': 'tester2.cer',
                                  'platform': 'Linux',
                                  'language': 'C++',
                                  },
                    'Crixus_srv': {
                                  'username': 'tester3',
                                  'email': 'tester1@crixus.com',
                                  'password': 'ssdff32',
                                  'certificate': 'tester3.cer',
                                  'platform': 'Python',
                                  'language': 'Mac',
                                  },
                    'Spartacus_srv': {
                                  'username': 'tester4',
                                  'email': 'tester1@spartacus.com',
                                  'password': 'afdfd32',
                                  'certificate': 'tester4.cer',
                                  'platform': 'Unix',
                                  'language': 'JavaScript',
                                  },
                    }
    logging.debug('dumping data to a variable using the json library')
    to_json = json.dumps(config_dict, indent = 4, sort_keys = True)
    
    logging.debug('dumping data to and create a json file')
    config_file = open('config.json', 'w')
    config_file.write(to_json)
    config_file.close()
    
convert_to_json()

logging.info('Convert json file into a dictionary')
def access_jsonFile(rawJsonFile):
    username = []
    password = []
    
    logging.debug('accessing data form the json file using load')
    json_file = open(rawJsonFile)
    dict_ = json.load(json_file)
    for key, value in dict_.items():
        for k, v in value.items():
            if k == "email":
                username.append(v)
            if k == "password":
                password.append(v)
    
    print(username)
    print(password)
    ####################################################
    
    #with open(jsonFile) as json_file:
    #    data = json.load(json_file)
    #    print(data)

jsonFile = 'C:\\Users\\Solrac\\workspace\\Python.Development\\InterviewPractice\\config.json'
print(access_jsonFile(jsonFile))

logging.info('practice converting to jsonfile')
def practice(dict_):
    json_format = json.dumps(dict_, indent = 4, sort_keys =  True)
    jsonf = open("jsonfile.json", 'w')
    jsonf.write(json_format)
    jsonf.close()

lista = ['Ronin', 'the pursue of happiness', 'Gotcha!']
dict_ = [{'movie': 'The Godfather', 'rating': 9}, {'movie': 'Ronin', 'rating': 8}]
practice(dict_)
result = [dict_[i] for i in range(len(dict_)) if dict_[i]['movie'] in lista]
print(result)

logging.info('practice converting to dictionary')
def practice2(jsonFile_raw):
    jsonFile = open(jsonFile_raw)
    dict_ = json.load(jsonFile)
    for dictionary in dict_:
        if dictionary['rating'] > 8:
            print('Best reviewed movie: ', dictionary)
    return dict_

jsonFile_raw = 'C:\\Users\\Solrac\\workspace\\Python.Development\\InterviewPractice\\jsonfile.json'
print(practice2(jsonFile_raw))

def handling_error():
    a = 3
    b = 7
    c = 0
    
    if b > a:
        print(a + b)
    else:
        raise Exception('b should be bigger than a')
    
    try:
        print(b / c)
    except Exception as e:
        print(e)
        
    try:
        print(a + 'c')
    except:
        errorFile = open('../error_handling/errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('Logs can be found in errorInfo.txt')

handling_error()
print(round(time.time() - start_time, 3), '\n')

# String manipulation
def str_manipulation():
    s = 'Logs in can be found in errorInfo.txt testing is fun'
    # reverse
    print(s)
    print(s[::-1])
    print(s.swapcase())
    print(s.find('in '))
    print(s.rfind('in '))
    print('left rotation:', s[4:] + '', s[:4])
    print('right rotation:', s[-4:] + '', s[:-4])
    
    for i in range(len(s)):
        if s[i] == 'in':
            print(i)

    #find duplicates
    dup = []
    for i in range(len(s)):
        if s[i] in dup:
            continue
        if s.count(s[i]) >= 2:
            dup.append(s[i])
    print(dup)
    
    dict_ = {}
    for i in range(len(s)):
        if s.count(s[i]) >= 2:
            dict_[s[i]] = s.count(s[i])
    print(dict_)
    
    #find non-duplicates
    nondup = []
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            nondup.append(s[i])
    print(nondup)
    
    # find max and min
    print('first max', max(s))
    list_ = list(s)
    print(list_)
    list_.remove(max(s))
    s1 = "".join(list_)
    print('second max', max(s1))
    print('min', min(s))
    
    # validate palindrome
    sp = " an5na "
    sp = sp.strip()
    list_ = list(sp)
    alphalist = []
    for character in list_:
        if character.isalpha():
            alphalist.append(character)
    new_sp = "".join(alphalist)
    reversed_new_sp = new_sp[::-1]
    if new_sp == reversed_new_sp:
        print(True)
    else:
        print(False)
    
    #substrings
    substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    print(substrings)
    
    # remove vowels
    list_ = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        while vowel in list_:
            list_.remove(vowel)
    s1 = "".join(list_)
    print(s1)
    
    
    
def slide_reversed(s, bulk):
    lista = []
    for i in range(0, len(s), bulk):
        lista.append(reverse_str(s[i:bulk+i]))
    return "".join(lista)

def reverse_str(s):
    list_ = []
    lista = list(s)
    for i in range(len(lista)-1, -1, -1):
        list_.append(lista[i])
    return "".join(list_) 
    
str_manipulation()
s = "abcdefghijkl"
bulk = 4
print(slide_reversed(s, bulk))

def parenthesis_validation(s):
    p = list(s)
    stack = []
    op = ['{', '[', '(']
    cp = ['}', ']', ')']
    
    for i in range(len(p)):
        if p[i] in op:
            stack.append(p[i])
        elif p[i] in cp:
            pos = cp.index(p[i])
            if len(stack) > 0 and op[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                return 'UNBALANCED'
    if len(stack) == 0:
        return 'BALANCED'

s = '{[(){}[]]{}[()]}'
print(parenthesis_validation(s))

def anagramvalidation(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False

s1 = 'cinema'
s2 = 'iceman'
print(anagramvalidation(s1, s2))

def fibonacci(n):
    if n <= 0:
        return 0;
    elif n == 1:
        return 1;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(20))

def prime(n):
    for i in range(2, n + 2):
        if i == 2:
            print(i, end=" ")
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                print(i, end=" ")
                break
                
def prime2():
    for i in range(1, 334):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
                else:
                    print(i, end=', ')
                    break

prime()
print()
prime2()
print()

def dec_bin(num):
    if num == 0:
        return ""
    else:
        return dec_bin(num // 2) + str(num % 2)
    
def dec_bin2(num):
    if num == 0:
        return ""
    else:
        return dec_bin2(num // 2) + str(num % 2)

print(dec_bin(333))
print(dec_bin2(117))
print(hex(333))

def bin_dec(bnum):
    lista = list(bnum)
    lista.reverse()
    result = 0
    for i in range(len(lista)):
        result += int(lista[i]) * 2 ** i
    return result

print(bin_dec('10100101'))

def combinaciones(s, n):
    lista = list(s)
    return list(itertools.combinations(lista, n))

s = "baca"
print(combinaciones(s, 2))

def generate_matrix(n):
    return [[random.randint(1, 99) for i in range(n)] for j in range(n)]

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

print(generate_matrix(4))
matrix = [[27, 8, 12, 70], [76, 45, 87, 71], [43, 71, 35, 92], [60, 58, 35, 64]]
print_matrix(matrix)

def spiral_matrix(endRow, endColumn):
    matrix = generate_matrix(4)
    startRow = 0
    startColumn = 0
    lista = []
    
    while startRow < endRow and startColumn < endColumn:
        for i in range(startColumn, endColumn):
            lista.append(matrix[startRow][i])
            
        startRow += 1
        
        for i in range(startRow, endRow):
            lista.append(matrix[i][endColumn-1])
            
        endColumn -= 1
        
        if startRow < endRow:
            for i in range(endColumn -1, startColumn-1, -1):
                lista.append(matrix[endRow-1][i])
                
            endRow -= 1
            
        if startColumn < endColumn:
            for i in range(endRow-1, startRow-1, -1):
                lista.append(matrix[i][startColumn])
                
            startColumn += 1
    return lista

print(spiral_matrix(4, 4))

def test_validation(generated_tests, test_ids):
    return [dict_ for dict_ in generated_tests if dict_['test_id'] in test_ids]
    
test_ids = ['cat', 'dog', 'log']
generated_tests = [{'test_id': 'dogz', 'number': 12}, {'test_id': 'log', 'number':15}]
# output = [{'test_id' : 'log', 'number' : 15}]
print(test_validation(generated_tests, test_ids))

def orderdictvalues(dict_):
    for key, value in sorted(dict_.items(), key=lambda x: x[1], reverse = True):
        print("{} : {}".format(key, value))

dict_ = {'a': 9, 'b': 8, 'c': 7, 'd': 6, 'e': 5}
print(dict_)
orderdictvalues(dict_)

# jsonfile = json.dumps(dict_, indent = 4, sort_keys=True)
    
lista = [
         {
          'Carlos': {
                     '50_movie': 'Rebel w/o Cause',
                     '60_movie': 'The Graduate',
                     '70_movie': 'The Godfather',
                    },
          'Camelit': {
                      '50_music': 'Run away Sue',
                      '60_music': 'Apache',
                      '70_music': 'Dont let me be misunderstood',
                      },
           'Nando':  {
                      'chocolate1': '3 Musketers',
                      'gum': 'beisbol bubble gum',
                      'song': 'seven up',
                      },
          },
         {
          'Carlos': {
                     '80_movie': 'AMADEUS',
                     '90_movie': 'Ronin',
                     '00_movie': 'The Pursue of Happiness',
                     '60_music': 'Time cannot wait'
                    },
          'Camelit': {
                      '60_music': 'Any 60s songs', 
                      '80_music': 'Rockin Amadeus',
                      '90_music': 'It is a beautiful life',
                      '00_music': 'Feel',
                      },
           'Nando':  {
                      '60_music': 'I cannot get more satisfaction',
                      'movie': 'top gun',
                      'serie': 'el portaaviones',
                      },
          }
         ]

for dict_ in lista:
    dict_keys = list(dict_.keys())
    if '00_movie' in dict_[dict_keys[0]]:
        print("{} : {}".format(dict_keys[0], dict_[dict_keys[0]]['00_movie']))
print()

for dict_ in lista:
    dict_keys = list(dict_.keys())
    dict_values = list(dict_.values())
    if '00_movie' in dict_[dict_keys[0]]: 
        print(dict_keys[0], dict_[dict_keys[0]]['00_movie'])
        
for dict_ in lista:
    keys = list(dict_.keys())
    for i in range(len(keys)):
        if keys[i] == 'Nando':
            print('{} : {}'.format(keys[i], dict_[keys[i]]))  
            
for dict_ in lista:
    keys = list(dict_.keys())
    values = list(dict_.values())
    for key, value in dict_.items():
        for k, v in value.items():
            if v == 'The Godfather':
                print("{}".format(key))
                print("\t{} : {}".format(k, v))
                
lista1 = ['apple', 'orage', 'banana', 'strawberry', 'melon', 'watermelon']
lista2 = ['melon', 'mango', 'grapes', 'strawberry', 'guava']
set1 = set(lista1)
set2 = set(lista2)
set3 = {'guava', 'orange', 'berry'}
set3.add('passion fruit')
print(set1, set2, set3)
print('union: ', set1.union(set2))
print('difference1:', set1.difference(set2))
print('difference2:', set2.difference(set1))
print('intersection1:', set1.intersection(set2))
print('intersection2:', set2.intersection(set1))
print('intersection2:', set2.intersection(set3))
print('all differences', set1.symmetric_difference(set2))
print('all diff', set1.symmetric_difference(set3))
        
def sorting(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i+1, len(lista)):
            if lista[min] > lista[j]:
                min = j
        swap(lista, i, min)
    return lista
    
def swap(lista, first, second):
    temp = lista[first]
    lista[first] = lista[second]
    lista[second] = temp

lista = [5, 8, 2, 7, 3]
print(lista)
print(sorting(lista))

def linearSearch(lista, k):
    for i in range(len(lista)):
        if lista[i] == k:
            print(i)
linearSearch(lista, 7)

def binarySearch(lista, k):
    start = 0
    end = len(lista)
    middle = (start + end + 1) // 2
    found = -1
    while start < end and found == -1:
        if lista[middle] == k:
            found = middle
        if lista[middle] < k:
            start = middle + 1
        else:
            end = middle -1
        middle = (start + end + 1) // 2
    return found

print(binarySearch(lista, 7))

'''def parsing(url_):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CertificateError
    
    url = url_
    html = url.urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))
    
parsing("https://usersnap.com/blog/gitlab-github/")'''

