'''
@author: Solrac
'''
def reverse_list(s):
    lista = list(s)
    list_ = []
    for i in range(len(lista)-1, -1, -1):
        list_.append(lista[i])
    return "".join(list_)

def reverse_string(s):
    return s[::-1]

s = "Be hungry, be foolish"
print(s)
print(reverse_list(s))
print(reverse_string(s))