'''
@author: Solrac
'''

def find_first_nonDuplicate(s):
    for i in range(len(s)):
        count = s.count(s[i])
        if count == 1:
            print(s[i])
            break
        
def nondup(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            print(s[i])
            break

s = "google"
print(find_first_nonDuplicate(s))
print(nondup(s))