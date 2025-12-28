'''
@author: Solrac
'''
def reduce_list_to_one(lista):
    if len(lista) > 1:
        r = len(lista) - 1
        m = r // 2
        lista_l = lista[:m+1]
        lista_r = lista[m+1:]
        reduce_list_to_one(lista_l)
        reduce_list_to_one(lista_r)
        
def mergeSort(lista):
    if len(lista) > 1:
        right = len(lista) - 1
        middle = right // 2
        L = lista[:middle+1]
        R = lista[middle+1:]
        mergeSort(L)
        mergeSort(R)
        
        i = j = k = 0
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
        
lista = [12, 11, 13, 5, 6, 7]
print(lista)
mergeSort(lista)
print(lista)