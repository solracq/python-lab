'''
@author: Solrac
'''
import json

def manipulating_json():
    s = "Testing is very dupper fun"
    dict_ = {s[i] : s.count(s[i]) for i in range(len(s))}
    
    # convert dictionary to JSON
    json_string = json.dumps(dict_, indent = 4, sort_keys = True)
    print(json_string)
    
    dictionary = {
                  "name": 'John',
                  'age': 30,
                  'likes': 'books',
                  'pets': None,
                  'cars': [
                           {"make": "BMW", 'mpg': 30.5},
                           {'make': 'Mercedes', 'mpg': 28.5},
                           {'make': 'Audi', 'mpg': 29.3},
                           ],
                  }
    
    car_dict = json.dumps(dictionary, indent = 4, sort_keys = True)
    
    newFile = open("config.json", 'w')
    newFile.write(car_dict)
    newFile.close()
    
    # convert json data to dictionary
    with open("config.json") as json_object:
        dictionary_ = json.load(json_object)
    print('Parsing json file to dictionary:', dictionary_)

    for key, value in sorted(dict_.items(), key=lambda x: x[1]):
        print("{} : {}".format(key, value))
    
manipulating_json()
