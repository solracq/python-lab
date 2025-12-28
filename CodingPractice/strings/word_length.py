'''
@author: Solrac
'''

def calculating_word_length(word):
    if len(word)<=0:
        return "the "+word+" word is "+ str(len(word))
    elif len(word)==1:
        return "the "+word+" word is "+ str(len(word))
    elif len(word)==2:
        return "the "+word+" word is "+ str(len(word))
    elif len(word)==3:
        return "the "+word+" word is "+ str(len(word))
    elif len(word)==4:
        return "the "+word+" word is "+ str(len(word))
    else:
        return "the "+word+" word is equal or bigger than "+ str(len(word))
    
def calculate_counter_while(word):
    count=1
    print("While loop")
    while count <= 10:
        print(str(count)+") "+word)
        count=count+1

def calculate_counter_for(word):
    print("For loop")
    for count in range(1, 11):
        print(str(count)+") "+word)
