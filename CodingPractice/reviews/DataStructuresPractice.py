'''
@author: Solrac
'''
import time
import random
from itertools import combinations, permutations, product

start_time = time.time()

def list_():
    numbers = []
    mythical = ["Unicorn", "Balrog", "Vampire", "Dragon", "Minotaur"]
    
    # Adding
    print("ADDING TO LIST")
    for i in range(10):
        numbers.append(random.randint(10, 90))
    numbers[3] = random.randint(10, 90)
    numbers = numbers + [88]
    mythical.insert(0, "Fary")
    mythical.append("Orion")
    mythical.extend(["BenHur"])
    print(mythical)
    new_list = mythical + numbers
    print(new_list)
    print(new_list[-14:-11])
    print(new_list[:-14])
    new_list = new_list[:-14] + ["cyclope"]
    print(new_list)
    print()
    
    # Copy and index location of element
    print("COPYING AND GETTING INDEX IN LIST")
    new_list = mythical.copy()
    print(new_list)
    print(mythical.index("Vampire"))
    mythical.extend(["Medusa"])
    print(new_list)    
    print(numbers)
    print(mythical)
    print()
    
    # Sorting list
    print("SORTING LISTS")
    numbers.sort()
    mythical.sort()
    print(numbers)
    print (mythical)
    numbers.reverse()
    mythical.reverse()
    print(numbers)
    print (mythical)
    print()
    
    # Remove list elements and clear list
    print("REMOVE AND CLEAR LISTS")
    print(mythical)
    mythical.clear()
    print(mythical)
    mythical = new_list
    print(mythical)
    print(numbers)
    mythical.remove("BenHur")
    numbers.remove(numbers[-1])
    print(mythical)
    print(numbers)
    print(mythical.pop(mythical.index("Orion")))
    print(mythical)
    mythical.extend(["DragonJack"])
    mythical = mythical + ["DragonJack"]
    print(mythical)
    print(mythical.count("DragonJack"))
    print(numbers.count(88))
    del mythical[len(mythical)-1]
    print(mythical)
    del numbers[9]
    print(numbers)
    del numbers[-3: -1]
    print(numbers)
    print()
    
    # Finding elements
    print("FINDING ELEMENTS IN LIST")
    print(mythical)
    while "DragonJack" in mythical:
        mythical.remove("DragonJack")
    print(mythical)
    if "Balrog" in mythical:
        print(True)
    else:
        print(False)
    mythical.insert(1, "Vampire")
    print()
    
    # find the first and second maximums
    print("FIND THE FIRST AND SECOND MAXIMUMS")
    list_ = [3, 5, 6, 8, 3, 9, 7]
    print(list_)
    print("maximum value", max(list_))
    lista = list_.copy()
    lista.remove(max(lista))
    print("second maximum value", max(lista))
    print()
    
    # find duplicates
    print(mythical)
    duplicate = []
    for element in mythical:
        if element in duplicate:
            continue 
        if mythical.count(element) == 2:
            print("Duplicates in list: ", element)
            duplicate.append(element)
    
    # find unique values
    print("Unique elements in list: ", end="")
    for element in mythical:
        if mythical.count(element) == 1:
            print(element + " ", end="")
    print('\n')
    
    # converting to list
    print("CONVERTING TO LIST")
    string = "Braveheart"
    print(string)
    lista = list(string)
    print(lista)
    lista.append('s')
    print(lista)
    print("".join(lista))
    print()
    
    # finding max and min
    print("Finding MAX AND MIN VALUES IN A LIST")
    print(numbers)
    print("Maximum value: ", max(numbers))
    print("Minimum value: ", min(numbers))
    print(mythical)
    print("Maximum value: ", max(mythical))
    print("Minimum value: ", min(mythical)) 
    print()
    
    # printing elements in list with format
    print("PRINTING LIST WITH FORMAT")
    print(mythical)
    print(set(mythical))
    print("The mythical animals are: {} and {} also {} why not? {} mmm, ah {} finally {}".format(*mythical))
    print()
    
    # reversing a list with for
    print("REVERSING A LIST WITH FOR")
    print(mythical)
    for i in range(len(mythical)-1, -1, -1):
        print(mythical[i])
    print()
    
    # initializing list with range and other ways
    print("INITIALIZING LIST WITH RANGE AND OTHER WAYS")
    list_even = list(range(0, 10, 2))
    list_odd = list(range(1, 10, 2))
    print(list_even)
    print(list_odd)
    list_new_for = [i**2 for i in range(10)]
    print(list_new_for)
    print()
