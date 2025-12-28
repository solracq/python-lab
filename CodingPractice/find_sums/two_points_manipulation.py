'''
@author: Solrac
'''

def match_sum(num_list, result):
    s = 0
    e = len(num_list) - 1
    result_list = []
    num_list.sort()
    while s < e :
        if num_list[s] + num_list[e] == result:
            result_list.append(num_list[s])
            result_list.append(num_list[e])
            return result_list
        elif num_list[s] + num_list[e] < result:
            s += 1
        else:
            e -= 1
        
    if result_list == []:
        return 'No sum found!'
    
lista = [50, 10, 80, 20, 75, 35] 
result = 70
print(match_sum(lista, result))
print(match_sum(lista, 20))

def approximate_sum(num_list, result):
    s = 0
    e = len(num_list) - 1
    diff = 1000
    s_res = 0
    e_res= 0
    while s < e:
        if abs(num_list[s] + num_list[e] - result) < diff:
            s_res = s
            e_res = e
            diff = abs(num_list[s] + num_list[e] - result)
        if num_list[s] + num_list[e] < result:
            s += 1
        else:
            e -= 1
    print(num_list[s_res], num_list[e_res], 'Difference=', diff)
    
print()
approximate_sum(lista, 31)

def approximate_sum_twoLists(lista1, lista2, result):
    s = 0
    e = len(lista2) - 1
    s_res = 0
    e_res = 0
    diff = 10000
    while s < len(lista1) and e >= 0:
        if abs(lista1[s] + lista2[e] - result) < diff:
            s_res = s
            e_res = e
            diff = abs(lista1[s] + lista2[e] - result)
        if lista1[s] + lista2[e] < result:
            s += 1
        else:
            e -= 1
    print(lista1[s_res], lista2[e_res], 'Difference =', diff)
     
print("APPROXIMATE SUM TWO LISTS")
lista1 = [1, 4, 5, 7]
lista2 = [10, 20, 30, 40]
result = 38
approximate_sum_twoLists(lista1, lista2, result)

def find_triplets_with_zero(lista):
    s = 0
    e = len(lista) - 1
    main = []
    dup = []
    for i in range(len(lista)-1):
        result = []
        s = set()
        for j in range(i+1, len(lista)):
            r = -(lista[i] + lista[j])
            if r in s:
                result.append(lista[i])
                result.append(lista[j])
                result.append(lista[r])
            else:
                s.add(lista[j])
        main.append(result)
    return main

print("FIND TRIPLESTS W/ZERO")
lista = [0, -1, 2, -3, 1]
print(lista)
print(find_triplets_with_zero(lista))