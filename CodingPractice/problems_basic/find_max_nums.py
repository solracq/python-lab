'''
@author: Solrac
'''

import random

def find_max(*list_):
    max_first = max(list_)
    list_.remove(max_first)
    max_second = max(list_)
    
    result=[max_first, max_second]
    
    print("First Maximum", result[0])
    print("Second Maximum", result[1])
    print()
    
def find_max_(list_):
    list_.sort(reverse=True)
    print(list_)
    print("First Maximum", list_[0])
    print("Second Maximum", list_[1])
    print()
    
def find_max_wo_pdf(list_):
    list_max= []
    max= 0
    
    while len(list_max) <= len(list_):
        max= list_[0]
        i=0
        for cont in range(len(list_)-1):
            if max <= list_[i+1]:
                max = list_[i+1]
            i += 1
        list_max.append(max)
        list_.remove(max)
        
    print(list_max)
    print("First Maximum", list_max[0])
    print("Second Maximum", list_max[1])
    print()
                

list_=[random.randint(10,90), random.randint(10,90), random.randint(10,90), random.randint(10,90), random.randint(10,90), random.randint(10,90), random.randint(10,90), random.randint(10,90)]
print(list_)
find_max(list_)
find_max_(list_)
find_max_wo_pdf(list_)
    