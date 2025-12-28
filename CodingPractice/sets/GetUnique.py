'''
@author: Solrac
'''

def get_common(s1, s2):
    output = []
    
    for i in range(len(s1)):
        if s1[i] in output:
            continue;
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                output.append(s1[i])
                break
    return output

def get_unique(s1, s2):
    unique = []
    for i in range(len(s2)):
        if s2[i] not in s1:
            unique.append(s2[i])
    return unique

def get_common2(s1, s2):
    common = []
    for element in s2:
        if element in common:
            continue
        
        if element in s1:
            common.append(element)
    return common

s1 = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
s2 = ["THREE", "SEVEN", "EIGHT", "FOUR", "THREE"]
print("Common elements", get_common(s1, s2))
print("Unique elements",get_unique(s1, s2))
print("Common elements", get_common2(s1, s2))
set1 = set(s1)
set2 = set(s2)
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))