list_()


def tuple_():
    # initializing tuple
    print("INITIALIZING TUPLE")
    months = ('January', 'February', "March", "April", "May", "June", "July", 'August', 'September', 'October', 'November', 'December')
    print(months)
    baroque = ("vivaldi",)
    print("tuple of one item", baroque)
    print()
    
    # Adding tuples to a list
    print("ADDING TUPLES TO A LIST")
    list_tuple = [('January', 30), ('February', 28), ('March', 31), ('April', 30), ('May', 31), ('June', 30), ('July', 31), ('August', 30)]
    print(list_tuple[2][0])
    for i in range(len(list_tuple)):
        print(list_tuple[i][1])
    print("{}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n".format(*list_tuple))
    
    # Adding data to tuples
    print("CONCATENATING OTHER TUPLE TO A TUPLE")
    months = months + ("January", "March")
    print(months)
    meses = months, ("January", "March")
    print(meses)
    print()
    
    # Sorting tuples
    print("SORTING TUPLES")
    print(sorted(months))
    print(sorted(months, reverse=True))
    print(months)
    print()
    
    # Tubples in for loop
    for month in months:
        print(month)
    print()
        
    if "August" in months:
        print("Found August!\n")
    # Finding duplicates in tuple
    duplicate = []
    for month in months:
        if month in duplicate:
            continue
        if months.count(month) == 2:
            print(month)
            duplicate.append(month)
    print()
    
    # Otehr methods
    print("OTHER METHODS")
    num_tuple = (0, 1, 2, 3, 4, 5)
    print(num_tuple.index(3))
    print()
    
    # Max and min
    print("MAX AND MIN WIHT TUPLES")
    print(max(num_tuple))
    print(min(num_tuple))
    print()
    
    # slicing tuples
    print("SLICING TUPLES")
    print(num_tuple[1:3])
    print()
    
    # converting list to tubles and viceversa
    lista = ['a', 'b', 'c', 'd', 'e', 'f', 'f']
    tuple_2 = tuple(lista)
    print(tuple_2)
    lista_2 = list(tuple_2)
    print(lista_2)
    print()
    
    # packing and unpacking
    print("PACKING AND UNPACKING TUPLE")
    tuple_packed = ("final fantasy", "Ronin", "333")
    (game, movie, beautiful_num) = tuple_packed
    print(tuple_packed)
    print("game: {}, movie: {}, beautiful number: {}".format(game, movie, beautiful_num))
    print()
