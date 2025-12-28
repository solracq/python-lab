def comp(a, b):
    if a == '' or b == '':
        raise Exception("One or two of the strings are empty!")
    if a == b:
        return True
    else:
        return False
str1= ''
str2= 'ab'
print()
print(comp(str1, str2))