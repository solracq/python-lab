'''
@author: Solrac
'''
import random

def search_key(array, key):
    for i in range(10):
        if key == array[i]:
            return array.index(array[i])
    return -1

array = []
for i in range(10):
    array.append(random.randint(10,90))

print(array)

key = int(input("Type number to search for?"))
print(search_key(array, key))