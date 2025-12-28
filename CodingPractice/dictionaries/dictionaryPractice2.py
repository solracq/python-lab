'''
@author: Solrac
'''
from A_set import set_
from sys import set_asyncgen_hooks
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

list_ = ["Voldo", "Valeria", "Connan", "warnerious", "CptCrunch"]
tuple_ = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
dict_ = {"American": 'Tesla', "German": 'BMW', "Italian": 'Ferrari', "French": 'Renault'}
dictionary_ = {'a':'c', 'b':"Test", 'c': 333, 'd': list_, 'e': tuple_, 'f': dict_}

print(dictionary_,"\n")
for letter in dictionary_:
    if letter == 'f':
        for subletter in dict_:
            print("subKey:{}  subValue:{}".format(subletter, dictionary_['f'][subletter]))
    else:
        print("key:{}\tvalue: {}".format(letter, dictionary_[letter]))
    
print()
print(dictionary_.keys())

# Add
dict1= {1: "american werewolf in london", 2: "IT", 3: "sleepwalkers"}
dictionary_["new_item"]= dict1
for item in dictionary_:
    print("{}\t{}".format(item, dictionary_[item]))
print()

# Remove
del dictionary_["a"]
print(dictionary_)

# Edit
dictionary_['c'] = {'c1': "Ronin", 'c2': "Pillgrim", 'c3': "As good as it gets", 'c4': "Sideways"}
for item in dictionary_:
    print("{}\t{}".format(item, dictionary_[item]))
print()

print("Printing full dictionary")
for letter in dictionary_:
    print(letter)
    if letter == 'c':
        for key,value in dictionary_['c'].items():
            print("{} :\t{}".format(key,value))
    if letter == 'f':
        for key,value in dict_.items():
            print("{} : \t{}".format(key,value))
    if letter == "new_item":
        for key,value in dict1.items():
            print("{} : \t{}".format(key,value))
print()

alien= {'xPosition': 0, 'yPosition': 25, 'speed': 'medium'}
print(alien)
def calculate():
    if alien['speed'] == 'low':
        alien['xPosition'] += 1
    elif alien['speed'] == 'medium':
        alien['xPosition'] += 2
    else:
        alien['xPosition'] += 3
    print(alien)
calculate()
alien['speed']='fast'
calculate()

fav_lan={
         "Lupita": 'python',
         "Carlos": 'python',
         "Naomi":  'scratch',
         "Carlitos": 'scratch',
         "Yu": 'python',
         "Carlos": 'java',
         }
for key, value in fav_lan.items():
    print(key + " : "+ value)
print()
print("Yu favorite language is {}".format(fav_lan["Yu"].title()))

leoP = {
        'name': 'leo',
        'last': 'palestino',
        'age': 38,
        'occupation': 'something',
        'city': 'puebla',
        'friend': True,
        }
leoP["University"] = "udlap"
del leoP["friend"]
# looping using keys
for element in leoP:
    print("{} : {}".format(element, leoP[element]))
print()

print("Printing by keys only")
for name in fav_lan.keys():  # the .keys() is optional
    print(name.title())
print()

# looping using keys and values
for key,value in leoP.items():
    print(key.upper()," : ", value)
print()

if 'Erin' not in fav_lan.keys():
    print("Erin please choose a languae to be included in the list")

if 'java' in fav_lan.values():
    print("do not forget java")

# Sorting when printing dictionaries
for name in sorted(fav_lan):
    print(name)

for name,value in sorted(fav_lan.items()):
    print("{} : {}".format(name, value))
print()

# looping using Values
for value in fav_lan.values():
    print(value)
print()

for value in sorted(fav_lan.values()):
    print(value)
print()

# converting to set to print unique values
set_ = set()
for value in sorted(fav_lan.values()):
    set_.add(value)
for valueSet in set_:
    print(valueSet)

print()
for unique_values in set(sorted(fav_lan.values())):
    print(unique_values) 
print()

for uniquekey, uniquevalue in set(sorted(fav_lan.items())):
    print("{} : {}".format(uniquekey, uniquevalue))

print(fav_lan)  # dictionary can only include unique keys

rivers={'nile': 'egypt', 'niagara': 'canada', 'itaka': 'mexico'}

rivers["river"]='italy'

for key, value in rivers.items():
    print("The {} runs through {}".format(key.capitalize(), value.capitalize()))
print()

del rivers["river"]
for key in sorted(rivers.keys()):
    print(key)
print()

for value in sorted(rivers.values()):
    print(value)
print()

# More about nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print()

for alien in range(30):
    new_alien = {'color': 'blue', 'points': '20', 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print()

print("Number of aliens:", len(aliens))

for alien in aliens[2:8]:
    if alien['color'] == 'blue':
        alien['color'] = 'violet'
        alien['points'] = 25
        alien['speed'] = 'medium'
        
for alien in aliens[20:29]:
    if alien['color'] == 'blue':
        alien['color'] = 'pink'
        alien['points'] = 30
        alien['speed'] = 'fast'

for alien in aliens[0:10]:
    print(alien)
print()

pizza= {
        'crust': 'thick',
        'toppings': ['mushrums', 'extra cheese'], 
        }

for key, value in pizza.items():
    print("{} : {}".format(key, value))
    
print()

fav_lan2 = {
            'jen': ['python', 'ruby'],
            'sarah': ['c'],
            'edward': ['ruby', 'go'],
            'phil': ['python', 'java'],
            }

for names, languages in fav_lan2.items():
    if len(languages) < 2:
        print("{}'s favorite language is : ".format(names.capitalize()))
    else:
        print("{}'s favorite languages are : ".format(names.capitalize()))
    for language in languages:
        print("\t{}".format(language.title()))
print()

users = {
         'aeinstein':{
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
            },
         'mcurie':{
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
            },
         }

for username, userinfo in users.items():
    print(username)
    full_name = userinfo['first'] + " " + userinfo["last"]
    location = userinfo['location']
    print(full_name.title())
    print(location,"\n")
print()    

users= {
        'cquiroz': {
            'name': "carlos",
            'second_name': "alberto",
            'last_name': "quiroz",
            'title': "test auto dev",
            'books': "a voice in the night",
            'movie': "ronin",
            },
        'yzhang': {
            'name': "yu",
            'second_name': "",
            'last_name': "zhang",
            'title': "acct",
            'books': "any",
            'movie': "as good as it gets",
            },
        'carlitosq': {
            'name': 'carlitos',
            'second_name': 'eddy',
            'last_name': 'quiroz',
            'title': "engineer",
            'books': "dinosaurs",
            'movie': "aladdin",         
            },
        'nquroz': {
            'name': 'naomi',
            'second_name': 'sophia',
            'last_name': 'quiroz',
            'title': "engineer and more",
            'books': "princess",
            'movie': "minnie mouse", 
            },
        }

for username, userinfo in users.items():
    print("username: {} ".format(username))
    full_name = userinfo['name'] + " " + userinfo['second_name'] + " " + userinfo['last_name']
    print("\tfull name: {}".format(full_name.title()))
    print("\ttitle: {}".format(userinfo['title']))
    print("\tbooks: {}".format(userinfo['books']))
    print("\tmovie: {}".format(userinfo['movie']))
print()

for username, userinfo in users.items():
    # finding specific data
    if userinfo['last_name'] == 'quiroz':
        print("{} lastname found with name {}".format(userinfo['last_name'], userinfo['name']))
print()