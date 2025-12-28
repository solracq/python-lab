'''
@author: Solrac
'''

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400:
                leap = True
    return leap
year = int(input())
print(is_leap(year))
############## PRACTICE ################

