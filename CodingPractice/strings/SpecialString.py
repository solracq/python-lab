'''
@author: Solrac
'''
def special_string(n, s):
    count = 0
    for j in range(n-2):
        if s[j] == s[j+1]:
            count += 1
        if s[j] == s[j+2]:
            count += 1
        if s.count(s[j]) == len(s):
            count += 1
    
    count = count + n
    return count
    
s = "abcbaba"
n = len(s)
output = special_string(n, s)
print(output)