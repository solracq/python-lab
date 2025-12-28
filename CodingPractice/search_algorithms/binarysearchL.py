'''
@author: Solrac
'''
def sort(list_):
    for i in range(len(list_)):
        min = i
        for j in range(i+1, len(list_)):
            if list_[min] > list_[j]:
                min = j
        swap(list_, i, min)

def swap(list_, first, second):
    temp = list_[first]
    list_[first] = list_[second]
    list_[second] = temp    
    
def binarysearch(list_, searchkey):
    location = -1
    start = 0
    end = len(list_)
    middle = int((start + end + 1) / 2)
    
    while (start < end or location == -1):
        if list_[middle] == searchkey:
            location = middle
        if list_[middle] < searchkey:
            start = middle + 1
        else:
            end = middle - 1
        middle = int((start + end + 1) / 2)
    return location
    
if __name__ == "__main__":
    list_ = [80, 35, 75, 11, 7, 38, 34, 45, 35, 67, 17, 14, 83, 94, 88, 56, 2, 10, 77, 51, 93, 30, 5, 52]
    searchkey = 88
    print(list_)
    sort(list_) 
    print(list_)
    print("Searching for {}... found it at {}".format(searchkey, binarysearch(list_, searchkey)))