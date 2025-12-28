'''
@author: Solrac
'''
def first_dup(str):
    for i in range(len(str)):
        if str.count(str[i]) >= 2:
            return str[i]
            break
        else:
            return None
        
def first_dub2(str):
    dict_ = {}
    
    for char_ in str:
        if char_ in str:
            return char_
            break
        else: 
            dict_[char_] +=1
            return None
        
str = "ABCA"
str2 = "BCABA"
str3 = "ABC"
print(first_dup(str))
print(first_dup(str2))
print(first_dup(str3))

print(first_dub2(str))
print(first_dub2(str2))