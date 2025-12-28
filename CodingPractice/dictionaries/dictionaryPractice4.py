'''
@author: Solrac
'''
# D I C T I O N A R Y
dict_ = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
keys_ = list(dict_.keys())
print('Accessing keys')
print(keys_[2])
print()
print(dict_)
dict_.update({'C': 'abc'})
print(dict_)
dict_.update({'D': 'def'})
print(dict_)
print('Accessing keys again')
listak = list(dict_.keys()) 
listav = list(dict_.values())
print(listak[3], 'corresponds', listav[3])
print(sorted(listav))
# Sparating sorted keys and values to individual lists
list_sorted_values = sorted(dict_.items(), key=lambda x: x[1])
print(list_sorted_values)
list_k = []
list_v = []
for i in range(len(list_sorted_values)):
    k_, v_ = list_sorted_values[i]
    list_k.append(k_)
    list_v.append(v_)
print(list_k)
print(list_v,'\n')

lista = [
         {
          'Abc': {
                     '50_movie': 'Rebel w/o Cause',
                     '60_movie': 'The Graduate',
                     '70_movie': 'The Godfather',
                    },
          'cd': {
                      '50_music': 'Run away Sue',
                      '60_music': 'Apache',
                      '70_music': 'Dont let me be misunderstood',
                      },
           'asdf':  {
                      'chocolate1': '3 Musketers',
                      'gum': 'beisbol bubble gum',
                      'song': 'seven up',
                      },
          },
         {
          'dsa': {
                     '80_movie': 'asdf',
                     '90_movie': 'fasdd',
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
    keys = list(dict_.keys())
    if '00_movie' in dict_[keys[0]]:
        print("{} : {}".format(keys[0], dict_[keys[0]]['00_movie']))
print()

print("Printing only avc' 90 movie")
for dict_ in lista:
    for key, value in dict_.items():
        if key == 'abc':
            for k, v in value.items():
                if k == '90_movie':
                    print("{}: {} : {}".format(key, k, v)) 
print()

# find all 60's songs
print("Printing only 60's songs")
for dict_ in lista:
    for key, value in dict_.items():
        for k, v in value.items():
            if k == '60_music':
                print("{} : {} : {}".format(key, k, v))
print()

# Find items in the list_songs
print("Printing in the list_songs")
list_songs = ['Rock Dj', 'let it go', 'The Godfather']
for dict_ in lista:
    for key, value in dict_.items():
        for k, v in value.items():
            if v in list_songs:
                print("Found= {} : {} : {}".format(key, k, v))
print()

# Order value Items
print("Print all dictionaries in order of the latest values")
for dict_ in lista:
    for key, value in dict_.items():
        print("{}:".format(key))
        for k, v in sorted(value.items(), key=lambda x: x[1], reverse=True):
            print("    {} : {}".format(k, v))
print()

users= [
        {'uname': {
            'name': "test",
            'second_name': "Ba",
            'last_name': "cl",
            'title': "eng",
            'books': "any",
            'movie': "as good as it gets",
            }},
        {'uname': {
            'name': "aaa",
            'second_name': "asdf",
            'last_name': "ad",
            'title': "acct",
            'books': "any",
            'movie': "as good as it gets",
            }},
        {'uname': {
            'name': 'ab',
            'second_name': 'fsadf',
            'last_name': 'abc',
            'title': "eadfeer",
            'books': "dinods",
            'movie': "aladdin",         
            }},
        {'uname': {
            'name': 'ase',
            'second_name': 'sads',
            'last_name': 'asdfaf',
            'title': "engineer and more",
            'books': "princess",
            'movie': "minnie mouse", 
            }}
    ]

users2 = [{'a': 1, 'b': 'z'}, {'a': 2, 'b': 'x'}, {'a':3, 'b': 'y'}]
# List comprehension
print('LIST COMPREHENSION')
lista = [list(dict_.keys()) for dict_ in users]
print(lista)
print()
print([dict_['a'] for dict_ in users2])
print([dict_['uname']['name'] for dict_ in users if dict_['uname']['last_name'] == 'abc'])
print()

# Dicionary comprehension
print("DICTIONARY COMPREHENSION")
dictionary = {dict_.values() for dict_ in users}
print(dictionary)
print()
print({dict_['uname']['name'] : dict_['uname']['second_name'] for dict_ in users})
