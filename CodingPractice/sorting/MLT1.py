'''
@author: Solrac
Sorting frequencies
'''
def cutosmSort(arr):
    countList = []
    list1 = []
    list2 = []
    
    for i in range(len(arr)):
        countList.append(arr.count(arr[i]))
    countList.sort()
    set_countList = set(countList)
    countList = list(set_countList)
    countList.sort()
    
    print(arr)
    
    lista = []
    for i in range(len(arr)):
        for j in range(len(countList)):
            if arr.count(arr[i]) == 1:
                list1.append(arr[i])
                list1.sort()
                break;
            else:
                list2.append(arr[i])
                list2.sort()
                break;
        lista = list1 + list2
    print(lista)
    
    '''dict_ = dict()
    for i in range(len(arr)):
        dict_[arr[i]] = arr.count(arr[i])
        
    for key, value in dict_.items():
        if value == 1:
            list1.append(key)
            list1.sort()
        if value == 2:
            j =2
            while j > 0:
                list2.append(key)
                list2.sort() 
                j -= 1
        
    list_ = list1 + list2
    for element in list_:
        print(element)'''
    
arr = [3, 1, 2, 2, 4]
cutosmSort(arr)
    
