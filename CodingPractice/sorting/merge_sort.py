'''
@author: Solrac
'''
def merge_sort(lista):
    if len(lista) > 1:
        e = len(lista) - 1
        m = e // 2
        L = lista[:m+1]
        R = lista[m+1:]
        merge_sort(L)
        merge_sort(R)
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

lista = [14, 83, 68, 39, 26, 35, 70, 55, 60, 70, 53, 38, 38, 54, 60, 26, 35, 47, 51, 53]
print(lista)
merge_sort(lista)
print(lista)