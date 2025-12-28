'''
@author: Solrac
'''
def password_validation(s):
    if atleast_one_uppercase(s) and atleast_one_lowercase(s) and min_chars(s, 8) and atleast_one_number(s) and atleast_one_symbol(s):
        return True
    else:
        return False
    
def min_chars(s, min):
    if len(s) >= min:
        return True
    else:
        return False

def atleast_one_uppercase(s):
    count = 0
    for i in range(len(s)):
        if s[i] == s[i].upper():
            count += 1
    if count >= 1 and count <= len(s)-2:
        return True
    else:
        return False

def atleast_one_lowercase(s):
    count = 0
    for i in range(len(s)):
        if s[i] == s[i].lower():
            count += 1
    if count >= 1:
        return True
    else:
        return False

def atleast_one_number(s):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    chars_ = list(s)
    for i in range(len(nums)):
        if nums[i] in chars_:
            return True
    return False
        
def atleast_one_symbol(s):
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '_', '=', '+', '-', '/', '?', '.', '~']
    chars_ = list(s)
    for i in range(len(symbols)):
        if symbols[i] in chars_:
            return True
    return False

s = 'Test@rrosa3'
print("Is {} a valid password? {}".format(s, password_validation(s)))