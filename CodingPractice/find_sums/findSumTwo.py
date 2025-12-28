'''
@author: Solrac
'''
def find_sum(lista, x):
    s = 0
    e = len(lista)-1
    while s < e:
        if lista[s] + lista[e] == x:
            return [lista[s], lista[e]]
        elif lista[s] + lista[e] < x:
            s += 1
        else:
            e -= 1
    return -1

lista = [10, 20, 35, 50, 75, 80]
x = 70
print(lista)
print(find_sum(lista, x))