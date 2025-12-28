'''
@author: Solrac
'''

def join_sets(set1: set, set2:set):
    return set1.union(set2)

def intersection_sets(set1: set, set2:set):
    return set1.intersection(set2)

def difference_from_one_set_to_other(set1: set, set2:set):
    return set1.difference(set2)

def symetric_difference_sets(set1:set, set2:set):
    return set1.symmetric_difference(set2)


if __name__ == "__main__":
    num_list = [3, 5, 1, 4, 2]
    alp_list = ["a", "b", "c", "d", "e"]
    num_set = set(num_list) # in order
    alp_set = set(alp_list) # in any order
    print(f"{num_set}\n{alp_set}")
    set_array = {'banana', 'apple', 'mango', 'banana'}
    # Add and remove items in a set
    set_array.add('guava')
    set_array.remove('apple')
    print(set_array)
    set_array = {5, 6, 8, 3, 8, 10} # Numbers are ordered in a set
    set_array.add(7)
    # More on deleting items in a set
    set_array.remove(6)
    print(set_array)
    set_array.discard(10)
    print(f"Discarding elements in {set_array}")
    # Remove a random item
    set_array.pop()
    print(f"Removing random elem: {set_array}")
    diff_items = {"hero", "ikki", "jabu", 1, 2, True, False, 0} # True/False and 1/0 are considered the same value
    print(diff_items)
    # Iterate through a set
    for item in diff_items:
        print(item)
    print("ikki" in diff_items)
    # Update an existing set w/ new items
    diff_items.update(set_array)
    print(diff_items)
    # delete the whole set_array set
    del set_array
    try:
        print(set_array)
    except NameError:
        print("'set_array' set doesn't exist")
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(join_sets(set1, set2))
    print(set1 | set2)
    print(f"joing sets: {set1 & set2}")
    tuple1 = ('a', 'b')
    print(set1.union(tuple1))
    print(intersection_sets(set1, set2))
    print(f"sets diff = {difference_from_one_set_to_other(set1, set2)}")
    print(f"symetric diff = {symetric_difference_sets(set1, set2)}")
    print(sorted(set1 | set2))
    set3 = set1.copy()
    print(set3)
    print(set3.clear())
    print("##########################################")
    print(set1)
    print(set2)
    set3 = {6, 7, 8}
    print(set1.issuperset(set2))
    print(set2.issuperset(set3))




