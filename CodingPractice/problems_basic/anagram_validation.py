'''
@author: Solrac
'''
def anagram_validation1(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    
    list1.sort()
    list2.sort()
    count = 0
    
    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)):
        if list1[i] == list2[i]:
            count += 1
            
    if count == len(str2):
        return True
    else:
        return False

def simple_validation(str1, str2):
    validation = False
    
    if len(str1) == len(str2):
        if sorted(str1) == sorted(str2):
            validation = True
    return validation
    
str1 = "cinema"
str2 = "iceman"

print("Are {} and {} anagrams? {}".format(str1, str2, anagram_validation1(str1, str2)))

print("Simple anagram validation between {} and {}: {}".format(str1, str2, simple_validation(str1, str2)))

def dictionary_counter(str_):
    list_ = list(str_)
    dict_ = {}
    duplicate = []
    
    for i in range(len(str_)):
        if list_[i] in duplicate:
            continue
        
        dict_[list_[i]] = str_.count(list_[i])
        
        if str_.count(list_[i]) >= 2:
            duplicate.append(list_[i])
    
    return dict_

def print_dictionary(dict_):
    for key, value in dict_.items():
        print("{} : {}".format(key, value))
        
def compare_dictionaries(dict1, dict2):
    list1 = list(dict1.keys())
    list2 = list(dict2.keys())
    list3 = list(dict1.values())
    list4 = list(dict2.values())

    count_v=0
    count_k=0
    for i in range(len(list1)):
        if list2[i] in list1:  
            count_k += 1
        if list3[i] == list4[i]: 
            count_v += 1

    if (count_k == len(list1)) and (count_v == len(list1)):
        return True
    else:
        return False
 
dict1 = dictionary_counter(str1)
print_dictionary(dict1)
print()
dict2 = dictionary_counter(str2)
print_dictionary(dict2)
print("Are {} and {} anagrams? {}".format(str1, str2, compare_dictionaries(dict1, dict2)))
