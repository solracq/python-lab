'''
@author: Solrac
'''
def insert_sort(list_):
    for i in range(1, len(list_)):
        insert = list_[i]  # value to insert
        moveItem = i    # location to place element
        
        # search for place to put current element
        # loop will terminate either when the program reaches 
        # the front of the array or when it reaches an element that is
        # less than the value to be inserted
        while moveItem > 0 and list_[moveItem - 1] > insert:
            # move an element to the right one slot
            list_[moveItem] = list_[moveItem - 1]
            moveItem -= 1
        list_[moveItem] = insert # place inserted element
        
        '''if i == 0 :
            if list_[i] > list_[i+1]:
                swap(list_, i, i+1)
        else:
            temp = i+1
            if list_[temp] < list_[i]:
                swap(list_, i, temp)
            if list_[temp] < list_[i-1]:
                swap(list_, i-1, temp)'''
    
def swap(list_, first, second):
    temp = list_[first]
    list_[first] = list_[second]
    list_[second] = temp

if __name__ == "__main__":
    list_ = [80, 35, 75, 11, 7, 38, 34, 45, 35, 67, 17, 14, 83, 94, 88, 56, 2, 10, 77, 51, 93, 30, 5, 52]
    print(list_)
    insert_sort(list_)
    print(list_)