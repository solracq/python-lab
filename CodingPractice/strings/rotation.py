'''
@author: Solrac
'''

def rotatetoleft(s, n):
    return s[n:] + s[:n]
    
def rotatetoright(s, n):
    return s[-n:] + s[:-n]

s = "abcdefghijkl"
n = 1
print(s)
print(rotatetoleft(s, n))
print(rotatetoright(s, n))
