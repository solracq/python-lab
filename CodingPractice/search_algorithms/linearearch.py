'''
@author: Solrac
O(n^2)
'''

def linear_search(list_, searchkey):
    location = -1
    for i in range(len(list_)):
        if list_[i] == searchkey:
            location = i
            return location

def linear_search2(list_, searchkey):
    location = -1
    for number in list_:
        if number == searchkey:
            location = list_.index(number) 
            return location

if __name__ == "__main__":
    list_ = [34, 56, 2, 10, 77, 51, 93, 30, 5, 52]
    indx = linear_search(list_, 51)
    print("51 is at", indx)
    print("93 is at", linear_search2(list_, 93))
    print("1 is at", linear_search2(list_, 1))