tuple_()

    
def dictionary_():
    # initializing dictionary
    print("INITIALIZING DICTIONARY")
    dict_car = {
                'name' : "Carlitos", 
                'age' : 5, 
                'hobby' : "build legos", 
                'likes' : "Cars", 
                'color' : "blue", 
                'movies' : ["Aladdin", "paw-petrol", "lion king"], 
                'superheroes' : ("spiderman", "batman", "superman")
                }
    print(dict_car)
    
    for key, value in dict_car.items():
        if key == "movies" or key == "superheroes":
            print("{} : ".format(key))
            for i in range(3):
                print("\t{}".format(value[i]))
        else:
            print("{} : {}".format(key, value))
            
    dict1 = {
             'num1' : 23, 
             'num2' : 54, 
             'num3' : 78, 
             'num4' : 89, 
             'num5' : 98,
             'num6' : 23,
             'num7' : 23,
             }
    dict2 = {
             'movie1' : "Ronin", 
             'movie2' : "As good as it gets", 
             'movie3' : "Scott vs World", 
             'movie4' : "Donnie Brasco", 
             'movie5' : "the Fugitive"
             }
    dict3 = {'month1' : "March", 
             'month2' : "August", 
             'month3' : "October", 
             'month4' : "December"
             }
    dict4 = {'music1' : "Baroque", 
             'music2' : "Tango", 
             'music3' : "Salsa"
             }
    dict5 = {'book1' : "mitos y leyendas del mundo", 
             'book2' : "una voz en la noche", 
             'book3' : "el juego de Gerald"
             }
    main_dict = {
                 'numbers': dict1,
                 'movies': dict2,
                 'months': dict3,
                 'music': dict4,
                 'books': dict5}
    for key, value in main_dict.items():
        print("{} : ".format(key))
        for dict_key, dict_value in value.items():
            print("\t{} : {}".format(dict_key, dict_value))
    print()        
    
    # accessing dictionaries
    print("ACCESSION DICTIONARY")
    print(dict_car.keys())
    print(dict_car.values())
    print("accession name index: ", dict_car["name"])
    print(dict_car.get("name"))
    print(main_dict["books"])
    print(main_dict.values())
    print(main_dict["music"]["music1"])
    print()
    
    # adding values
    print("ADDING TO DICTIONARY")
    dict_car["instrument"] = "violin"
    print(dict_car)
    print()
    
    # copyng dictionary
    print("COPYING DICTIONARIES")
    dict_ = dict()
    dict_ = dict_car.copy()
    print(dict_)
    print()
    
    # removing elements in a dictionary
    print("REMOVING ELEMENTS FROM DICTIONARY")
    print(dict_car.pop("superheroes"))
    print(dict_car)
    del dict_car['instrument']
    print(dict_car)
    dict_.clear()
    print(dict_)
    print()
    
    # update dictionary
    print("EDIT DICTIONARY")
    dict_car["name"] = "Carlitos Quiroz"
    print(dict_car)
    print()
    
    # sort dict
    print("SORT DICTIONARY")
    for key in sorted(main_dict.keys()):
        print("{} : {}".format(key, main_dict[key]))
        
    print()
    for key, value in sorted(main_dict.items()):
        print("{} :".format(key))
        for kval, vval in sorted(value.items()):
            print("\t{}".format(str(vval)))
        
    print()
    
    # count on dict
    print("COUNT ON DICT")
    
    #sum numbers dict from main_dict
    total = 0
    for keys, values in main_dict.items():
        for kval, vval in values.items():
            if vval != str(vval):
                total += vval
                print(vval, "is a number")
    print("The total value of the numbers dictionary within the main_dict is : ", total)
    
    # counting the frequencies of chars from a text and save it in a dictionary
    print("COUNTING FREQUENCIES FROM A LONG STRING")
    text = "A list is a data structure that holds an ordered collection of items for example you can store a sequence of items in a list. This is easy to imagine if you can think of a shopping list where you have a list of items to buy, except that you probably have each item on a separate line in your shopping list whereas in Python you put commas in between them"
    dupchars = []
    dict_ = dict()
    for i in range(len(text)):
        if text[i] in dupchars:
            continue
        dict_[text[i]] = text.count(text[i])
        dupchars.append(text[i])
    
    for key, value in dict_.items():
        print("{} : {}".format(key, value))
    print()
    
    # counting the frequencies of chars from a file
    print("COUNTING FREQUENCIES FROM A FILE")
    text_f = open("C:/Users/Solrac/workspace/Python.Development/src/test.txt")
    text_list = text_f.readlines()
    text_ = "".join(text_list)
    duplicates = list()
    dictionary = dict()
    for i in range(len(text_)):
        if text_[i] in duplicates:
            continue
        if (text_[i] == 'n') and (text_[i-1] == '\\'):
            continue
        dictionary[text_[i]] = text_.count(text_[i])
        duplicates.append(text_[i])
         
    for key, value in dictionary.items():
        print("{} : {}".format(key, value))
    print()
        
    # print unique values in a dictionary using set
    set_ = set()
    for key, value in main_dict.items():
        for kval, vval in value.items():
            if vval != str(vval):
                set_.add(vval)
    for set_element in set_:
        print("{} ".format(set_element))
    print()
    
