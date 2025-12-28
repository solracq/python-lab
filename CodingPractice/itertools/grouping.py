'''
@author: Solrac
'''
import itertools

data = ['a', 'b', 'a', 'a', 'c', 'd', 'b', 'g', 'f', 'c']

unique_keys = []
groups = []
sorted_data = sorted(data)

for key, group in itertools.groupby(sorted_data):
    unique_keys.append(key)
    groups.append(list(group))
    
print('original data', data)
print('sorted data',sorted_data)
print('keys',unique_keys)
print('groups',groups)