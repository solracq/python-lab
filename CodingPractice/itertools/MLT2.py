'''
@author: Solrac
'''
from itertools import combinations

def subsets(s):
    combinations_list = []
    
    for n in range(len(s)):
        combinations_list = combinations_list + list(combinations(s, n+1))

    output_list = list(max(combinations_list))
    combinations_list.sort(reverse = True)
    print(combinations_list)
    return "".join(output_list)
    
s = "baca"
print(subsets(s))