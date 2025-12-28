'''
@author: Solrac
'''

def swap(list_, first, second):
    temp = list_[first]
    list_[first] = list_[second]
    list_[second] = temp
    
def sort(list_):
    for i in range(len(list_)):
        min = i
        for j in range(i+1, len(list_)):
            if list_[min] > list_[j]:
                min = j
        swap(list_, i, min)
    return list_

def binary_search(list_, search_key):
    start = 0
    end = len(list_)
    middle_ = (start + end + 1) / 2
    location = -1
    
    while (location == -1) and (start < end):
        if list_[int(middle_)] == search_key:
            location = int(middle_)
        if search_key < list_[int(middle_)]:
            end = int(middle_) - 1
        else:
            start = int(middle_) + 1
        middle_ = (start + end + 1) / 2
    return location

list_ = [34, 67, 89, 12, 21, 45, 88, 56, 73, 11, 48, 67, 5, 30, 32]
print(list_)
sort(list_)
print(list_)
search_key = 30
print("Searching for {} which is located at {}".format(search_key, binary_search(list_, search_key)))