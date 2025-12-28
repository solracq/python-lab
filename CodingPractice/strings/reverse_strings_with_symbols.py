'''
@author: Solrac
'''

def swap(string, first, second):
    lista = list(string)
    temp = lista[first]
    lista[first] = lista[second]
    lista[second] = temp
    return "".join(lista)
    
def swap_letters_only(string):
    s = 0
    e = len(string) - 1
    
    while s < e:
        if string[s].isalpha() and string[e].isalpha():
            string = swap(string, s, e)
            s += 1
            e -= 1
        elif string[s].isalpha():
            e -= 1
        elif string[e].isalpha():
            s += 1
        else:
            s += 1
            e -= 1
    return string

string = 'a#@b?*c&d!-+@e'
print(string)
print(swap_letters_only(string))