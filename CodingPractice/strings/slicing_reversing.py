'''
@author: Solrac
'''

def slicingReversing(s, bulk):
    lista = []
    for i in range(0, len(s), bulk):
        lista.append(reverse(s[i:i+bulk]))
    return "".join(lista)

def reverse(s):
    return s[::-1]

def loquesea(s, bulk):
    resp = []
    for i in range(0, len(s)-1, bulk):
        resp.append(reverse(s[i:i+bulk]))
    return "".join(resp)

# Driver function
if __name__ == "__main__":
    s = "abcdefghijkl"
    print(s)
    # print(slicingReversing(s, 3))
    print()
    print(loquesea(s, 3))

    
