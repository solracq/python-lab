'''
@author: Solrac
'''

def find_duplicates(s):
    s_list = s.split(',')
    for i in range(len(s)):
        if s.count(s[i]) == 2:
            return s[i]
    return "not found"

s = "0, 3, 2, 5, 7, 0"
print(s)
print(find_duplicates(s))

def find_duplicates(lista):
    lista.sort()
    pointer = 0
    end_point = len(lista) - 1
    duplicate = []
    duplicate.append(lista[pointer])
    pointer += 1
    while pointer <= end_point:
        if duplicate[len(duplicate)-1] == lista[pointer]:
            return lista[pointer]
            break
        duplicate.append(lista[pointer])
        pointer += 1
    return "not found"

lista = [0, 3, 2, 5, 7, 0]
print(lista)
print(find_duplicates(lista))

def find_non_duplicates(lista):
    lista.sort()
    pointer = 0
    end_point = len(lista) - 1
    nondup = []
    nondup.append(lista[pointer])
    pointer += 1
    while pointer <= end_point:
        if nondup[len(nondup)-1] != lista[pointer]:
            return lista[pointer]
            break
        nondup.append(lista[pointer])
        pointer += 1
    return "not found"

lista = [0, 3, 2, 5, 7, 0]
print(sorted(lista))
print(find_non_duplicates(lista))

def find_dup(nums):
    nums.sort()
    dup = []
    pointer = 0
    e = len(nums) - 1
    while pointer <= e:
        dup.append(nums[pointer])
        pointer += 1
        if pointer <= e:
            if dup[len(dup)-1] == nums[pointer]:
                return True
    return False

nums = [45, 89, 24, 70, 22, 22]
print(nums)
print(find_dup(nums))

def find_dup_set(nums):
    set1 = set(nums)
    if len(set1) != len(nums):
        return True
    else:
        return False
    
print()
print(nums)
print(find_dup_set(nums)) 


