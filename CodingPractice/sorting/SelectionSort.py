'''
@author: Solrac
'''

def sorting_descending(list_):
    for i in range(len(list_)-1):
        min_= i
        for j in range(i+1, len(list_)):
            if list_[j] < list_[min_]:
                min_= j
        swap(list_, i, min_)
        
def sorting_ascending(list_):
    for i in range(len(list_)-1):
        max_= i
        for j in range(i+1, len(list_)):
            if list_[j] > list_[max_]:
                max_= j
        swap(list_, i, max_)

def swap(list_, first, second):
    temp = list_[first]
    list_[first] = list_[second]
    list_[second] = temp


list_=[35, 56, 4, 10, 77, 51, 93, 30, 5, 52]
print(list_)
sorting_descending(list_)
print(list_)
sorting_ascending(list_)
print(list_)