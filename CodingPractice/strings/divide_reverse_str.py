'''
@author: Solrac
'''
def calculate(s, chunk):
    list_ = []
    for i in range(0, len(s), chunk):
        list_.append(reverse_s(s[i:(i+chunk)]))
    return "".join(list_)   
    
def reverse_s(s):
    list_ = list(s)
    list_rv = []
    for i in range(len(s)-1, -1, -1):
        list_rv.append(list_[i])
        
    s = "".join(list_rv)
    return s
    
s = "testing"
print(s)
print(calculate(s, 3))