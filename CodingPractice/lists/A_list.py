'''
@author: Solrac
'''
def find_duplicates(array:list):
    duplicates = list()
    for item in array:
        if array.count(item) >= 2:
            if item not in duplicates:
                duplicates.append(item)
    if duplicates != []:
        return f"found duplicates {duplicates}"
    else:
        return "No duplicates found"

def are_duplicated_items(array:list):
    if len(array) == len(set(array)):
        return False
    else:
        return True

def remove_duplicates(pets: list):
    duplicate = []
    for pet in pets:
        if pets.count(pet) >= 2:
            if pet not in duplicate:
                duplicate.append(pet)

    for dpet in duplicate:
        while dpet in pets:
            pets.remove(dpet)
    return pets

def get_common_items(array1:list, array2:list):
    common = []
    for item in array1:
        if item in array2:
            if item not in common:
                common.append(item)
    return common

def get_unique_items(array1:list, array2:list):
    unique = []
    for item in array1:
        if item in unique:
            continue
        if item not in array2:
            unique.append(item)
    return unique

def get_unique_items_set(array1:list, array2:list):
    set1 = set(array1)
    set2 = set(array2)
    unique = set1.difference(set2)
    return list(unique)

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def asc_order_list(array:list):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[min] > array[j]:
                swap(array, min, j)

def desc_order_list(array:list):
    for i in range(len(array)):
        max = i
        for j in range(i+1, len(array)):
            if array[max] < array[j]:
                swap(array, max, j)

def get_min_list(array:list):
    min = array[0]
    for i in range(len(array)-1):
        if min > array[i+1]:
            min = array[i+1]
    return min

def get_max_list(array:list):
    max = array[0]
    for i in range(len(array)-1):
        if max < array[i+1]:
            max = array[i+1]
    return max

def linear_search(array: list, k: int):
    for item in array:
        if item == k:
            return array.index(item)
    return f"{k} not found in {array}"

def binary_search(array: list, k: int):
    l = 0
    r = len(array)-1
    while l <= r:
        m = (l + r) // 2
        if array[m] < k:
            l = m + 1
        elif array[m] > k:
            r = m - 1
        elif array[m] == k:
            return m
    return f"'{k}' is not found in '{array}'"

def insertion_sort(array:list):
    for i in range(1, len(array)):
        print(f"i = {i}")
        key = array[i] # insert item
        print(f"key = {key}")
        j = i -1 # move item
        print(f"j = i-1 = {j}")
        while j >= 0 and key < array[j]:
            print(f"{j}>=0 and {key}<{array[j]}:")
            array[j+1] = array[j]
            print(f"array[{j}+1] = {array[j]}")
            j -= 1
            print(f"j -= 1 =>{j}")
            print(f"array in while: {array}")
        array[j+1] = key
        print(f"{array[j+1]} = {key}")
        print(f"array in for: {array}")



if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 5]
    mythical = ["Unicorn", "Balrog", "Vampire", "Dragon", "Minotaur"]
    print(numbers)
    print(mythical[2:4])
    print(numbers + [7, 6])
    print(numbers.count(5))
    numbers.remove(5)
    print(numbers)
    del numbers[0]
    print(numbers)
    mythical.remove("Balrog")
    print(mythical)
    mythical.sort()
    print(mythical)
    sorted(mythical, reverse=True)
    print(mythical)
    print(sorted(mythical, reverse=True))
    mythical.reverse()
    print(mythical)
    new_array = numbers + mythical
    print(new_array)
    new_array.clear()
    print(new_array)
    print(mythical[-2:] + mythical[:-2])
    mythical = mythical + ['medusa']
    print(mythical)
    print(numbers)
    numbers.pop(2)
    print(numbers)
    # finding duplicates
    array = ["a", "b", "c", "d", "d"]
    print(find_duplicates(array))
    array = ["a", "b", "b", "c", "d", "d"]
    print(find_duplicates(array))
    print(f"Are there duplicate items in {array}: {are_duplicated_items(array)}")
    array = ["a", "b", "c", "d"]
    print(find_duplicates(array))
    print(f"Are there duplicate items in {array}: {are_duplicated_items(array)}")
    numbers = [1, 2, 3, 4, 5, 5]
    print(max(numbers))
    print(min(numbers))
    numbers.extend("3")
    print(numbers)
    numbers[len(numbers)-2]=10
    print(numbers)
    numbers.insert(0, 99)
    print(numbers)
    print(list(range(1,3,1)))
    cubes2 = [i ** 3 for i in range(1, 11)]
    print(cubes2)
    # slicing lists
    subsets = ["a", "b", "c", "d", "e", "f"]
    for subset in subsets[-5:-1]:
        print(subset, end="")
    print()
    subsets.remove("a")
    print(subsets)
    subsets.pop()
    print(subsets)
    subsets.pop(0)
    print(subsets)
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(remove_duplicates(pets))
    arr1 = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
    arr2 = ["THREE", "SEVEN", "EIGHT", "FOUR", "THREE"]
    print(get_common_items(arr1, arr2))
    print(get_unique_items(arr1, arr2))
    print(f"unique items via list: {get_unique_items(arr2, arr1)}")
    print(f"unique items via set: {get_unique_items_set(arr2, arr1)}")
    array = [5, 3, 7, 9, 3, 8, 2]
    print(array)
    asc_order_list(array)
    print(f"min = {array}")
    array = [5, 3, 7, 9, 3, 8, 2]
    print(array)
    desc_order_list(array)
    print(f"max = {array}")
    array = [5, 3, 7, 9, 3, 8, 2]
    print(array)
    print(get_min_list(array))
    print(get_max_list(array))
    array = [5, 3, 7, 9, 3, 8, 2]
    k = 9
    print(array)
    print("linear search: ", linear_search(array, k))
    k = 10
    print("binary search: ", binary_search(array, k))
    insertion_sort(array)
    print("insertion sort: ", array)