dictionary_()

def set_():
    #initialize a set
    print("INITIALIZE A SET")
    set1 = set()
    set2 = {"cherry", "blueberry", "rasperry"}
    print(set2)
    set1 = set2.copy()
    print(set1)
    print()
    
    # add elements to set
    print("ADD ELEMENTS TO SET")
    set1.add("mango")
    set1.add("strawberry")
    set1.add("blueberry")
    set1.add("papaya")
    print(set1)
    set3 = {"orange", "melon"}
    set1.update(set3)
    set1.update(["pear", "prune"])
    print(set1)
    
    # access elements in a set
    print("ACCESS A SET")
    for fruit in set1:
        print(fruit)
    print()
    
    # length of a set
    print("LENGTH OF A SET")
    print(len(set1))
    print()
    
    # remove elements from a set
    print("REMOVE ELEMENTS FROM A SET")
    print(set1)
    set1.remove('cherry')
    print(set1)
    set2.clear()
    print(set2)
    set2.add("kiwi")
    set2.add('banana')
    print(set2)
    set2.discard("banana")
    print(set2)
    print(set1)
    print("removing the last item: ", set1.pop())
    print(set1)
    del set2
    print()
    
    # join two sets
    print("JOIN TWO SETS")
    set2 = ['banana', 'kiwi', 'passion fruit']
    set4 = set1.union(set2)
    print(set4)
    print()
    
    # intersection
    print("INTERSECTION BETWEEN TWO SETS")
    print("set1: ",set1)
    set2 = set(set2)
    print("set2: ",set2)
    print("set4: ",set4)
    print("intersection betw set1 and set2", set1.intersection(set2)) # creates a new set
    print("intersection betw set1 and set4", set1.intersection(set4))
    print("intersection betw set2 and set4", set2.intersection(set4))
    set4.intersection_update(set2) # this changes set4
    print("intersection update", set4) # set4 now has only the common elements between the two sets
    print()
    
    # difference
    print("DIFFERENCE BETWEEN TWO SETS")
    print("set1: ",set1)
    print("set2: ",set2)
    set4.add("car")
    set4.add("movie")
    set4.add('book')
    print("set4: ",set4)
    print("difference set1 and set2", set1.difference(set2))
    print("difference set2 and set1", set2.difference(set1))
    print("difference set2 and set4", set2.difference(set4)) # all gets removed because all the elements in set2 are contained in set4
    print("difference set4 and set2", set4.difference(set2)) # shows only the different elements, it removes the common
    set4.difference_update(set2)
    print(set4)
    print()
    
    # showing if two sets have intersection or not
    print("CHECKS IF TWO SETS HAVE INTERSECTION")
    print("set2", set2)
    print("set4", set4)
    print("are set2 and set4 different (no intersection)?", set4.isdisjoint(set2))
    set4.add("kiwi")
    print("set4", set4)
    print("are set2 and set4 different (no intersection)?", set4.isdisjoint(set2))
    
    # showing if two sets are subsets of each other (BOOLEAN)
    print("CHECKS IF TWO SETS ARE SUPERSET OR SUBSET")
    print("set2", set2)
    print("set4", set4)
    set6 = {'kiwi'}
    print("set6", set6)
    print("are set2 and set4 subset of each other?", set4.issuperset(set2))
    print("is set2 a superset of set6?", set2.issuperset(set6))
    print("is set6 a superset of set2?", set6.issuperset(set2))
    print("is set6 a subset of set2?", set6.issubset(set2))
    print()
    
    # showing symetric difference
    print("CHECKS FOR SYMETRIC DIFFERENCE")
    print("set2", set2)
    print("set4", set4)
    print("set6", set6)
    print("Showing the different items in the set2 and set4 (removes the common elements btw the two sets)", set2.symmetric_difference(set4))
    print("Showing and updating the different items in the set2 and set4 (removes the common elements btw the two sets)", set2.symmetric_difference_update(set4))
    print("set2", set2)
    print("set4", set4)
