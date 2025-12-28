'''
@author: Solrac
'''
def remove_vowels(s):
    alist = list(s)
    vlist = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(len(vlist)):
        if vlist[i] in alist:
            while vlist[i] in alist:
                alist.remove(vlist[i])

    res = "".join(alist)
            
    return res
    
s = "Hola Carlitos"
print(remove_vowels(s))