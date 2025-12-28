'''
@author: Solrac
'''
def bsearch(list_, key):
    start = 0
    end = len(list_)-1
    middle = int((start + end + 1) / 2)
    index = -1
    
    while (start <= end) and (index == -1):
        if key == list_[middle]:
            index = middle
        elif key < list_[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = int((start + end + 1) / 2)
        
    return index

def getMiddle(list_):
    list_size = len(list_)
    middle = 0
    middle1 = 0
    middle2 = 0
    if list_size % 2 != 0:
        middle = (list_size-1)/2
    else:
        middle1 = list_size / 2
        middle2 = middle1 - 1
        if middle1 >= middle2:
            middle = middle1
        else:
            middle = middle2
    return int(middle)

list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1)
print(bsearch(list1, 6))
list2 = [23, 54, 90, 67, 23, 67]
print(list2)
print(bsearch(list2, 67))
list2.sort()
print(list2)
print(bsearch(list2, 67))