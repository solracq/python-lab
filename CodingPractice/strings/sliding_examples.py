'''
@author: Solrac
'''
#from collections import deque

def slide_reverse(s, bulk):
    lista = []
    for i in range(0, len(s), bulk):
        lista.append(reverse_string(s[i:bulk+i]))
    return "".join(lista)
    
def reverse_string(s):
    slist = list(s)
    lista = []
    for i in range(len(slist)-1, -1, -1):
        lista.append(slist[i])
    return "".join(lista)

s = "abcdefghijkl"
print(s)
print(slide_reverse(s, 3))
print()

def rotate_left(s, n):
    return s[n:] + s[:n]

def rotate_right(s, n):
    return s[-n:] + s[:-n]

'''def rotation_deque_left(s, n):
    slist = list(s)
    slist = deque(slist)
    slist.rotate(-n)
    slist = list(slist)
    return slist

def rotation_deque_right(s, n):
    slist = list(s)
    slist = deque(slist)
    slist.rotate(n)
    slist = list(slist)
    return slist'''
    
s = [1, 2, 3, 4, 5]
print(s)
print(rotate_left(s, 3))
print(rotate_right(s, 3))
#print(rotation_deque_left(s, 3))
#print(rotation_deque_right(s, 3))