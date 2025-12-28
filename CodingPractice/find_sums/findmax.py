'''
@author: Solrac
'''

def findmax(list_):
    max = list_[0];
    
    for i in range(len(list_)-1):
        if max <= list_[i+1]:
            max = list_[i+1]
    
    return max