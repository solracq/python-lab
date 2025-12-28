'''
@author: Solrac
'''
def get_all_substrings(s):
    lista = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    print(lista)
    return len(lista)

s = "BANANA"
print(s)
print(get_all_substrings(s))