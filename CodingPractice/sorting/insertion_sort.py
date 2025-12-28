'''
@author: Solrac
'''
def insertion_sort(lista):
    for i in range(1, len(lista)):
        insert = lista[i]
        move_item = i
        
        while (move_item > 0) and (lista[move_item-1] > insert):
            lista[move_item] = lista[move_item-1]
            move_item -= 1
        lista[move_item] = insert
    
if __name__ == "__main__":
    lista = [80, 35, 75, 11, 7, 38, 34, 45, 35, 67, 17, 14, 83, 94, 88, 56, 2, 10, 77, 51, 93, 30, 5, 52, 70, 1, 99, 84, 22, 11, 4, 76, 69]
    
    print(lista)
    insertion_sort(lista)
    print(lista)