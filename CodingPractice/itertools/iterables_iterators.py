'''
@author: Solrac
'''
from itertools import combinations, compress, permutations, product
from itertools import dropwhile

# function
def subsets(list_, n):
    return list(combinations(list_, n))

def compressing(string_, list_):
    return list(compress(string_, list_))

def permutations_(list_, n):
    return list(permutations(list_, n))

def product_(list_, n):
    return list(product(list_, repeat = n))

def find_probability_letter(n, list_, k):
    combina = list(combinations(range(4), k))
    tot_pos = len(combina)
    probability = 0
    for i in range(len(combina)):
        if (combina[i][0] == 0) or (combina[i][0] == 1) or (combina[i][1] == 0) or (combina[i][1] == 1):
            probability += 1 
    return format(probability/tot_pos, '.3f')
    

# Driver function
if __name__ == "__main__":
    list1_ = ['A', "B", 'C', 'D']
    list2_ = list(range(4))
    
    print("combinations: ")
    print(subsets(list1_, 2))
    print(max(subsets(list1_, 2)))
    print(subsets(list2_, 3))
    print(max(subsets(list2_, 3)))
    print()
 
    n = 2
    list_ = ['A', "B", 'C', 'D']
    print("permutations:")
    print(permutations_(list_, n))
    print(max(permutations_(list_, n)))
    print()
    
    n = 2
    list_ = ['A', "B", 'C', 'D']
    print("product:")
    print(product_(list_, n))
    print(max(product_(list_, n)))
    print()
    
    string_ = 'ABCDEF'
    list_ = [1,0,1,0,1,1]
    print(compressing(string_, list_)) # printing only the ones
    print()
       
    n = 4
    list_ = ['a', 'a', 'c', 'd']
    k = 2
    print(find_probability_letter(n, list_, k))
    
    