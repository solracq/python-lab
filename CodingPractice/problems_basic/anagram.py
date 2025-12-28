'''
@author: Solrac
'''
def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
    
str1 = "cinema"
str2 = "iceman"
print(anagram(str1, str2))