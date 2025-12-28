'''
@author: Solrac
'''
def find_duplicate(list_):
    duplicate_list = list()
    for k in range(len(list_)):
        if list_[k] in duplicate_list:  # if duplicate_list.__contains__(list_[k]):
            continue
        for j in range(len(list_)):
            if k == j:
                continue
            if list_[k] == list_[j]:
                duplicate_list.append(list_[j])
                print("duplicate at "+str(list_.index(list_[j]))+" and "+str(list_.index(list_[k])))
                print("frequency of "+list_[j]+" is "+str(list_.count(list_[j])))
    
def is_duplicate(list_):
    if len(list_) == len(set(list_)):
        return False
    else:
        return True
    
def find_duplicates_set(list_):
    set_ = set()
    
    for element in list_:
        if element in set_:
            return True
        else:
            set_.add(element)
    return False

def find_duplicate_count(list_):
    for element in list_:
        if list_.count(element)>1:
            return True
    return False
    