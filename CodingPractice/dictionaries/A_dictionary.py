'''
@author: Solrac
'''
import random

def filling_up_dict():
    dictionary = {}
    res = "n"
    res = input("do you want to start?")
    while res == "y":
        key = input("favorite zodiac knight? ")
        value = input("power level? ")
        dictionary[key] = value
        res = input("Do you want to add more? ")
    print(dictionary)

def calculate(alien:dict):
    if alien['speed'] == 'low':
        alien["xPosition"] += 1
    elif alien['speed'] == 'medium':
        alien["xPosition"] += 2
    else:
        alien["xPosition"] += 3
        alien["yPosition"] += 3
    print(alien)

# Passing multiple args of unknown number
def print_elements(*kwargs):
    return print(kwargs)

def print_dict(dictionary:dict):
    for key, value in dictionary.items():
        print(f"{key}:")
        for k, v in value.items():
            print(f"\t{k} : {v}")

def sort_dict(dictionary:dict, reverse:bool):
    if reverse:
        for key, value in sorted(dictionary.items(), reverse=True):
            print(f"{key}:")
            for k, v in sorted(value.items(), reverse= True):
                print(f"\t{k} : {v}")
    else:
        for key, value in sorted(dictionary.items()):
            print(f"{key}:")
            for k, v in sorted(value.items()):
                print(f"\t{k} : {v}")

def sort_dict_values(dictionary:dict):
    for key, value in dictionary.items():
        print(f"{key}")
        for k, v in sorted(value.items(), key=lambda x: x[1]):
            print(f"\t{k} : {v}")

def get_char_frequency(text:str):
    array = list(text)
    dictionary = {}
    for i in range(len(array)):
        dictionary[array[i]] = text.count(array[i])
    return dictionary

def are_dicts_equals(dict1:dict, dict2:dict):
    if len(dict1) != len(dict2):
        print("Not equals due to dict diff size")
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    values1 = list(dict1.values())
    values2 = list(dict2.values())
    if keys1 != keys2:
        print("Not equals due to dict diff KEYS")
    elif values1 != values2:
        print("Not equals due to dict diff VALUES")
    else:
        print("Dictionaries are equal!")