set_()

def references():
    print("REFERENCES")
    list1_ = [1, 2, 3 ,4, 5]
    list2_ = list1_
    list3_ = list1_[:]
    list_4 = list1_.copy()
    print(list1_)
    print(list2_)
    print(list3_)
    print(list_4)
    list1_.remove(4)
    print("removed 4 from list1")
    print(list1_)
    print(list2_)
    print(list3_)
    print(list_4)
references()

def string_manipulation():
    s = "swaroop"
    if s.startswith('s'):
        print("found 's' in", s)
    if s.endswith('p'):
        print("found 'p' in", s)
    if 'r' in s:
        print("found 'r' in", s)
    print("found 'oo' in",s, "at", s.find('oo'))
    if s.find('x') == -1:
        print("could not find 'x' in", s)
    if s.find('w') != -1:
        print("found 'w' in", s)
    print("found the first o in", s, "at", s.find('o'))
    print("The first 'o' in", s, "is found at", s.find('o'), "the second 'o' is at", s.rfind('o'))
    print("another way to find the second 'o'", s.rindex('o'))
    list_ = list(s) 
    print(list_)
    s2 = "Cute Naomi chula"
    print("/".join(s2))
    print(s2.split("/"))
    print(s2.swapcase())
    print(s2)
    print("splitting string from front", s2.split(" ", 1))
    print("splitting string from back", s2.rsplit(" ", 1))
    print("split all", s2.split(" "))
    
    print()
    s1 = "El cArLiToS quiroz es guaperrimo"
    print(s1)
    list_chars = list(s1)
    print(list_chars)
    list_words1 = s1.split(" ", 1)
    list_words2 = s1.rsplit(" ", 2)
    print(list_words1)
    print(list_words2)
    list_words = s1.split(" ")
    list_words[1] = list_words[1].swapcase()
    list_words[2] = list_words[2].title()
    list_words[len(list_words)-1] = list_words[len(list_words)-1].upper() 
    print(list_words)
    list_words[1] = list_words[1].swapcase()
    s1 = " ".join(list_words)
    print(s1)
    print("The first 'r' in {} can be fount at {} (the same {}). The last r is located at {} (or at {})".format(s1, s1.find('r'), s1.index('r'), s1.rfind('r'), s1.rindex('r')))
    if 'R' in s1:
        print("'R' was founr in", s1)
    if s1.startswith('E'):
        print("'{}' starts with 'E'".format(s1))
    if s1.endswith('O'): 
        print("'{}' ends with 'O'".format(s1))
    print(s1.capitalize())
    print(s1.casefold())
    print(s1.upper())
    print(s1.lower())
    
    if s1.isalnum():
        print("{} is alphanumeric".format(s1))

    s5 = "test"
    if s5.isalpha():
        print("{} is alpha".format(s5))
    else:
        print("is not")

    num = "133453"
    if num.isnumeric():
        print("{} is numeric string".format(num))
        
    if s1.islower():
        print("all lower cases in",s1)
    else:
        print("not all lower in",s1)
     
    s1 = s1.lower()
    if s1.islower():
        print("all lower cases in",s1)
    
    print(s1.partition(" "))
    
    print(s1.replace('carlitos', 'CaloBeto', 3))
    
    print(s1.splitlines(0 ))
    
string_manipulation()