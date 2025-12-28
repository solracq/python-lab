from itertools import groupby

def compression(s):
    arr = list(s)
    groups = []
    res = []
    for key, group in groupby(arr):
        groups.append(list(group))
    for group in groups:
        res.append(str(len(group)) + group[0])
    return "".join(res)

# Execution
s = "AAAABBBCCCCCC"
print(f"Compressing {s} = {compression(s)}")


def compression_altr(s):
    keys = sorted(set(s))
    sorted_s = sorted(s)
    res = ""
    for key in keys:
        i = 0
        while key in sorted_s:
            if sorted_s[0] == key:
                i += 1
                sorted_s.remove(key)
        res += str(i)
        res += key
    return res

def compression_ml(s:str)->str:
    resp = ""
    dup = []
    slist = list(s)
    for i in range(len(s)):
        ch = slist.pop()
        if slist == [] and dup != []:
            dup.append(ch)
            resp += ch
            resp += str(len(dup))
        elif ch != slist[len(slist)-1] and dup == []:
            resp += ch
            resp += str(1)
        elif ch != slist[len(slist)-1] and dup != []:
            dup.append(ch)
            resp += ch
            resp += str(len(dup))
            dup = []
        elif ch == slist[len(slist)-1]:
            dup.append(ch)
    return resp[::-1]