if __name__ == "__main__":
    # filling_up_dict()
    phonebook = {"sadf": 1234567, "abc": 7654321, "adsf": 9876543, "dsfaar": 33323567}
    print(phonebook)
    print(list(phonebook.keys()))
    print(list(phonebook.values()))
    print(phonebook["Nom"])
    phonebook["Car"] = 2269334899
    print(phonebook)
    phonebook["Carmelit"] = 529297242
    for key, value in phonebook.items():
        print(f"{key}:{value}")
    print(phonebook.popitem())
    print(phonebook)
    phonebook["Carmelit"] = 529297242
    print(phonebook)
    phonebook.pop("abc")
    print(phonebook.get("Cedar"))
    print(len(phonebook))
    for element in phonebook:
        print(f"{element} : {phonebook[element]}")
    phonebook["Conan"] = 12123333
    print(phonebook)
    del phonebook["Conan"]
    print(phonebook)
    array = [("test", 1), ("testing", 2), ("qa", 3), ("testa", 4)]
    dictionary = dict(array)
    print(dictionary)
    print(f"min key = {min(dictionary)}")
    print(f"max key = {max(dictionary)}")
    print(f"min value = {min(list(dictionary.values()))}")
    print(f"max value = {max(list(dictionary.values()))}")
    car_list = ["Voldo", "Valeria", "Connan", "warnerious", "CptCrunch"]
    month_tuple = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
    "December")
    car_brands_dict = {"American": 'Tesla', "German": 'BMW', "Italian": 'Ferrari', "French": 'Renault'}
    dictionary = {"cars": car_list, "months": month_tuple, "car_brands": car_brands_dict}
    for key, value in dictionary.items():
        if type(value) is dict:
            print(f"{key}: ")
            for k, v in value.items():
                print(f"\t\t{k} : {v}")
        else:
            print(f"{key} : {value}")
    alien = {'xPosition': 0, 'yPosition': 25, 'speed': 'medium'}
    print(alien)
    calculate(alien)
    alien['speed'] = 'fast'
    calculate(alien)
    for value in alien.values():
        print(value)
    if 'fast' in alien.values():
        print("way to fast!")
    if 'speed' in alien.keys():
        print("you can change speed!")
    phonebook = {"Nom": 1234567, "abc": 7654321, "dsaf": 9876543, "adsf": 33323567, "dsfcy": 53764357}
    print(phonebook)
    for key, value in sorted(phonebook.items()):
        print(f"{key} : {value}")
    print("//////////////////////////////")
    for key, value in sorted(phonebook.items(), reverse=True):
        print(f"{key} : {value}")
    fav_lan = {
        "abc": 'python',
        "efg": 'python',
        "hij": 'scratch',
        "klm": 'scratch',
        "nmo": 'python',
        "Pqrs": 'java',
    }
    print(fav_lan)
    set_fav_lan = set(fav_lan.items())
    print(set_fav_lan)
    for key, value in sorted(set(fav_lan.items())):
        print(f"{key} : {value}")

    test0 = {'title': 'green', 'status': 'pass'}
    test1 = {'title': 'yellow', 'status': 'fail'}
    test2 = {'title': 'red', 'status': "pass"}
    test_suite = [test0, test1, test2]
    tc = []
    for test in test_suite:
        for key, value in test.items():
            if value == 'fail':
                tc.append(test['title'])
    print(f"The failed test cases were: {tc}")
    print_elements('a')
    print_elements('a', 'b', 'c')
    print_elements('a', 'b', 'c', 1, 2, 3)
    fav_lan = {
        "adsf": 'python',
        "qer": 'python',
        "uyj": 'scratch',
        "asde": 'scratch',
        "Ycz": 'python',
        "Cdffs": 'java',
    }
    print(sorted(fav_lan.items()))
    # sorting based on values of a list
    print(sorted(fav_lan.items(), key=lambda x: x[1]))
    ####################################################################################################
    s = "abc and abc are very super duper cute"
    list_num = [random.randint(10, 90) for i in range(10)]
    list_words = ['kiwi', 'banana', 'strawberry', 'orange', 'blueberry', 'mango', 'pear', 'apple', 'rasperry', 'melon',
                  'papaya', 'watermelon']
    tuple_months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December')
    set_colors = {'blue', 'red', 'green', 'purple', 'orange', 'black', 'white', 'grey', 'yellow', 'magenta', 'pink',
                  'brown'}
    dictionary = {
        "solrac": {
            'name': 'CaloBeto',
            'number': list_num[3],
            'month': tuple_months[7],
            'fruit': list_words[2],
            'color': 'blue',
            'likes': 'cars',
            'hobbies': 'soccer',
            'movies': 'Aladdin',
        },
        "nquiroz": {
            'name': 'Abc test',
            'number': list_num[5],
            'month': tuple_months[3],
            'fruit': list_words[1],
            'color': 'pink',
            'likes': 'baby braqui',
            'hobbies': 'singing',
            'movies': 'princess movies',
        },
        "abc": {
            'name': 'Av',
            'number': list_num[random.randint(0, 9)],
            'month': tuple_months[9],
            'fruit': list_words[5],
            'color': 'purple',
            'likes': 'shopping',
            'hobbies': 'cooking',
            'movies': 'As good as it gets',
        },
    }
    data_structure_dict = {'string': s,
                           'list_num': list_num,
                           'list_words': list_words,
                           'tuple': tuple_months,
                           'set': set_colors,
                           'dictionary': dictionary,
                           }
    print("***********************************************")
    print(data_structure_dict)
    print(data_structure_dict["tuple"])
    print(data_structure_dict["dictionary"]["yuyis"]["movies"])
    print_dict(dictionary)
    print("Sort dict:")
    sort_dict(dictionary, reverse=False)
    print("Reverse dict:")
    sort_dict(dictionary, reverse=True)
    print("Sort values of a dict")
    dictionary = {
        "solrac": {
            'name': 'CaloBeto',
            'month': tuple_months[7],
            'fruit': list_words[2],
            'color': 'blue',
            'likes': 'cars',
            'hobbies': 'soccer',
            'movies': 'Aladdin',
        },
        "nquiroz": {
            'name': 'Abc Efg',
            'month': tuple_months[3],
            'fruit': list_words[1],
            'color': 'pink',
            'likes': 'baby braqui',
            'hobbies': 'singing',
            'movies': 'princess movies',
        },
        "abc": {
            'name': 'ab',
            'month': tuple_months[9],
            'fruit': list_words[5],
            'color': 'purple',
            'likes': 'shopping',
            'hobbies': 'cooking',
            'movies': 'As good as it gets',
        },
    }
    sort_dict_values(dictionary)
    text = "A list is a data structure that holds an ordered collection of items for example you can store a sequence " \
           "of items in a list. This is easy to imagine if you can think of a shopping list where you have a list of " \
           "items to buy, except that you probably have each item on a separate line in your shopping list whereas in " \
           "Python you put commas in between them"
    print(text)
    print(get_char_frequency(text))
    dict_a = {"a": "hola",
              "b": 123456,
              "c": ['a', 'b', 'c'],
              }
    dict_b = dict_a.copy()
    print(dict_b)
    dict_b.update({"b": 123456})
    print(dict_b)
    if dict_a == dict_b: # Only works when numbers in values
        print("dict_a and dict_b are equal")
    else:
        print("dict_a and dict_b are NOT equal")
    dict_a = {"a": "hola",
              "b": 123456,
              "c": ['a', 'b', 'c'],
              }
    dict_b = {"a": "hola",
              "b": 123456,
              "c": ['a', 'b', 'c'],
              }
    are_dicts_equals(dict_a, dict_b)
#########################################################
    file_logs = "../logs/logs.txt"
    with open(file_logs) as file_obj:
        content_list = file_obj.readlines()
        content_text = "".join(content_list)

    duplicates = []
    dictionary = {}
    for i in range(len(content_text)):
        if content_text[i] == 'n' and content_text[i - 1] == '\\':
            continue
        if content_text[i] == ' ' or content_text == '  ':
            continue
        if content_text[i] == '6/23/2019' or content_text[i] == '0:33:33.':
            continue
        dictionary[content_text[i]] = content_text.count(content_text[i])

    print(content_text)
    print(sorted(dictionary.items(), key=lambda x: x[1]))
